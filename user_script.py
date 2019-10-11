from flask import Flask, request
import sys

words = ""
word_list = [w.strip() for w in words.split(",")] # Create list from query and strip whitespace
