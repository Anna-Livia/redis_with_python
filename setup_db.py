import redis
import os
r = redis.from_url(os.environ['REDIS_URL'], charset="utf-8", decode_responses=True)

for key in r.scan_iter():
    # do something with the key
    if r.type(key) == 'string' :
        print(str(key) +' : ' + str(r.get(key)))
    else :
        print(str(key) + ' : ' + str(r.hgetall(key)))

    r.delete(key)

r.set('counter', 1)
r.set('user', [])

