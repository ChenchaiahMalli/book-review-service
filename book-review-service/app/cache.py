import json
from typing import Optional
import redis
from app.config import settings

class Cache:
    def __init__(self):
        try:
            self.redis = redis.Redis.from_url(settings.redis_url)
            self.redis.ping()  # Test connection
            self.available = True
        except redis.ConnectionError:
            self.available = False

    def get(self, key: str) -> Optional[dict]:
        if not self.available:
            return None
        cached_data = self.redis.get(key)
        if cached_data:
            return json.loads(cached_data)
        return None

    def set(self, key: str, value: dict, expire: int = None) -> bool:
        if not self.available:
            return False
        if expire is None:
            expire = settings.cache_expiration
        self.redis.setex(key, expire, json.dumps(value))
        return True

cache = Cache()