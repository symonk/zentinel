from abc import ABC
from dataclasses import dataclass
from functools import partial
from typing import Optional


@dataclass(repr=True, frozen=True, eq=True)
class ScanResult(ABC):
    port: int
    status: str
    service: Optional[str] = None


open_port_result = partial(ScanResult, status="open")
closed_port_result = partial(ScanResult, status="closed")
