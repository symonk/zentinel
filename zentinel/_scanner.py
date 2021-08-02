from __future__ import annotations

import asyncio
import contextlib
import time
import typing
from typing import Dict

from ._results import ConnectScanResult


class Scanner:
    def __init__(self, target: str):
        self.target = target
        self.ports = set(range(1, 1025))  # TODO: Make this configurable later & smarter.
        self._event_loop = asyncio.get_event_loop()
        self.scan_time = 0.0
        self.scan_results: Dict[str, ConnectScanResult] = {}

    @contextlib.contextmanager
    def benchmark(self) -> typing.Generator[None, None, None]:
        """
        Decorator for benchmarking the actual scan runtime and updating the scanners
        :class:`float` scan_time.  This is used later for reporting.
        """
        start = time.perf_counter()
        yield
        self.scan_time += time.perf_counter() - start

    def execute(self):
        print(f"Scanning: {self.target} for: {self.ports}")

    def __aenter__(self) -> Scanner:
        ...

    def __aexit__(self, exc_type, exc_val, exc_tb) -> Scanner:
        ...
