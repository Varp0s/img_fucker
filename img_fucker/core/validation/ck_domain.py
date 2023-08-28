import httpx
import logging
from config import settings

async def is_server_reachable(url: str) -> bool:
    """
    Check if the server is reachable.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the server is reachable, False otherwise.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.head(url)
            return response.status_code == 200
    except httpx.RequestError:
        return False

async def fetch_dns_lookup_data(domain: str) -> dict:
    api_url = f"https://api.api-ninjas.com/v1/dnslookup?domain={domain}"
    headers = {"X-Api-Key": settings.API_NINJAS}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url, headers=headers)
            response.raise_for_status()
            return response.json()  
        except httpx.HTTPError as e:
            logging.error("Error fetching DNS lookup data: %s", e)
            return None

async def verify_domain(domain: str) -> bool:
    if not await is_server_reachable("https://api.api-ninjas.com"):
        logging.warning("Server is not reachable.")
        return False

    result = await fetch_dns_lookup_data(domain)
    return result is not None


