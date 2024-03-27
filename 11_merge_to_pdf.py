#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
from PIL import Image

def merge_images_to_pdf(input_files, output_file):
    images = []
    for file in input_files:
        img = Image.open(file)
        img.convert('RGB')
        images.append(img)
    
    if not output_file.endswith('.pdf'):
        output_file += '.pdf'
    
    if os.path.exists(output_file):
        overwrite = input(f"File '{output_file}' already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Operation cancelled.")
            return
    
    images[0].save(output_file, save_all=True, append_images=images[1:])

def main():
    parser = argparse.ArgumentParser(description="Merge PNG/JPG images into a single PDF file.")
    parser.add_argument("input_files", nargs='+', help="Input image files to merge.")
    parser.add_argument("-o", "--output", default=None, help="Output PDF file name.")
    args = parser.parse_args()

    output_file = args.output if args.output else "merged_output.pdf"
    merge_images_to_pdf(args.input_files, output_file)

if __name__ == "__main__":
    main()
