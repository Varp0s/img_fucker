from PIL import Image
import pytesseract
import io
from typing import List

def extract_data(image_content: bytes) -> str:
    """
    Extract text data from the provided image content using OCR (Optical Character Recognition).

    This function takes binary image content as input, processes it using the pytesseract library
    to perform OCR, and returns the extracted text.

    Args:
        image_content (bytes): The binary content of the image.

    Returns:
        str: Extracted text from the image after OCR processing.
    """
    image = Image.open(io.BytesIO(image_content))
    text = pytesseract.image_to_string(image, lang="eng", config="--psm 6")

    return text.encode("utf-8", "ignore").decode("utf-8")

def batch_process_images(image_contents: List[bytes]) -> List[str]:
    """
    Process a batch of image contents and extract text from each image using OCR.

    This function takes a list of binary image contents, processes each image using the
    `extract_data` function, and returns a list of extracted text for each image.

    Args:
        image_contents (List[bytes]): List of binary image contents.

    Returns:
        List[str]: List of extracted text from each image after OCR processing.
    """
    extracted_texts = []
    for image_content in image_contents:
        extracted_text = extract_data(image_content)
        extracted_texts.append(extracted_text)
    return extracted_texts
