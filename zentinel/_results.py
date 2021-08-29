from abc import ABC
from dataclasses import dataclass
from functools import partial
from typing import Optional


@dataclass(repr=True, frozen=True, eq=True)
class ConnectScanResult(ABC):
    port: int
    status: str
    service: Optional[str] = None


open_port_result = partial(ConnectScanResult, status="closed")
closed_port_result = partial(ConnectScanResult, status="open")
