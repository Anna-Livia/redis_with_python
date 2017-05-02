import redis
import os
import datetime

r = redis.from_url(os.environ['REDIS_URL'], charset="utf-8", decode_responses=True)


def create_tweet() :
    input_name = input("Enter your name: ")

    input_message = input("Enter your message: ")

    counter_user = r.get('counter')
    print("Counter is : " + counter_user)
    r.incr('counter')

    message_id = 'mid:' + str(counter_user)
    d = datetime.datetime.now()
    print("message id is : " + message_id)
    r.hset(message_id, 'name', input_name)
    r.hset(message_id, 'message', input_message)
    r.hset(message_id, 'datetime', str(d))
    r.bgsave()

    print(r.hgetall(message_id))


def get_all_tweet() :
    for key in r.scan_iter():
        # do something with the key
        if r.type(key) == 'string':
            pass
        else:
            print(str(r.hget(key, 'name')) + ' : ' + str(r.hgetall(key)))



def get_user(user_name):
    found = False

    for key in r.scan_iter():

        if r.type(key) == 'hash' and r.hget(key, 'name') == user_name :
            print(r.hget(key, 'datetime') + ' : ' + r.hget(key, 'message'))
            found = True

    if not found:
        print("user does not exist")

while True :
    interface = input("to create, enter c to read, enter r or enter user name, q to quit  ")
    if interface == 'c':
        create_tweet()
    elif interface == 'r':
        get_all_tweet()
    elif interface == 'q' :
        break
    else:
        get_user(interface)