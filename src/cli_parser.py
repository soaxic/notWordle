import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="notWordle. A game like Wordle, but not!")

    parser.add_argument(
        "-D",
        "--debug",
        "--Debug",
        action="store_true",
        help="Enable debugging mode"
    )

    parser.add_argument(
        "-s",
        "--seed",
        "--Seed",
        type=int,
        default=None,
        help="Set the seed for randomization. E.g. '-s 1234'"
    )

    return parser

def parse_cli_arguments():
    parser = get_parser()
    return parser.parse_args()