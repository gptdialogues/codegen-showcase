import pytest
import os
from unittest import mock
from PIL import Image
import tempfile
from merge_images import merge_images_to_pdf, confirm_overwrite, get_default_output_filename

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
