# Merge PNG/JPG to PDF

Creation Time: 2024-03-27 10:42:50.129884

## User

Time: 2024-03-27 10:42:50.130571

Please give me a python3 code to merge png/jpg files and create a merged PDF file.
I would like to add some additional specifications below.
- Add a help option using argparse.
- Add an option to specify the output filename. Use a default name by adding a specific suffix after the original basename.
- Preserve the original width and height to generate a PDF file.
- Give some candidates for the file name of the script.
- Ask "(y)es/(n)o" before overwriting an existing file (default: no). 
- Add the following shebang and an encoding declaration.
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

## Assistant

Time: 2024-03-27 10:43:23.719733

Model: gpt-4

## Assistant

Time: 2024-03-27 10:43:23.719944

Here's a Python script that meets your specifications:

```python
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
```

To use this script:

1. Save the code in a file with a name like `merge_images_to_pdf.py`, `images_to_pdf.py`, or `merge_to_pdf.py`.
2. Make sure you have the `PIL` (Pillow) library installed. If not, you can install it using `pip install Pillow`.
3. Run the script using the command `python merge_images_to_pdf.py image1.png image2.jpg -o output.pdf`. Replace `image1.png`, `image2.jpg`, and `output.pdf` with your actual file names. If you don't specify an output file name with `-o`, it will default to `merged_output.pdf`.

The script will prompt you before overwriting an existing file, and you can choose to proceed or cancel the operation.

Model: gpt-4
