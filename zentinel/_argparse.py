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
    parser.add_argument(
        "--half-open",
        "--syn-ack-only",
        action="store_true",
        default=False,
        dest="half_open",
        type=bool,
        help="Should zentinel avoid establishing the full 3-way handshake on each port and drop after SYN-ACK",
    )
    return Configuration(**vars(parser.parse_args()))


@dataclass(repr=True, frozen=True)
class Configuration:
    target: str
