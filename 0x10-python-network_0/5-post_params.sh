#!/bin/bash
#a Bash script that takes in a URL, sends a POST request to the passed URL
curl -s "$1" -X POST -d "test@gmail.com" -d "subject=I will always be here for PLD"