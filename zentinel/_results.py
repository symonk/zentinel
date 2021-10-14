from abc import ABC
from dataclasses import dataclass
from typing import Optional

from ._constants import CLOSED_STATUS
from ._constants import OPEN_STATUS


@dataclass(repr=True, frozen=True, eq=True)
class ScanResult(ABC):
    port: int
    status: str
    service: Optional[str] = None


@dataclass(frozen=True)
class OpenPortResult(ScanResult):
    status: str = OPEN_STATUS


@dataclass(frozen=True)
class ClosedPortResult(ScanResult):
    status: str = CLOSED_STATUS
