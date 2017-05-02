import redis

r = redis.StrictRedis(host='localhost', port=6379, password='', db=0,  charset="utf-8", decode_responses=True)

for key in r.scan_iter():
    # do something with the key
    if r.type(key) == 'string' :
        print(str(key) +' : ' + str(r.get(key)))
    else :
        print(str(key) + ' : ' + str(r.hgetall(key)))

    #r.delete(key)

r.set('counter', 1)

