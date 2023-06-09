from pydantic import BaseSettings
from typing import Set
from functools import lru_cache


class Settings(BaseSettings):

    SECRET_KEY: str = ""
    ALGORITHM: str = ""

    AUTH_MODE: str = "static"  # db, cache, static
    AUTH_CACHE_TIMEOUT_MINUTES: int = 5
    AUTH_TOKEN_EXPIRE_MINUTES: int = 30

    CACHE_HOST: str = "127.0.0.1"
    CACHE_PORT: int = 6379
    CACHE_USERNAME: str = ""
    CACHE_PASSWORD: str = ""
    CACHE_DB: int = 1
    CACHE_TIMEOUT: int = 300

    DATABASE_DEBUG: bool = False
    DATABASE_URL: str = "mysql+mysqldb://root@localhost/fastapi-vuejs"

    DEFAULT_LANGUAGE: str = "pt"
    SUPPORTED_LANGUAGE: Set[str] = set(['pt', 'en'])

    class Config:
        env_file = ".env"

    @property
    def languages(self):
        return list(set([self.DEFAULT_LANGUAGE]) | self.SUPPORTED_LANGUAGE)

    @property
    def caches(self):
        return {
            'default': {
                'host': self.CACHE_HOST,
                'port': self.CACHE_PORT,
                'username': self.CACHE_USERNAME,
                'password': self.CACHE_PASSWORD,
                'db': self.CACHE_DB
            }
        }

    @property
    def databases(self):
        return {
            'default': {'url': self.DATABASE_URL},
        }


@lru_cache()
def get_settings():
    return Settings()
