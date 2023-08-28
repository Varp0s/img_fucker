import httpx
import asyncio
import re
from config import settings

async def fetch_email_verification(email: str) -> dict:
    """
    Fetch email verification results from the Emailable API.

    This asynchronous function takes an email address as input and fetches the verification
    results from the Emailable API using HTTP GET requests.

    Args:
        email (str): The email address to verify.

    Returns:
        dict: A dictionary containing the JSON response from the Emailable API,
              containing verification results. Returns None if an error occurs.
    """
    api_url = f"https://api.emailable.com/v1/verify"
    params = {"email": email, "api_key": settings.MAIL_VALIDATION}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            print("Error:", e)
            return None

async def is_email_deliverable(verification_result: dict) -> bool:
    """
    Check if an email is deliverable based on verification results.

    This asynchronous function takes the verification results returned by the Emailable API
    and checks if the email's state is 'deliverable'.

    Args:
        verification_result (dict): Verification results returned by the API.

    Returns:
        bool: True if the email is deliverable, False otherwise.
    """
    return verification_result.get('state') == 'deliverable'
