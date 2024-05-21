#!/usr/bin/python3
"""
Piece of code that retrieves the total number of users on a given Reddit subreddit.
"""

import requests

def get_subscriber_count(community):
"""Obtain the total number of users on a given subreddit."""
url = "https://www.reddit.com/r/{}/about.json".format(community)
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers, allow_redirects=False)
if response.status_code == 200:
data = response.json()
subscriber_count = data['data']['subscribers']
return subscriber_count
else:
return 0
