#!/usr/bin/python3

import requests

# Save a region 500 frames long, starting at frame 300.
post = requests.post('http://192.168.12.1/control/startFilesave', json = {'format': 'h264', 'device': 'sda1', 'start': 300, 'length': 500})
if post.reason != "OK" :
	print("Could not save recording. Is a storage device inserted?")

