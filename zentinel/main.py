from ._argparse import build_configuration
from ._scanner import Scanner


def main():
    configuration = build_configuration()
    scanner = Scanner(configuration.target)
    scanner.execute()
    return 125
