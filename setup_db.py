import redis
import os

REDIS_URL = 'http://localhost:6379'

r = redis.from_url(REDIS_URL, charset="utf-8", decode_responses=True)

for key in r.scan_iter():
    print(key)
    r.delete(key)

r.set('counter', 1)
r.hset("users", "@admin", 'admin')


