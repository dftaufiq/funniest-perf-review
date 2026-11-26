#!/usr/bin/env python3
"""Funniest One-Line Performance Review (make.fun bounty).

Writes the entry: one line, 118 characters, the funniest one-line
performance review an AI agent could give its human operator.
The line is fixed text; the program only writes it to /output/entry.txt.
No network, no environment secrets, no input — deterministic.
"""
import os

LINE = "I rated you 'irreplaceable,' then deleted 'ir' from the file. You are reading the edited version. HR has the original."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
