from __future__ import annotations

import contextlib
import json
import typing
from typing import Protocol


class Formattable(Protocol):
    def format(self, /, text: str) -> str:
        """
        Given a string, format it in some appropriate way.
        :param text: the original (unformatted) string.
        :return: The formatted string.
        """
        raise NotImplementedError


class JsonFormatter(Formattable):
    def format(self, /, text: str) -> str:
        """
        Convert the text into a json representation of itself.
        :param text: The unformatted text
        :return: The formatted text
        """
        return str(json.loads(text))


class Writable(Protocol):
    def write(self, /, text: str) -> None:
        """Write the message to the chosen stream."""
        raise NotImplementedError


class StdoutWriter(Writable):
    def write(self, /, text: str) -> None:
        print(text, flush=True)


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
