from __future__ import annotations

import asyncio
import contextlib
import functools
import socket
import time
import typing
from typing import Dict

from ._results import ConnectScanResult


class Scanner:
    def __init__(self, target: str, ports: typing.Set[int]):
        self.target = target
        self.ports = ports
        self.scan_time = 0.0
        self.scan_results: Dict[int, ConnectScanResult] = {}

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

    @functools.cached_property
    def open_ports(self) -> Dict[int, ConnectScanResult]:
        return {k: v for k, v in self.scan_results.items() if v.status == "open"}

    @functools.cached_property
    def closed_ports(self) -> Dict[int, ConnectScanResult]:
        return {k: v for k, v in self.scan_results.items() if v.status == "closed"}

    async def _coroutine_for_port(self, port: int) -> None:
        try:
            await asyncio.open_connection(self.target, port)
            # todo: is this blocking?
            service = socket.getservbyport(port, "tcp")
            self.scan_results[port] = ConnectScanResult(port, "open", service)
        except OSError:
            self.scan_results[port] = ConnectScanResult(port)

    async def execute(self) -> None:
        async with self.benchmark():
            await asyncio.gather(*(self._coroutine_for_port(p) for p in self.ports))
