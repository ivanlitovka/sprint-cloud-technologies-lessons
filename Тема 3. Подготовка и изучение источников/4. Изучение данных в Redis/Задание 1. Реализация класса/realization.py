import json
from typing import Dict
import redis


class RedisClient:
    def __init__(self, host: str, port: int, password: str, cert_path: str) -> None:
        self._client = redis.StrictRedis(
            host=host,
            port=port,
            password=password,
            ssl=True,
            ssl_ca_certs=cert_path
        )

    def set(self, k: str, v: Dict) -> None:
        self._client.set(k, json.dumps(v, ensure_ascii=False))

    def get(self, k: str) -> Dict:
        result = self._client.get(k)
        if not result:
            return {}
        return json.loads(result.decode("utf-8"))