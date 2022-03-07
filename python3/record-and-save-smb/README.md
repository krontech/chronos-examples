# record-and-save-smb
Demonstration of how to record and save a video file to your host environment via SMB Share, and verify the video file usign FFMpeg
# Setup

## SMB Share - Windows
1. Follow the [SMB Share Setup Guide0(https://www.krontech.ca/wp-content/uploads/2020/07/Chronos-SMB-Share-Setup-Guide.pdf)
2. Connect your camera to the same network as your host computer via Ethernet.
3. Install [python](https://www.python.org/downloads/windows/).
4. Install [FFmpeg](https://www.ffmpeg.org/download.html).
5. Create a Python virtual Environment with the following command
  `python3 -m venv virtual_environment_name`
6. Activate the Python virtual environment with the following command:
  `.\virtual_environment_name\Scripts\activate.bat`
  - You may also use the following command to activate your virtual environment:
  `source ./venv/Scripts/activate`
7. To install all the libraries, run the following command:
  `python3 -m pip3 install -r requirements.txt`
8. Execute the Python script with the following command:
  `python3 src/record-and-save-smb.py "http://<IP address of Chronos camera>" "<Path to Windows SMB Share Location>"`

## SMB Share - Linux

Needs work. Unable to configure Linux SMB server to connect host to camera.
