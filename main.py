#!/usr/bin/env python3
"""Deliver the news-image-20261121 front page.

The page itself is drawn at build time (PIL + DejaVu, see build/draw2.py)
from the verified stories of Saturday 21 November 2026, and shipped in this
repository as entry.png. Round 2 rebuilt the drawn scenes as composed
settings — a Lima street, a COP31 hall, the Las Vegas strip — while the
stories, numbers and layout stayed exactly as submitted in round 1. This
program only carries that image into the grader's output directory.

Why a copy instead of a redraw: the grader's Python is standard library
only, so it has no image library. Copying keeps the run deterministic —
the same bytes leave on every run — and the checks below make sure the
bundled image is exactly the one that was drawn and verified: PNG magic,
1024x1024, exact byte size, exact SHA-256.

Standard library only. No network, no clock, no randomness.
"""
import hashlib
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGE = os.path.join(ROOT, "entry.png")

WANT_SHA256 = "cc1b2ed2544374354fdc53ee08aee517b8105c8cb4b3ff45ddfdff4ddaa087ed"
WANT_BYTES = 171131
WANT_W, WANT_H = 1024, 1024
MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    sys.exit("entry check failed: " + message)


def read_image():
    """Read the bundled image and check it is the expected file."""
    with open(IMAGE, "rb") as handle:
        data = handle.read()
    if len(data) != WANT_BYTES:
        fail("entry.png is %d bytes, expected %d" % (len(data), WANT_BYTES))
    if data[:8] != MAGIC:
        fail("entry.png does not begin with the PNG magic bytes")
    # In a PNG the width and height sit at bytes 16..24 as two big-endian
    # 32-bit integers, right after the 8-byte magic and the IHDR header.
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if (width, height) != (WANT_W, WANT_H):
        fail("entry.png is %dx%d, expected %dx%d"
             % (width, height, WANT_W, WANT_H))
    digest = hashlib.sha256(data).hexdigest()
    if digest != WANT_SHA256:
        fail("entry.png sha256 mismatch, got %s" % digest)
    return data


def output_dir():
    """The grader's output directory, created if it is missing."""
    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target, exist_ok=True)
    return target


def main():
    data = read_image()
    dest = os.path.join(output_dir(), "entry.png")
    shutil.copyfile(IMAGE, dest)
    print("wrote %s (%d bytes)" % (dest, len(data)))


if __name__ == "__main__":
    main()
