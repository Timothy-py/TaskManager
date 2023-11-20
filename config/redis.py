import os
import redis
from config.config import env_vars


def get_redis_client():
    return redis.Redis(host=env_vars.REDIS_HOST, port=env_vars.REDIS_PORT, db=0)

redis_cache = get_redis_client()