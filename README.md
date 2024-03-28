# codegen-showcase

A repository showcasing how to use ChatGPT to generate Python 3 code for various purposes.

## Adding a Help Option

One useful feature that ChatGPT can add to scripts is a help option. This option allows users to view a description of the script's functionality and usage instructions directly from the command line. To add a help option, ChatGPT typically uses the `argparse` module in Python, which provides a way to parse command-line options and arguments.

By including a help option, users can quickly understand what the script does and how to use it without needing to read through the source code or external documentation. This makes the script more user-friendly and accessible.

To access the help information for a script, you can typically use the `-h` or `--help` flag when running the script. For example:

```bash
python script_name.py --help
```

This will display the help message, including a brief description of the script and the available options.

## Scripts

### 1. Remove Empty Directories Script

- **File:** [00_Remove_empty_dirs_script_2024_0327.md](00_Remove_empty_dirs_script_2024_0327.md)
- **Description:** This script recursively finds and removes empty directories in a specified path. It includes options for specifying the output filename, running in silent mode, and displaying help.
- **Usage:**
  ```bash
  python 01_clean_empty_folders.py --path <path-to-search> --output <output-file> --silent
  ```

### 2. Merge PNG/JPG to PDF

- **File:** [10_Merge_PNG_JPG_to_PDF_2024_0327.md](10_Merge_PNG_JPG_to_PDF_2024_0327.md)
- **Description:** This script merges PNG/JPG image files into a single PDF file while preserving their original dimensions. It includes options for specifying the output filename and confirming before overwriting an existing file.
- **Usage:**
  ```bash
  python 11_merge_to_pdf.py image1.png image2.jpg -o output.pdf
  ```

### 3. Rotate Image Python Script

- **File:** [20_Rotate_Image_Python_Script_2024_0328.md](20_Rotate_Image_Python_Script_2024_0328.md)
- **Description:** This script rotates a PNG/JPG image by 90 degrees. It includes options for specifying the output filename, adding a help option, and confirming before overwriting an existing file.
- **Usage:**
  ```bash
  python 21_rotate_image.py input_image.png --output rotated_image.png
  ```

## How to Use

To use these scripts, clone this repository and navigate to the directory containing the script you want to use. Make sure you have the required dependencies installed, and then run the script with the appropriate arguments.
