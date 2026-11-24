#!/usr/bin/env python3
"""Publish the 24 November 2026 front page as the competition entry.

The newspaper image ships in this repository as ``front-page.png``.
This script does no drawing and no networking: it checks that the
shipped file really is a 1024x1024 PNG and then writes an exact copy
to ``$MAKEFUN_OUTPUT_DIR/entry.png`` (``/output`` when the variable
is unset). Copying byte for byte means repeated runs agree exactly.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
SOURCE_NAME = "front-page.png"
TARGET_NAME = "entry.png"


def fail(message):
    print(f"main.py: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_source():
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        fail(f"missing {SOURCE_NAME} next to {Path(__file__).name}")
    return source.read_bytes()


def check_png(data):
    if data[:8] != PNG_MAGIC:
        fail("front-page.png does not start with the PNG signature")
    if len(data) < 33 or data[12:16] != b"IHDR":
        fail("front-page.png has no IHDR chunk where one is expected")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail(f"front-page.png is {width}x{height}, expected 1024x1024")
    return width, height


def main():
    data = read_source()
    check_png(data)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / TARGET_NAME
    target.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    # Re-read what landed on disk so a short write can never pass
    # silently: the entry must be the shipped image, byte for byte.
    written = target.read_bytes()
    if hashlib.sha256(written).hexdigest() != digest:
        fail(f"{target} does not match the shipped image after writing")
    print(f"wrote {target} ({len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
