import argparse

from .metrics import aggregate
from .models import Event
from .reporting import report


def main() -> None:
    parser = argparse.ArgumentParser(prog="ga")
    commands = parser.add_subparsers(dest="command", required=True)
    command = commands.add_parser("report")
    command.add_argument("--min-conversions-per-arm", type=int, default=0)
    args = parser.parse_args()
    sample = aggregate([
        Event("1", "search", "impression"), Event("2", "search", "click"),
        Event("3", "search", "conversion"), Event("4", "social", "impression"),
    ])
    print(report(sample, args.min_conversions_per_arm))


if __name__ == "__main__":
    main()
