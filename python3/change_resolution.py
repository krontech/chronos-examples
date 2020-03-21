#!/usr/bin/python3

import requests

post = requests.post('http://192.168.12.1/control/p', json = {'resolution': {'hRes': 640, 'vRes': 480, 'bitDepth': 12}})
