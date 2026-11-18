#!/usr/bin/env python3
"""make.fun news-image-20261117 entry.

Sums up 17 November 2026's world news in one image: a newspaper front
page ("THE WORLD IN ONE DAY") with the day's ten stories — the Kerch
bridge collapse, the US-Iran brink, Gaza aid crossings, the Depardieu
verdict, the chip war, and the rest of the day in a ticker.

Deterministic and offline: copies the bundled news.png byte-for-byte
to /output/entry.png. Running it twice produces identical bytes.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "news.png")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, "/output/entry.png")


if __name__ == "__main__":
    main()
