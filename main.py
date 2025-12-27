#!/usr/bin/env python3
"""
Starter Python CLI

Usage:
  python main.py greet [name]
  python main.py --version
"""
import argparse

VERSION = "0.1.0"

def greet(name: str) -> None:
    """Print a friendly greeting."""
    print(f"Hello, {name}!")

def main() -> None:
    parser = argparse.ArgumentParser(prog="starter", description="Starter Python CLI")
    parser.add_argument("--version", action="store_true", help="Show version and exit")

    subparsers = parser.add_subparsers(dest="command")
    greet_p = subparsers.add_parser("greet", help="Greet someone")
    greet_p.add_argument("name", nargs="?", default="world", help="Name to greet")

    args = parser.parse_args()

    if args.version:
        print(VERSION)
        return

    if args.command == "greet":
        greet(args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
