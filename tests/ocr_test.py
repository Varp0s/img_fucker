import unittest
from unittest.mock import MagicMock
from img_fucker.core.ocr import extract_data, batch_process_images

class TestImageProcessing(unittest.TestCase):

    def test_extract_data(self):
        mock_pil_image = MagicMock()
        mock_pil_image_to_string = MagicMock(return_value="Extracted Text")
        Image.open = MagicMock(return_value=mock_pil_image)
        pytesseract.image_to_string = mock_pil_image_to_string

        extracted_text = extract_data(b"fake_image_content")
        self.assertEqual(extracted_text, "Extracted Text")

    def test_batch_process_images(self):
        mock_extract_data = MagicMock(return_value="Extracted Text")
        extract_data = mock_extract_data

        image_contents = [b"image1", b"image2", b"image3"]
        extracted_texts = batch_process_images(image_contents)
        
        expected_texts = ["Extracted Text", "Extracted Text", "Extracted Text"]
        self.assertEqual(extracted_texts, expected_texts)

if __name__ == "__main__":
    unittest.main()
