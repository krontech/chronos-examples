#!/usr/bin/python3

import time
import requests

post = requests.post('http://192.168.12.1/control/startRecording')
time.sleep(2)
post = requests.post('http://192.168.12.1/control/stopRecording')

