from __future__ import annotations

import contextlib
import typing
from typing import Protocol


class Writable(Protocol):
    def write(self, /, text: str) -> None:
        """ Write the message to the chosen stream."""
        raise NotImplementedError


class StdoutWriter(Writable):

    def write(self, /, text: str) -> None:
        print(text)


class WriterComposite(Writable):
    """
    Compose a sequence of writable objects so that when writing output we can easily
    write it to multiple places if required.
    """
    def __init__(self) -> None:
        self.handlers: typing.MutableSequence[Writable] = []

    def add_handler(self, handler: Writable) -> WriterComposite:
        if handler not in self.handlers:
            self.handlers.append(handler)
        return self

    def revoke(self, handler: Writable) -> WriterComposite:
        with contextlib.suppress(ValueError):
            self.handlers.remove(handler)
        return self

    def write(self, /, text: str) -> None:
        for handler in self.handlers:
            handler.write(text)
