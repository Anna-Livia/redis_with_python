import redis
import os
import re
import datetime



r = redis.from_url(os.environ['REDIS_URL'], charset="utf-8", decode_responses=True)


def get_all_keys():
    all_keys = []
    for key in r.scan_iter():
        all_keys.append(key)
    return all_keys

# print("#### GET ALL KEYS OUTPUT #####")
# print(get_all_keys())


def get_all_tweets():
    return r.zrange('messages', 0, -1)

# print("#### GET ALL TWEETS OUTPUT #####")
# print(get_all_tweets())

def get_tweet(mid):
    return r.hgetall(mid)

# print("#### GET mid:2 TWEET #####")
# print(get_tweet('mid:2'))


def print_tweets(list_of_tweets):
    for i in list_of_tweets :
        tweet = r.hgetall(i)
        print(tweet['datetime'] + " - " + tweet['name'] + ": " + tweet['message'])

# print("#### PRINT  mid:2 TWEET #####")
# print_tweets(['mid:2'])
#
# print("#### GET ALL TWEETS PRINT #####")
#
# print_tweets(get_all_tweets())


def get_tweet_for_one_user(user_name) :
    user_tweet_ids = []
    for i in get_all_tweets() :
        if r.hget(i, 'name') == user_name :
            user_tweet_ids.append(i)
    return user_tweet_ids

# print("#### get_tweet_for_one_user(user_name) #####")
# print(get_tweet_for_one_user('@vanessa'))
# print(print_tweets(get_tweet_for_one_user('@vanessa')))
# print(get_tweet_for_one_user('@anna-livia'))

#####REDIS
# string r.get
# hash - r.hget, r.hgetall
# set - r.smembers
# sorted set
# list


def name_check(user_name):
    if type(user_name) != str or len(user_name)<1 :
        return False
    first_charac = user_name[0]
    handle = user_name[1:]
    if first_charac != '@' :
        return False
    if bool(re.search(' ', handle, re.IGNORECASE)) :
        return False
    if bool(re.search('[^a-zA-Z0-9-_áàâäãåçéèêëíìîïñóòôöõúùûüýÿæœÁÀÂÄÃÅÇÉÈÊËÍÌÎÏÑÓÒÔÖÕÚÙÛÜÝŸÆŒ]', handle, re.IGNORECASE)):
        return False
    return True


def get_user_names():
    return r.hkeys('users')


def create_tweet(name, message):

    r.incr('counter')
    message_counter = r.get('counter')
    message_id = 'mid:' + str(message_counter)
    r.zadd("messages", message_id, message_counter)
    d = datetime.datetime.now()

    r.hset(message_id, 'name', name)
    r.hset(message_id, 'message', message)
    r.hset(message_id, 'datetime', d)

    try :
        r.bgsave()
    except ResponseError:
        pass

#print(get_user_names())

def delete_empty_message() :
    for i in get_all_tweets() :
        if r.hexists(i, 'datetime') == False :
            print(i)
            print(r.hgetall(i))
            r.delete(i)


def check_user_password(a,b) :
    if r.hget("users", a) == b :
        return True
    else:
        return False