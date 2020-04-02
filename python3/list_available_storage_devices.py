#!/usr/bin/python3

import requests

post = requests.get('http://192.168.12.1/control/p/externalStorage')
print(post.json())

