#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, displays it
curl -Is '$1' | grep 'Content-Length' | cut -d ' ' -f 2
