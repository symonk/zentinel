import asyncio

from ._argparse import build_configuration
from ._scanner import Scanner


def main():
    zentinel_config = build_configuration()
    scanner = Scanner(zentinel_config.target, zentinel_config.ports)
    asyncio.run(scanner.execute())
    print("open port summary".center(100, "-"))
    print(scanner.open_ports)
    return 125
