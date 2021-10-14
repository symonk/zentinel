from __future__ import annotations

import time
import types
import typing

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

    async def __aexit__(
        self,
        exc_type: typing.Optional[typing.Type[BaseException]],
        exc_val: typing.Optional[BaseException],
        traceback: typing.Optional[types.TracebackType],
    ):
        self.writer.write(f"Total scan duration: {time.perf_counter() - self.start}")
