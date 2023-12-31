from secrets import secrets
from os import getenv

secrets.load_env_vars()

consumer_key = getenv('consumer_key')
consumer_secret = getenv('consumer_secret')

access_token = getenv('access_token')
access_secret = getenv('access_secret')