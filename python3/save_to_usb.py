#!/usr/bin/python3

import requests

post = requests.post('http://192.168.12.1/control/startFilesave', json = {'format': 'h264', 'device': 'sda1', 'start': 300, 'length': 500})
if post.reason != "OK" :
	print("Could not save recording. Is a storage device inserted?")

