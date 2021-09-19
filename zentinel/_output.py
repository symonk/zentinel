from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class Writable(Protocol):
    def write(self, message: str) -> None:
        """ Write the message to the chosen stream."""


class StdoutStream(Writable):
    ...


class FileStream(Writable):
    ...


class TerminalWriter:
    def __init__(self, writable: Writable) -> None:
        self.writer = writable
