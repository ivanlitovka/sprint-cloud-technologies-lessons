import json
from typing import Dict
import redis


class RedisClient:
    def __init__(self, host: str, port: int, password: str, cert_path: str) -> None:
        # Инициализируем клиент Redis/Valkey с SSL-подключением
        self._client = redis.StrictRedis(
            host=host,
            port=port,
            password=password,
            ssl=True,
            ssl_ca_certs=cert_path
        )

    def set(self, k: str, v: Dict) -> None:
        # Сериализуем словарь в JSON-строку и сохраняем по ключу k
        # ensure_ascii=False — чтобы кириллица сохранялась в читаемом виде
        self._client.set(k, json.dumps(v, ensure_ascii=False))

    def get(self, k: str) -> Dict:
        # Получаем значение по ключу
        result = self._client.get(k)
        if not result:
            return {}
        # Декодируем байты в строку и парсим JSON обратно в словарь
        return json.loads(result.decode("utf-8"))