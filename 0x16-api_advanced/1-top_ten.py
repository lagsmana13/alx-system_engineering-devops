#!/usr/bin/python3
"""
Program to display hot threads from a specified Reddit community.
"""

import requests


def top_ten(subreddit):
    """Show the headings of the 10 most popular threads in a specified community."""
    # Create the link for the community's hot threads in JSON structure
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Set up details for the HTTP query, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Set up parameters for the query, capping the number of threads to 10
    params = {
        "limit": 10
    }

    # Make a GET query to the community's hot threads endpoint
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Verify if the query status code signals a missing resource error (404)
    if response.status_code == 404:
        print("None")
        return

    # Decode the JSON query result and get the 'data' portion
    results = response.json().get("data")

    # Display the headings of the leading 10 hottest threads
    [print(c.get("data").get("title")) for c in results.get("children")]
