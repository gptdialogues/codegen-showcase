---
title: PDF 画像結合 Python。
create_time: 2024-06-10 07:34:52
update_time: 2024-06-10 07:35:14
conversation_id: c24ac1f3-9096-403d-9ac7-1ef939e397c8
---

# PDF 画像結合 Python。

Creation Time: 2024-06-10 07:34:52

Update Time: 2024-06-10 07:35:14

## Assistant



## User

複数の画像ファイルを1つのPDFファイルに結合するpython3コードを生成してください。以下にいくつかの仕様を追加します。
- 引数として1つまたは複数の画像ファイルをフラグなしで受け取る
- argparseを使ったヘルプオプションを追加
- docstringsとtype hintsを追加
- 出力ファイル名を指定するオプションを追加。元のベースネームの後に特定のサフィックスを追加してデフォルト名を使用。
- スクリプトのファイル名の候補をいくつかあげる。
- 既存のファイルを上書きする前に"(y)es/(n)o "と尋ねる（デフォルト：no）。
- 以下のshebangとエンコーディング宣言を追加する。
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-.
```
また、生成したコードの各関数のテストコードを pytest を使って生成してください。

## Assistant (gpt-4o)

こちらにご希望のPythonスクリプトとそのテストコードを記載します。

### 画像ファイルをPDFに結合するPythonスクリプト

```python
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
```

### テストコード (pytest)

```python
import os
import pytest
from PIL import Image
from your_script import convert_images_to_pdf, get_output_filename

@pytest.fixture
def sample_images(tmp_path):
    image1 = tmp_path / "image1.jpg"
    image2 = tmp_path / "image2.jpg"
    Image.new('RGB', (100, 100), color='red').save(image1)
    Image.new('RGB', (100, 100), color='blue').save(image2)
    return [str(image1), str(image2)]

def test_get_output_filename():
    assert get_output_filename("test_image.jpg") == "test_image_combined.pdf"
    assert get_output_filename("test_image.jpg", "_output") == "test_image_output.pdf"
    assert get_output_filename("test_image.jpg", "_output", ".txt") == "test_image_output.txt"

def test_convert_images_to_pdf(sample_images, tmp_path):
    output_file = tmp_path / "output.pdf"
    convert_images_to_pdf(sample_images, str(output_file))
    assert os.path.exists(output_file)

    # Check if the PDF file is not empty
    assert os.path.getsize(output_file) > 0

def test_main_overwrite_prompt(monkeypatch, tmp_path, sample_images):
    output_file = tmp_path / "output.pdf"
    convert_images_to_pdf(sample_images, str(output_file))

    def mock_input(prompt):
        return "n"
    monkeypatch.setattr('builtins.input', mock_input)

    from your_script import main
    import sys
    sys.argv = ["your_script.py"] + sample_images + ["-o", str(output_file)]
    main()

    # Ensure the original file is unchanged
    assert os.path.exists(output_file)

# Replace 'your_script' with the actual name of your script when using it.
```

### スクリプトファイル名の候補
1. `image_to_pdf_combiner.py`
2. `img2pdf.py`
3. `pdf_creator.py`

これで、画像をPDFに結合するPythonスクリプトとそのテストコードが完成しました。お役に立てれば幸いです。

