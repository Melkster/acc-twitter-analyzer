import numpy as np
import sys
import requests
import matplotlib.pyplot as plot

if len(sys.argv) <= 1:
    exit("Please provide words to look for.")

server_url = 'http://130.238.28.43:5000'

words = sys.argv[1:]
query = '?words=' + ','.join(words)
result = requests.get(server_url + query).json()

# Plot the data:
height = list(map(lambda w: result[w + '_count'], words))
y_pos = np.arange(len(words))
plot.bar(y_pos, height)  # Create bars
plot.ylabel('Word frequency')  # Y-label
plot.suptitle('Total number of parsed tweets: ' + str(result['tweet_count']), fontsize=14)
plot.xticks(y_pos, words)  # Create names on the x-axis
plot.show()  # Show graphic
