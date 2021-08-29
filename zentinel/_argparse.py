from __future__ import annotations

import argparse
import typing
from dataclasses import dataclass


def build_configuration() -> Configuration:
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
        default=range(1025),
        dest="ports",
        help="Explicit ports to perform scanning against",
    )
    arguments = parser.parse_args()
    arguments.ports = set(arguments.ports)
    return Configuration(**vars(arguments))


@dataclass(repr=True, frozen=True, eq=True)
class Configuration:
    target: str
    ports: typing.Set[int]
