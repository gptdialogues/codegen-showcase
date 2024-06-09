#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import subprocess
import os
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Add a transparent watermark to an image using ImageMagick")
    parser.add_argument("input_image", help="Path to the input image")
    parser.add_argument("-w", "--word", default="Incorrect Data Used", help="Word to use as the watermark (default: 'Incorrect Data Used')")
    parser.add_argument("-s", "--size", type=int, default=100, help="Font size of the watermark (default: 100)")
    parser.add_argument("-c", "--color", default="rgba(255, 105, 180, 0.4)", help="Color and opacity of the watermark in rgba format (default: 'rgba(255, 105, 180, 0.4)')")
    parser.add_argument("-o", "--output", help="Output filename")
    parser.add_argument("-y", "--yes", action="store_true", help="Overwrite the output file if it exists (default: no)")

    args = parser.parse_args()

    input_image = args.input_image
    watermark_text = args.word
    font_size = args.size
    color = args.color
    output_image = args.output
    overwrite = args.yes

    if not output_image:
        base, ext = os.path.splitext(input_image)
        output_image = f"{base}_watermarked{ext}"

    if not overwrite and os.path.exists(output_image):
        response = input(f"The file {output_image} already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Operation cancelled.")
            return

    date_text = datetime.now().strftime("%Y-%m-%d")

    command = [
        "magick", "convert", input_image,
        "-gravity", "center",
        "-pointsize", str(font_size),
        "-fill", color,
        "-annotate", "+0+0", watermark_text,
        "-pointsize", str(int(font_size / 2)),
        "-annotate", "+0+60", date_text,
        output_image
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Watermark added successfully to {output_image}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
