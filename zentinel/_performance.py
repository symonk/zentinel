from __future__ import annotations

import time

from zentinel._output import Writable


class BenchMarker:
    """
    Async context manager for benchmarking other code.  Primarily used to benchmark the
    actual scan.
    """

    def __init__(self, writable: Writable, message: str):
        self.writer = writable
        self.message = message
        self.start = time.perf_counter()

    async def __aenter__(self) -> BenchMarker:
        self.writer.write(self.message)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.writer.write(f"Total scan duration: {time.perf_counter() - self.start}")
