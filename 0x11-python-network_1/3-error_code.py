#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays the body of the response"""

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as r:
            print(r.read().decode("utf-8"))

    except error.HTTPError as e:
        print(f'Error code: {e.code}')
