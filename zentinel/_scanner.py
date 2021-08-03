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
    def __init__(self, target: str):
        self.target = target
        self.ports = set(range(1, 1025))  # TODO: Make this configurable later & smarter.
        self.scan_time = 0.0
        self.scan_results: Dict[int, ConnectScanResult] = {}

    @contextlib.contextmanager
    def benchmark(self) -> typing.Generator[None, None, None]:
        """
        Decorator for benchmarking the actual scan runtime and updating the scanners
        :class:`float` scan_time.  This is used later for reporting.
        """
        print("Executing coroutines!")
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
            service = socket.getservbyport(port)
            self.scan_results[port] = ConnectScanResult(port, "open", service)
        except OSError:
            self.scan_results[port] = ConnectScanResult(port)

    async def execute(self) -> None:
        with self.benchmark():
            await asyncio.gather(*(self._coroutine_for_port(p) for p in self.ports))

    def __aenter__(self) -> Scanner:
        ...

    def __aexit__(self, exc_type, exc_val, exc_tb) -> Scanner:
        ...
