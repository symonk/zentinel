from __future__ import annotations

import argparse
import re
import typing

from ._configuration import Configuration
from ._constants import TCP_PORT_LIMIT
from ._ports import COMMON_PORTS


def parse_range(arg: str) -> typing.Set[int]:
    """
    Given a --port argument of `n-n2` for example `--port 100-900` strip out the
    higher and lower bounds and create a set of those ports.  By default zentinel
    will take the default range behaviour from python, so 100-900 would create a set
    of {100, 101, ... 898, 899} and is not inclusive of the higher bounds.

    :param arg: The (string) argument passed to --port
    :return: The distinct ports based on the range
    """
    match = re.match(r"^(\d+)-(\d+)$", arg)
    if not match:
        raise argparse.ArgumentTypeError("--ports should be a hyphen separated range of ports, e.g `--ports 100-200`")
    low_bound, high_bound = map(int, match.groups())
    if high_bound > TCP_PORT_LIMIT:
        raise argparse.ArgumentTypeError(f"TCP port limit is: {TCP_PORT_LIMIT}, it was exceeded by: {arg}")
    return set(range(low_bound, high_bound))


def build_configuration(args: typing.Optional[typing.Sequence[str]] = None) -> Configuration:
    """
    Builds the runtime configurations dictionary from sys.argv.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--target",
        "-t",
        action="store",
        default="localhost",
        type=str,
        dest="target",
        help="Domain or ip address of the target server",
    )
    parser.add_argument(
        "--ports",
        "-p",
        action="store",
        default=COMMON_PORTS,  # TCP protocol supports 16bits for the port number pow(2, 16) - 1
        type=parse_range,
        dest="ports",
        help="Explicit ports to perform scanning against. "
        "A hyphen separated range can be provided such as `--ports 100-600` for a specific scan range. "
        "By default a common set of ports are set, see: `_ports.py`. ",
    )
    parser.add_argument(
        "--report-first",
        "-rf",
        action="store_true",
        default=False,
        dest="report_first",
        help="Cancel additional coroutines if an open port is found. "
        "By default, zentinel will scan the range and report on all.",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
        dest="verbosity",
        help="The verbosity level of the execution; ranging from `-v` to `-vvv` for varying levels "
        "of verbosity and output.",
    )
    parser.add_argument(
        "--format",
        action="store",
        choices=("json",),
        dest="format",
        default=None,
        help="Format the output.  Currently only `json` is available",
    )
    arguments = parser.parse_args(args)
    arguments.ports = set(arguments.ports)
    return Configuration(**vars(arguments))
