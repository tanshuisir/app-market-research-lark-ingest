#!/usr/bin/env python3
"""Resize store screenshots to one height and stitch them horizontally."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def positive_int(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return number


def stitch(inputs: list[Path], output: Path, target_height: int | None, quality: int) -> tuple[int, int]:
    images: list[Image.Image] = []
    try:
        for path in inputs:
            with Image.open(path) as source:
                images.append(ImageOps.exif_transpose(source).convert("RGB"))

        height = target_height or max(image.height for image in images)
        resized: list[Image.Image] = []
        for image in images:
            width = max(1, round(image.width * height / image.height))
            resized.append(image.resize((width, height), Image.Resampling.LANCZOS))

        canvas = Image.new("RGB", (sum(image.width for image in resized), height), "white")
        x = 0
        for image in resized:
            canvas.paste(image, (x, 0))
            x += image.width

        output.parent.mkdir(parents=True, exist_ok=True)
        save_args = {"quality": quality, "optimize": True} if output.suffix.lower() in {".jpg", ".jpeg"} else {}
        canvas.save(output, **save_args)
        return canvas.size
    finally:
        for image in images:
            image.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", type=Path, help="screenshots in store order")
    parser.add_argument("--output", "-o", required=True, type=Path, help="stitched PNG or JPEG")
    parser.add_argument("--target-height", type=positive_int, help="output height; defaults to tallest input")
    parser.add_argument("--quality", type=positive_int, default=92, help="JPEG quality (default: 92)")
    args = parser.parse_args()

    missing = [str(path) for path in args.inputs if not path.is_file()]
    if missing:
        parser.error("input files not found: " + ", ".join(missing))
    if not 1 <= args.quality <= 100:
        parser.error("--quality must be between 1 and 100")

    width, height = stitch(args.inputs, args.output, args.target_height, args.quality)
    print(f"Created {args.output} ({width}x{height}) from {len(args.inputs)} screenshots.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
