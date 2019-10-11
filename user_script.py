from flask import Flask, request
import sys
import requests
import json
import pyplot

if len(sys.argv) <= 1: exit("Please provide words to look for.")

server_url = 'http://localhost:5000'

words = sys.argv[1:]
query = '?words=' + ','.join(words)
result = requests.get(server_url + query).json()
print(result)
