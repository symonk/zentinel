import asyncio
import typing

from ._argparse import build_configuration
from ._scanner import Scanner


def main(args: typing.Optional[typing.List[str]] = None) -> int:
    """
    Main entrypoint into zentinel.  This can be called in two ways.
    Preferably by running the `zentinel` command line which is registered via the console_scripts
    entry point, or by calling `zentinel.main()` programmatically within python code.

    :param args: A list of arguments, replacing those which would normally be provided on the command line.
    :return: An integer representing the exit code of executing zentinel.
    """
    zentinel_config = build_configuration()
    scanner = Scanner(zentinel_config.target, zentinel_config.ports)
    asyncio.run(scanner.perform_scan())
    print("open port summary".center(100, "-"))
    print(scanner.open_ports)
    return 0
