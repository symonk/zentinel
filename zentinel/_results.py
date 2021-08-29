from abc import ABC
from dataclasses import dataclass
from functools import partial
from typing import Optional

from ._constants import CLOSED_STATUS
from ._constants import OPEN_STATUS


@dataclass(repr=True, frozen=True, eq=True)
class ScanResult(ABC):
    port: int
    status: str
    service: Optional[str] = None


open_port_result = partial(ScanResult, status=OPEN_STATUS)
closed_port_result = partial(ScanResult, status=CLOSED_STATUS)
