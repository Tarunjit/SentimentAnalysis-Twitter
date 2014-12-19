__author__ = 'Tarun'

from TwitterAPI import TwitterAPI


SEARCH_TERM = 'pizza'


ACCESS_TOKEN_KEY = "91070076-hXHCPWZNQiJ1LwwUFZLzjGJXMZLwoJkbZLKVCi6jx"
ACCESS_TOKEN_SECRET = "V0zScYzfuKBTl0VWWHpG84Y34gNGkIN80PDs5eQsnEdgO"
CONSUMER_KEY = "vVypmaitmk21exXEo22Bi691H"
CONSUMER_SECRET = "9wWmNH6UgDafRuZKTZ02G7arEf9YsJfH2oYanaE6itk0FyMFKA"


api = TwitterAPI(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET)

r = api.request('search/tweets', {'q': SEARCH_TERM})

for item in r:
    print(item['text'] if 'text' in item else item)

print('\nQUOTA: %s' % r.get_rest_quota())
