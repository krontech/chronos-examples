cameraURL = "http://192.168.12.1/control/startFilesave";
data = {"format", "h264", "device", "sda1", "start", "300", "length", "500"};
response = urlread (cameraURL, "post", data);
