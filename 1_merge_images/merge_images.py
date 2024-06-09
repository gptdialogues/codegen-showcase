#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from typing import List
from PIL import Image
import argparse

def merge_images_to_pdf(image_files: List[str], output_filename: str) -> None:
    """
    Merges a list of images into a single PDF file.

    :param image_files: List of paths to the image files to be merged.
    :param output_filename: The name of the output PDF file.
    """
    images = [Image.open(image_file).convert('RGB') for image_file in image_files]
    if images:
        images[0].save(output_filename, save_all=True, append_images=images[1:])

def confirm_overwrite(filename: str) -> bool:
    """
    Asks user for confirmation before overwriting an existing file.

    :param filename: The name of the file to be potentially overwritten.
    :return: True if the user confirms, False otherwise.
    """
    if os.path.exists(filename):
        response = input(f"File '{filename}' already exists. Overwrite? (y/n): ").strip().lower()
        return response == 'y'
    return True

def get_default_output_filename(image_files: List[str]) -> str:
    """
    Generates a default output filename based on the first image file name.

    :param image_files: List of paths to the image files.
    :return: The default output PDF file name.
    """
    base_name = os.path.splitext(os.path.basename(image_files[0]))[0]
    return f"{base_name}_merged.pdf"

def main():
    parser = argparse.ArgumentParser(description='Merge multiple images into a single PDF file.')
    parser.add_argument('images', metavar='IMAGE', type=str, nargs='+', help='Image files to merge')
    parser.add_argument('-o', '--output', type=str, help='Output PDF file name')
    args = parser.parse_args()

    output_filename = args.output if args.output else get_default_output_filename(args.images)
    
    if confirm_overwrite(output_filename):
        merge_images_to_pdf(args.images, output_filename)
        print(f"PDF file created: {output_filename}")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()
