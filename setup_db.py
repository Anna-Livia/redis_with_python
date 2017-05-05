import redis
import os
r = redis.from_url(os.environ['REDIS_URL'], charset="utf-8", decode_responses=True)

for key in r.scan_iter():
    print(key)
    r.delete(key)

r.set('counter', 1)
r.hset("users", "@admin", 'admin')


