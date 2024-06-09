# Rotate Image Python Script

Creation Time: 2024-03-28 13:43:19.052322

## System

Time: Invalid or missing timestamp



## System

Time: Invalid or missing timestamp



## User

Time: 2024-03-28 13:43:19.053294

Please give me a python3 code to rotate a png/jpg image by 90 degrees. I would like to add some additional specifications below.
- Add a help option using argparse.
- Add an option to specify the output filename. Use a default name by adding a specific suffix after the original basename.
- Give some candidates for the file name of the script.
- Ask "(y)es/(n)o" before overwriting an existing file (default: no). 
- Add the following shebang and an encoding declaration.
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

## Assistant

Time: 2024-03-28 13:43:57.619721

Model: gpt-4

## Assistant

Time: 2024-03-28 13:43:57.619929

Here's a Python script that meets your requirements. The script uses the `PIL` library for image manipulation, so make sure you have it installed (`pip install Pillow` if you don't).

```python
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
```

Here are some candidates for the file name of the script:
- `rotate_image.py`
- `image_rotator.py`
- `rotate_picture.py`
- `picture_rotator.py`

To use the script, save it with one of the suggested filenames and run it from the command line. For example:
```sh
python rotate_image.py input_image.png --output rotated_image.png
```

This script includes the shebang and encoding declaration as requested, and it uses `argparse` for handling command-line arguments, including a help option. The output filename can be specified with the `-o` or `--output` flag, and it will prompt for confirmation before overwriting an existing file.

Model: gpt-4