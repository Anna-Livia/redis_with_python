import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

def create_tweet() :
    input_name = input("Enter your name: ")
    input_age = int(input("Enter your age: "))
    input_message = input("Enter your message: ")

    counter_user = r.get('counter')
    print ("Counter is : " + counter_user)
    r.incr('counter')

    user_ID = 'user:' + str(counter_user)

    print("user id is : " + user_ID)
    r.hset(user_ID, 'name', input_name)
    r.hset(user_ID, 'age', input_age)
    r.hset(user_ID, 'message', input_message)
    r.bgsave()

    print(r.hgetall(user_ID))

def get_all_tweet() :
    for key in r.scan_iter():
        # do something with the key
        if r.type(key) == 'string':
            print(str(key) + ' : ' + str(r.get(key)))
        else:
            print(str(key) + ' : ' + str(r.hgetall(key)))


interface = input("to create, enter c to read, enter r ")
if interface == 'c' :
    create_tweet()
else:
    get_all_tweet()