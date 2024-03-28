#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
from PIL import Image

def rotate_image(input_path, output_path):
    with Image.open(input_path) as img:
        rotated_img = img.rotate(270, expand=True)
        rotated_img.save(output_path)

def main():
    parser = argparse.ArgumentParser(description="Rotate an image by 90 degrees.")
    parser.add_argument("input", help="Path to the input image (PNG/JPG).")
    parser.add_argument("-o", "--output", help="Path to the output image. Default is input filename with '_rotated' suffix.", default=None)
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_rotated{ext}"

    if os.path.exists(output_path):
        overwrite = input(f"{output_path} already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Operation cancelled.")
            return

    rotate_image(input_path, output_path)
    print(f"Image rotated and saved to {output_path}")

if __name__ == "__main__":
    main()
