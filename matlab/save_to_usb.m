cameraURL = 'http://192.168.12.1/control/startFilesave';
options = weboptions('MediaType','application/json');
response = webwrite(cameraURL,'format','h264','device','sda1','start',300,'length',500);
