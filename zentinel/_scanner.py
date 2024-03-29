from __future__ import annotations

import asyncio
import socket
import typing
from typing import Dict

from ._constants import TCP_PROTOCOL_NAME
from ._output import Writable
from ._performance import BenchMarker
from ._results import ClosedPortResult
from ._results import OpenPortResult
from ._results import ScanResult


@typing.runtime_checkable
class Scannable(typing.Protocol):
    """
    A simple protocol for something which can perform a port scan.
    """

    async def scan(self) -> None:
        """
        Perform a port scan.
        """


class Scanner(Scannable):
    """
    Responsible for performing the actual TCP port scan.  By default it will perform
    a full TCP connect scan (SYN->SYN-ACK->ACK) against all of the specified ports.
    Scanner is completely asynchronous and as a result it will scan a remote server with
    lightning speed.

    :param target: The target url, localhost by default
    :param ports: A distinct set of ports to scan
    :param writer: A Writable instance, responsible for managing output, stdout by default.
    """

    def __init__(self, target: str, ports: typing.Set[int], writer: Writable):
        self.target = target
        self.ports = ports
        self.scan_time = 0.0
        self.open_ports: Dict[int, ScanResult] = {}
        self.closed_ports: Dict[int, ScanResult] = {}
        self.writer = writer

    async def _coroutine_for_port(self, port: int) -> None:
        """
        Performs a TCP connect scan against the port.  if the port is open it will
        subsequently attempt to resolve which service is running on that port,
        this may not always be possible tho.  In the event that the TCP connection
        fails we will also store the closed port information for inspection later

        :param port: The (integer) port to perform a full TCP connect / scan against
        :return: None
        """
        try:
            _ = await asyncio.open_connection(self.target, port)
            service = socket.getservbyport(port, TCP_PROTOCOL_NAME)  # Todo: Limitation on TCP services for future.
            self.open_ports[port] = OpenPortResult(port=port, service=service)
        # TODO: Is this exception handling sufficient? needs investigation.
        except OSError:
            self.closed_ports[port] = ClosedPortResult(port=port)

    async def scan(self) -> None:
        """
        Gathers a coroutine for each port in the port range provided at runtime
        and schedules them to be executed in the asyncio event loop.
        _coroutine_for_port does not return anything, so the result set here is
        negligible; results are appending to self.open_ports | self.closed_ports
        for inspection later.
        :return: None
        """
        self.writer.write(f"Launching port scan against: {self.target}, total ports: {len(self.ports)}")
        message = f"Executing coroutines for ports in range: {min(self.ports)} -> {max(self.ports)}"

        async with BenchMarker(self.writer, message):
            await asyncio.gather(*(self._coroutine_for_port(port) for port in self.ports))
            await self.report()

    async def report(self) -> None:
        """Handles report and summary information to the writer."""
        self.writer.write("open port summary".center(100, "-"))
        if ports := self.open_ports:
            self.writer.write(str(ports))
            return
        self.writer.write("No open ports.")
