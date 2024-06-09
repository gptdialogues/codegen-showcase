#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
from PIL import Image
from typing import List

def convert_images_to_pdf(image_files: List[str], output_file: str) -> None:
    """
    Convert multiple image files to a single PDF file.

    :param image_files: List of paths to the image files to be combined.
    :param output_file: Path to the output PDF file.
    """
    images = [Image.open(image_file).convert('RGB') for image_file in image_files]
    images[0].save(output_file, save_all=True, append_images=images[1:])

def get_output_filename(base_name: str, suffix: str = "_combined", ext: str = ".pdf") -> str:
    """
    Generate the output filename by appending a suffix to the base name.

    :param base_name: Base name of the output file.
    :param suffix: Suffix to append to the base name.
    :param ext: File extension for the output file.
    :return: Generated output filename.
    """
    base, _ = os.path.splitext(base_name)
    return base + suffix + ext

def main():
    parser = argparse.ArgumentParser(description="Combine multiple image files into a single PDF file.")
    parser.add_argument("image_files", nargs='+', help="List of image files to combine.")
    parser.add_argument("-o", "--output", help="Name of the output PDF file.")
    args = parser.parse_args()

    if args.output:
        output_file = args.output
    else:
        output_file = get_output_filename(args.image_files[0])

    if os.path.exists(output_file):
        overwrite = input(f"{output_file} already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Operation cancelled.")
            return

    convert_images_to_pdf(args.image_files, output_file)
    print(f"PDF file created: {output_file}")

if __name__ == "__main__":
    main()
