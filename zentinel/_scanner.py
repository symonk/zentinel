from __future__ import annotations

import asyncio
import contextlib
import socket
import time
import typing
from typing import Dict

from ._constants import TCP_PROTOCOL_NAME
from ._results import ScanResult
from ._results import closed_port_result
from ._results import open_port_result


class Scanner:
    """
    The scanner instance is carries the brunt of the port scanning activity.  By
    default it will perform a full TCP connect scan (SYN->SYN-ACK->ACK) against
    all of the specified ports.  Scanner is completely asynchronous and as a result
    it will scan a remote server with lightning speed, however this can potentially
    overwhelm a server so care is advised.

        :param target: The target url, localhost by default
        :param ports: A distinct collection of ports to scan
    """

    def __init__(self, target: str, ports: typing.Set[int]):
        self.target = target
        self.ports = ports
        self.scan_time = 0.0
        self.open_ports: Dict[int, ScanResult] = {}
        self.closed_ports: Dict[int, ScanResult] = {}

    @contextlib.asynccontextmanager
    async def benchmark(self) -> typing.AsyncGenerator[None, None]:
        """
        Decorator for benchmarking the actual scan runtime and updating the scanners
        :class:`float` scan_time.  This is used later for reporting.
        """
        print(f"Executing coroutines for ports in range: {min(self.ports)} -> {max(self.ports)}")
        start = time.perf_counter()
        yield
        end_time = time.perf_counter() - start
        print(f"Total scan duration: {end_time} seconds")
        self.scan_time += end_time

    async def _coroutine_for_port(self, port: int) -> None:
        try:
            _ = await asyncio.open_connection(self.target, port)
            service = socket.getservbyport(port, TCP_PROTOCOL_NAME)
            self.open_ports[port] = open_port_result(port=port, service=service)
        except OSError:
            self.closed_ports[port] = closed_port_result(port=port)

    async def execute(self) -> None:
        async with self.benchmark():
            await asyncio.gather(*(self._coroutine_for_port(p) for p in self.ports))
