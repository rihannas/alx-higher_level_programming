#!/usr/bin/python3
"""a Python script that takes 2 arguments
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
"""
import sys
import requests


if __name__ == "__main__":

    response = requests.get('https://api.github.com/user',
                            auth=(sys.argv[1], sys.argv[2]))
    if response.status_code >= 400:
        print('None')
    else:
        print(response.json().get('id'))
