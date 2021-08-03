import asyncio

from ._argparse import build_configuration
from ._scanner import Scanner


def main():
    configuration = build_configuration()
    scanner = Scanner(configuration.target)
    asyncio.run(scanner.execute())
    print("open port summary".center(100, "-"))
    print(scanner.open_ports)
    return 125
