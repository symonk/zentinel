class ConnectScanResult:
    def __init__(self, port: int, status: str = "closed") -> None:
        self.port = port
        self.status = status
