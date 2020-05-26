#!/usr/bin/python3

import requests

post = requests.get('http://192.168.12.1/cgi-bin/storageInfo?mmcblk1p1')
print(post.json())

