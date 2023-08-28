import httpx

def is_valid_url(url: str) -> bool:
    """
    Check if a URL is valid and reachable.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is valid and reachable, False otherwise.
    """
    try:
        response = httpx.head(url)
        return response.status_code == 200
    except httpx.RequestError:
        return False

if __name__ == "__main__":
    
    if is_valid_url(ocr_url):
        print(f"The OCR result URL '{ocr_url}' is valid and reachable.")
    else:
        print(f"The OCR result URL '{ocr_url}' is not valid or not reachable.")
