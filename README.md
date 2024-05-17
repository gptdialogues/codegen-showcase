# codegen-showcase

A repository showcasing how to use ChatGPT to generate Python 3 code for various purposes.

## Snippets

Below is a snippet I frequently use when instructing ChatGPT to write Python 3 code:

~~~
I would like to add some additional specifications below.
- Add a help option using argparse.
- Add an option to specify the output filename. Use a default name by adding a specific suffix after the original basename.
- Give some candidates for the file name of the script.
- Ask "(y)es/(n)o" before overwriting an existing file (default: no). 
- Add the following shebang and an encoding declaration.
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```
~~~

## Adding a Help Option

One useful feature that ChatGPT can add to scripts is a help option. This option allows users to view a description of the script's functionality and usage instructions directly from the command line. To add a help option, ChatGPT typically uses the `argparse` module in Python, which provides a way to parse command-line options and arguments.

By including a help option, users can quickly understand what the script does and how to use it without needing to read through the source code or external documentation. This makes the script more user-friendly and accessible.

To access the help information for a script, you can typically use the `-h` or `--help` flag when running the script. For example:

```bash
python script_name.py --help
```

This will display the help message, including a brief description of the script and the available options.

## Additional Specifications for Scripts

The following are some additional specifications that can be included in Python scripts to enhance their functionality:

- **Output Filename Specification:** An option can be added to specify the output filename. If not specified, a default name can be used by adding a specific suffix after the original basename.

- **Filename Candidates:** When suggesting filenames for the script, some candidates can be provided for the user to choose from.

- **Overwrite Confirmation:** Before overwriting an existing file, the script can ask for confirmation from the user with a "(y)es/(n)o" prompt. By default, the script can be set not to overwrite the file.

- **Shebang and Encoding Declaration:** The following shebang and encoding declaration can be added at the beginning of the script to ensure that it is executed using Python 3 and with UTF-8 encoding:

  ```python
  #!/usr/bin/env python3
  # -*- coding: utf-8 -*-
  ```

By incorporating these specifications, scripts can become more user-friendly, flexible, and safe to use, providing a better experience for users who run them.

## Scripts

### 0. Remove Empty Directories Script

- **File:** [00_Remove_empty_dirs_script_2024_0327.md](00_Remove_empty_dirs_script_2024_0327.md)
- **Description:** This script recursively finds and removes empty directories in a specified path. It includes options for specifying the output filename, running in silent mode, and displaying help.
- **Usage:**
  ```bash
  python 01_clean_empty_folders.py --path <path-to-search> --output <output-file> --silent
  ```

### 1. Merge PNG/JPG to PDF

- **File:** [10_Merge_PNG_JPG_to_PDF_2024_0327.md](10_Merge_PNG_JPG_to_PDF_2024_0327.md)
- **Description:** This script merges PNG/JPG image files into a single PDF file while preserving their original dimensions. It includes options for specifying the output filename and confirming before overwriting an existing file.
- **Usage:**
  ```bash
  python 11_merge_to_pdf.py image1.png image2.jpg -o output.pdf
  ```

### 2. Rotate Image Python Script

- **File:** [20_Rotate_Image_Python_Script_2024_0328.md](20_Rotate_Image_Python_Script_2024_0328.md)
- **Description:** This script rotates a PNG/JPG image by 90 degrees. It includes options for specifying the output filename, adding a help option, and confirming before overwriting an existing file.
- **Usage:**
  ```bash
  python 21_rotate_image.py input_image.png --output rotated_image.png
  ```

### 3. ImageMagick Python Watermark Script

- **File:** [30_ImageMagick_Python_Watermark_Script_2024_0517.md](30_ImageMagick_Python_Watermark_Script_2024_0517.md)
- **Description:** This script adds a transparent watermark to an input image using the ImageMagick command through `subprocess`. It includes options for specifying the word, font size, color, opacity, and output filename. The watermark is placed in the center of the image, with the date information just below it. The script also confirms before overwriting an existing file.
- **Usage:**
  ```bash
  python 31_add_watermark.py input_image.jpg --word "Confidential" --size 120 --color "rgba(0, 0, 0, 0.5)" --output output_image.jpg
  ```

## How to Use

To use these scripts, clone this repository and navigate to the directory containing the script you want to use. Make sure you have the required dependencies installed, and then run the script with the appropriate arguments.
