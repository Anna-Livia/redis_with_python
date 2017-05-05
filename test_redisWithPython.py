import hashes
import redis
import os
import datetime


r = redis.from_url(os.environ['REDIS_URL'], charset="utf-8", decode_responses=True)


def test_get_all_keys():
    assert len(hashes.get_all_keys()) == len(r.keys()), "C'est en fait " + str(len(hashes.get_all_keys()))


def test_get_all_tweets():
    assert len(hashes.get_all_tweets()) == len(r.zrange('messages', 0, -1))

def test_get_tweet():
    assert hashes.get_tweet('mid:2') == r.hgetall('mid:2')


def test_name_check_is_ok():
    assert hashes.name_check('@vanessa') == True, hashes.name_check('@vanessa')

def test_name_check_with_spec_charac_is_ok():
    assert hashes.name_check('@anna-livia') == True

def test_name_check_with_accent_charac_is_ok():
    assert hashes.name_check('@Étienne') == True

def test_name_check_WO_arobase_is_NOK():
    assert hashes.name_check('vanessa') == False

def test_name_check_with_blank_space_is_NOK():
    assert hashes.name_check("@vanessa is here") == False

def test_name_check_with_weird_charac_is_NOK():
    assert hashes.name_check("@vanessa%is/here") == False

def test_name_check_with_no_charac_is_NOK():
    assert hashes.name_check("") == False

# def test_set_user_password():
#     set_user_password()
#     assert

def test_check_user_password_al_admin_OK():
    assert hashes.check_user_password("@anna-livia", "admin") == True

def test_check_user_password_al_admin_NOK():
    assert hashes.check_user_password("@anna-livia", "pas_admin") == False
