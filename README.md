# Tweet it like REDIS

This is a tweeter like project in python that uses a redis db

## Installation
- Install Redis (`brew install redis)
- run `redis-server`
- run `python setup_db.py`

Check your install with `nosetests test_redisWithPython.py `

## Run the app locally 
- run `python redisWithPython.py` to access the cli

## To-do
- remote setup (on heroku)
- password hashing 
- secure redis setup
- set the redis URL as environment variable and  change it in the files
- rename project properly