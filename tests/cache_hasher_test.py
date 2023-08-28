import unittest
from unittest.mock import Mock
from core.redis_config import redis_client
from img_fucker.utils.cache_helpers import get_md5_hash, get_cached_result

class TestYourFunctions(unittest.TestCase):
    def test_get_md5_hash(self):
        content = b"test_content"
        expected_hash = "5a105e8b9d40e1329780d62ea2265d8a"
        self.assertEqual(get_md5_hash(content), expected_hash)

    def test_get_cached_result(self):
        content = b"test_content"
        expected_data = {"data": "cached_data", "source": "cache"}
        mock_redis_client = Mock()
        mock_redis_client.get.return_value = json.dumps(expected_data).encode("utf-8")
        with unittest.mock.patch("redis_config.redis_client", mock_redis_client):
            result = get_cached_result(content)
            self.assertEqual(result, expected_data)

        mock_redis_client.get.return_value = None
        with unittest.mock.patch("redis_config.redis_client", mock_redis_client):
            result = get_cached_result(content)
            self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
