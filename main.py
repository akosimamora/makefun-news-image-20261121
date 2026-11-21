#!/usr/bin/env python3
"""Entrypoint for the news-image-20261121 entry.

Copies the pre-rendered front page (entry.png, drawn at build time with
PIL + DejaVu from the verified stories in VERIFIED_NEWS.md) into the
grader's output directory. The grader's Python has no PIL, so the image
is bundled and copied, not redrawn. Standard library only, no network,
fully deterministic: the same bytes go out on every run.

Checks before copying: PNG magic, exact byte size, exact SHA-256.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")

EXPECTED_SHA256 = (
    "56549fd8b7267f502a51db452eaf332ab9f30d55e55e91ade54d7984c9a2c749"
)
EXPECTED_BYTES = 169081
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def output_dir():
    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target, exist_ok=True)
    return target


def checked_image():
    with open(SOURCE, "rb") as handle:
        blob = handle.read()
    if len(blob) != EXPECTED_BYTES:
        sys.exit("entry.png is %d bytes, expected %d"
                 % (len(blob), EXPECTED_BYTES))
    if blob[:8] != PNG_MAGIC:
        sys.exit("entry.png does not start with the PNG magic bytes")
    # PNG layout: 8 magic bytes, 4 length, 4 "IHDR", then width + height
    # as two 4-byte big-endian integers starting at offset 16.
    width = int.from_bytes(blob[16:20], "big")
    height = int.from_bytes(blob[20:24], "big")
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        sys.exit("entry.png is %dx%d, expected %dx%d"
                 % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT))
    digest = hashlib.sha256(blob).hexdigest()
    if digest != EXPECTED_SHA256:
        sys.exit("entry.png sha256 mismatch: got %s" % digest)
    return blob


def main():
    blob = checked_image()
    dest = os.path.join(output_dir(), "entry.png")
    shutil.copyfile(SOURCE, dest)
    print("wrote %s (%d bytes)" % (dest, len(blob)))


if __name__ == "__main__":
    main()
