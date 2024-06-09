import os
import pytest
from PIL import Image
from image_to_pdf_combiner import convert_images_to_pdf, get_output_filename

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

    from image_to_pdf_combiner import main
    import sys
    sys.argv = ["image_to_pdf_combiner.py"] + sample_images + ["-o", str(output_file)]
    main()

    # Ensure the original file is unchanged
    assert os.path.exists(output_file)

# Replace 'your_script' with the actual name of your script when using it.
