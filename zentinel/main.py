import asyncio
import typing

from ._argument_parsing import build_configuration
from ._output import StdoutWriter
from ._output import WriterComposite
from ._scanner import Scanner


def main(args: typing.Optional[typing.Sequence[str]] = None) -> int:
    """
    Main entrypoint into zentinel.  This can be called in two ways.
    Preferably by running the `zentinel` command line which is registered via the console_scripts
    entry point, or by calling `zentinel.main()` programmatically within python code.

    :param args: A list of arguments, replacing those which would normally be provided on the command line.
    :return: An integer representing the exit code of executing zentinel.
    """
    zentinel_config = build_configuration(args)
    writer = WriterComposite().add_handler(StdoutWriter())
    scanner = Scanner(zentinel_config.target, zentinel_config.ports, writer)
    asyncio.run(scanner.scan())
    return 0
