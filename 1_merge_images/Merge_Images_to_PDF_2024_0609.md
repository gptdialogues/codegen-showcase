---
title: Merge Images to PDF
create_time: 2024-06-09 18:59:33
update_time: 2024-06-09 18:59:58
conversation_id: a879c623-a9a3-4a47-b067-78028cf8d06b
---

# Merge Images to PDF

Creation Time: 2024-06-09 18:59:33

Update Time: 2024-06-09 18:59:58

## Assistant



## User

Please generate python3 code to merge images to a single PDF file. I would like to add some additional specifications below.
- Add a help option using `argparse`.
- Add docstrings and type hints.
- Add an option to specify the output filename. Use a default name by adding a specific suffix after the original basename.
- Give some candidates for the file name of the script.
- Ask "(y)es/(n)o" before overwriting an existing file (default: no). 
- Add the following shebang and an encoding declaration.
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```
Also, please generate a test code for each function of the generated code using pytest.

## Assistant (gpt-4o)

Certainly! Here is the Python script with the specified requirements:

```python
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
```

### Candidate File Names for the Script
- `image_to_pdf.py`
- `merge_images.py`
- `images_to_pdf_converter.py`
- `pdf_creator_from_images.py`

### Test Code for Each Function Using Pytest
```python
import pytest
import os
from unittest import mock
from PIL import Image
import tempfile
from script_name import merge_images_to_pdf, confirm_overwrite, get_default_output_filename

@pytest.fixture
def temp_images():
    images = []
    for i in range(3):
        img = Image.new('RGB', (100, 100), color=(i * 40, i * 40, i * 40))
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        img.save(tmp_file.name)
        images.append(tmp_file.name)
    yield images
    for image in images:
        os.remove(image)

def test_merge_images_to_pdf(temp_images):
    output_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    merge_images_to_pdf(temp_images, output_file)
    assert os.path.exists(output_file)
    os.remove(output_file)

def test_confirm_overwrite_yes(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
        assert confirm_overwrite(tmp_file.name) is True

def test_confirm_overwrite_no(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
        assert confirm_overwrite(tmp_file.name) is False

def test_get_default_output_filename(temp_images):
    default_filename = get_default_output_filename(temp_images)
    expected_suffix = "_merged.pdf"
    assert default_filename.endswith(expected_suffix)
    base_name = os.path.splitext(os.path.basename(temp_images[0]))[0]
    assert default_filename == f"{base_name}{expected_suffix}"

def test_get_default_output_filename_single_image():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        image_files = [tmp_file.name]
        default_filename = get_default_output_filename(image_files)
        expected_suffix = "_merged.pdf"
        base_name = os.path.splitext(os.path.basename(tmp_file.name))[0]
        assert default_filename == f"{base_name}{expected_suffix}"

if __name__ == "__main__":
    pytest.main()
```

**Note**: Replace `script_name` with the actual name of your script file without the `.py` extension. 

These pieces of code should fulfill all the requirements you specified, including the additional options, docstrings, type hints, and test coverage with pytest.

