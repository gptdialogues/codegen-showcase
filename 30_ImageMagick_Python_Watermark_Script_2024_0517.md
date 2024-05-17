---
title: ImageMagick Python Watermark Script
create_time: 2024-05-17 14:20:26
update_time: 2024-05-17 14:21:01
conversation_id: 34220f7a-1399-4b52-a291-e87f4316c204
---

# ImageMagick Python Watermark Script

Creation Time: 2024-05-17 14:20:26

Update Time: 2024-05-17 14:21:01

## Assistant



## Assistant



## User

Please generate a python3 code to put a transparent word (watermark) on an input image using the ImageMagick command through `subprocess`. I would like to add some additional specifications below.
- Add a help option using `argparse`
- Add an option to specify the word (default: "Incorrect Data Used")
- Place the watermark in the center of the image
- Add an option to specify the font size (default: 100)
Add the date information just below the watermark using a smaller font size
- Add an option to specify the color (default: transparent pink) and opacity (default: 0.4)
- Add an option to specify the output filename. Use a default name by adding a specific suffix after the original basename.
- Give some candidates for the file name of the script.
- Ask "(y)es/(n)o" before overwriting an existing file (default: no). 
- Add the following shebang and an encoding declaration.
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

## Assistant (gpt-4o)

Sure, here's the Python script that fulfills your requirements. This script uses the `subprocess` module to call ImageMagick commands and `argparse` to handle command-line arguments. 

```python
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
```

### Explanation of the Script

1. **Shebang and Encoding Declaration**: 
    ```python
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    ```
    These lines specify the script should be run with Python 3 and use UTF-8 encoding.

2. **Imports**:
    ```python
    import argparse
    import subprocess
    import os
    from datetime import datetime
    ```
    We import necessary modules for handling command-line arguments, running subprocesses, checking file existence, and getting the current date.

3. **Argument Parsing**:
    ```python
    parser = argparse.ArgumentParser(description="Add a transparent watermark to an image using ImageMagick")
    parser.add_argument("input_image", help="Path to the input image")
    parser.add_argument("-w", "--word", default="Incorrect Data Used", help="Word to use as the watermark (default: 'Incorrect Data Used')")
    parser.add_argument("-s", "--size", type=int, default=100, help="Font size of the watermark (default: 100)")
    parser.add_argument("-c", "--color", default="rgba(255, 105, 180, 0.4)", help="Color and opacity of the watermark in rgba format (default: 'rgba(255, 105, 180, 0.4)')")
    parser.add_argument("-o", "--output", help="Output filename")
    parser.add_argument("-y", "--yes", action="store_true", help="Overwrite the output file if it exists (default: no)")
    args = parser.parse_args()
    ```
    Here we set up `argparse` to handle command-line arguments and provide default values and help messages.

4. **Handling Output Filename and Overwrite Confirmation**:
    ```python
    if not output_image:
        base, ext = os.path.splitext(input_image)
        output_image = f"{base}_watermarked{ext}"

    if not overwrite and os.path.exists(output_image):
        response = input(f"The file {output_image} already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Operation cancelled.")
            return
    ```
    This block determines the output filename and checks whether to overwrite an existing file based on user input.

5. **Generating Date Text**:
    ```python
    date_text = datetime.now().strftime("%Y-%m-%d")
    ```
    This line gets the current date formatted as "YYYY-MM-DD".

6. **Constructing and Running the ImageMagick Command**:
    ```python
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
    ```
    This section builds the `ImageMagick` command and executes it using `subprocess.run`.

### File Name Suggestions for the Script
- `watermark_image.py`
- `add_watermark.py`
- `image_watermark.py`
- `watermark_tool.py`

You can save this script with any of the suggested names or another name of your choosing.

