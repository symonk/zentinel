from __future__ import annotations

import argparse
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
    return Configuration(**vars(parser.parse_args()))


@dataclass(repr=True, frozen=True)
class Configuration:
    target: str
