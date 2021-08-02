from . import _argparse
from ._scanner import Scanner


def main():
    configuration = _argparse.build_configuration()
    scanner = Scanner(configuration.target)
    scanner.execute()
    return 125
