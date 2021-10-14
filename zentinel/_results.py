from abc import ABC
from dataclasses import dataclass
from typing import Optional

from ._constants import CLOSED_STATUS
from ._constants import OPEN_STATUS


@dataclass(repr=True, frozen=True, eq=True)
class ScanResult(ABC):
    """
    Stores the results of an individual scan against a particular port.
    """

    port: int
    status: str


@dataclass(frozen=True)
class OpenPortResult(ScanResult):
    """
    Created when a port post-scan is considered `OPEN`
    """

    status: str = OPEN_STATUS
    service: Optional[str] = None


@dataclass(frozen=True)
class ClosedPortResult(ScanResult):
    """
    Created when a port post-scan is considered `CLOSED`.  (Mostly for reporting purposes).
    """

    status: str = CLOSED_STATUS
