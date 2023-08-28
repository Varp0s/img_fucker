import hashlib
from typing import Optional
from core.redis_config import redis_client
import json

def get_md5_hash(content: bytes) -> str:
    """
    Calculate the MD5 hash of the given content.

    Args:
        content (bytes): The content to calculate the hash for.

    Returns:
        str: The MD5 hash in hexadecimal format.
    """
    return hashlib.md5(content).hexdigest()

def get_cached_result(content: bytes) -> Optional[dict]:
    """
    Retrieve cached result from Redis based on content hash.

    This function takes binary content, calculates its MD5 hash, and checks if
    the hash exists in the Redis cache. If the hash exists, the cached JSON data
    is retrieved and returned as a dictionary. If not found, returns None.

    Args:
        content (bytes): The content to look for in the cache.

    Returns:
        Optional[dict]: Cached data as a dictionary if found, otherwise None.
    """
    content_hash = get_md5_hash(content)
    cached = redis_client.get(content_hash)
    if cached:
        cached_data = json.loads(cached.decode("utf-8"))
        cached_data["source"] = "cache"  
        return cached_data
    return None

