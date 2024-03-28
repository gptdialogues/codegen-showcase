# codegen-showcase

A repository showcasing how to use ChatGPT to generate Python 3 code for various purposes.

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

## How to Use

To use these scripts, clone this repository and navigate to the directory containing the script you want to use. Make sure you have the required dependencies installed, and then run the script with the appropriate arguments.