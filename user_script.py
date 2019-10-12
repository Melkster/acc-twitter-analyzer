from flask import Flask, request
import sys
import requests
import json
import matplotlib.pyplot as plt


if len(sys.argv) <= 1: exit("Please provide words to look for.")

server_url = 'http://localhost:5000'

words = sys.argv[1:]
query = '?words=' + ','.join(words)
result = requests.get(server_url + query).json()
print(result)

import numpy as np

x = np.arange(0, 5, 0.1);
y = np.sin(x)

plt.plot(10, 5)
