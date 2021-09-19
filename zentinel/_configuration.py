import dataclasses
import typing


@dataclasses.dataclass(repr=True, frozen=True, eq=True)
class Configuration:
    """
    A representation of configuration for a zentinel scan.
    """

    target: str
    ports: typing.Set[int]
