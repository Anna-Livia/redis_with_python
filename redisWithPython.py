import redis
import os
import datetime

r = redis.from_url(os.environ['REDIS_URL'], charset="utf-8", decode_responses=True)


def create_tweet(name):
    input_message = input("Enter your message: ")

    r.incr('counter')
    counter_user = r.get('counter')
    message_id = 'mid:' + str(counter_user)

    d = datetime.datetime.now()

    r.hset(message_id, 'name', name)
    r.hset(message_id, 'message', input_message)
    r.hset(message_id, 'datetime', str(d))
    try :
        r.bgsave()
    except ResponseError :
        pass


def get_all_tweet() :
    for key in r.scan_iter():
        # do something with the key
        if r.type(key) == 'string':
            pass
        else:
            print(str(r.hget(key, 'datetime')) + "-" + str(r.hget(key, 'name')) + ' : ' + str(r.hget(key, 'message')))


def get_user(user_name):
    found = False

    for key in r.scan_iter():

        if r.type(key) == 'hash' and r.hget(key, 'name') == user_name:
            found = True
            print(r.hget(key, 'datetime') + ' : ' + r.hget(key, 'message'))


    if not found:
        print("user does not exist")


name = input("What is your name ?")

while True:
    interface = input("to create, enter c to read, enter r or enter user name, q to quit  ")
    if interface == 'c':
        create_tweet(name)
    elif interface == 'r':
        get_all_tweet()
    elif interface == 'q':
        break
    else:
        get_user(interface)

