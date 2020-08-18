status = urlread('http://192.168.12.1/control/startRecording','post','{}');
pause(2);
status = urlread('http://192.168.12.1/control/stopRecording','post','');
