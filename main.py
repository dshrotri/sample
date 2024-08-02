from flask import Flask
from openai import OpenAI
import os


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, world!"

if __name__ == '__main__':
    print("hello world")
    