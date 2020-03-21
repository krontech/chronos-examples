# HTTP Control API examples
The python bindings and camera control software for the Chronos High Speed Cameras can be found in the pychronos repository: https://github.com/krontech/pychronos/

The example scripts in this folder run in python 3 on a remote computer and communicate with the camera over the network via the HTTP API. They use the Requests libary for HTTP requests: https://2.python-requests.org/en/master/

The documentation for the HTTP API is hosted on the camera itself. To access it, open a web browser and go to the address http://IP/apidoc/, where IP is the IP address of the camera.

To find the IP address:
If connecting via ethernet: On the camera's touchscreen, enter the Util menu and select the Network tab. The IP address is listed in the Network Status box at the bottom of the screen, on the 2nd line, just after "inet addr:". It should be a string of four numbers, such as 192.168.1.123.
If connecting to the computer via the mini-USB or micro-USB port on the side of the camera, the IP address is 192.168.12.1.
