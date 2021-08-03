from dataclasses import dataclass


@dataclass(repr=True, frozen=True, eq=True)
class ConnectScanResult:
    port: int
    status: str = "closed"
    service: str = "unknown"
