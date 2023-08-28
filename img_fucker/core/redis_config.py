import redis
from config import settings

redis_client = redis.StrictRedis(host=settings.redis_host, port=settings.redis_port, db=0)
