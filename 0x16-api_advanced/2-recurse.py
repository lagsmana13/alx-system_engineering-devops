#!/usr/bin/python3
"""
Program to fetch a collection of all trending threads in a specified Reddit community.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively collects a collection of titles of all trending posts
    in a specified subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): Collection to accumulate the post titles.
                                    Default is an empty collection.
        after (str, optional): Token utilized for pagination.
                                Default is an empty token.
        count (int, optional): Current tally of retrieved posts. Default is 0.

    Returns:
        list: A collection of post titles from the trending section of the subreddit.
    """
    # Build the URL for the community's trending posts in JSON structure
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Set headers for the HTTP query, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Set parameters for the query, including pagination and limit
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Make a GET query to the community's trending posts endpoint
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Verify if the query status code signals a missing resource error (404)
    if response.status_code == 404:
        return None
    # Decode the JSON query result and obtain relevant data
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    # Add post titles to the hot_list
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    # If there are more posts to fetch, recursively call the function
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # Return the completed collection of trending post titles
    return hot_list
