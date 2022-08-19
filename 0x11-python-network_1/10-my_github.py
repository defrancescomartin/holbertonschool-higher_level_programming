#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 3:
        url = 'https://api.github.com/user'
        username = argv[1]
        password = argv[2]
        r = requests.get(url, auth=(username, password))
        try:
            req = r.json()
            print(req.get('id'))
        except:
            print("Not a valid JSON")
    else:
        print("Usage: {} <username> <password>".format(argv[0]))
