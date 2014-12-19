__author__ = 'Tarun'
## Source : https://github.com/geduldig/TwitterAPI
from TwitterAPI import TwitterAPI
import json

from TwitterAPI import TwitterAPI

ACCESS_TOKEN_KEY = "91070076-hXHCPWZNQiJ1LwwUFZLzjGJXMZLwoJkbZLKVCi6jx"
ACCESS_TOKEN_SECRET = "V0zScYzfuKBTl0VWWHpG84Y34gNGkIN80PDs5eQsnEdgO"
CONSUMER_KEY = "vVypmaitmk21exXEo22Bi691H"
CONSUMER_SECRET = "9wWmNH6UgDafRuZKTZ02G7arEf9YsJfH2oYanaE6itk0FyMFKA"

# If you are behind a firewall you may need to provide proxy server
# authentication.
proxy_url = None  # Example: 'https://USERNAME:PASSWORD@PROXYSERVER:PORT'

# Using OAuth 1.0 to authenticate you have access all Twitter endpoints.
# Using OAuth 2.0 to authenticate you lose access to user specific endpoints (ex. statuses/update),
# but you get higher rate limits.
api = TwitterAPI(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET,
    auth_type='oAuth1',
    proxy_url=proxy_url)
#api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, auth_type='oAuth2', proxy_url=proxy_url)


r = api.request('application/rate_limit_status')


# Print HTTP status code (=200 when no errors).
print(r.status_code)

# Print the raw response.
print(r.text)

# Parse the JSON response.
j = r.response.json()
print(j['resources']['search'])

