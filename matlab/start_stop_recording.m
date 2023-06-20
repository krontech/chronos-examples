% 192.168.12.1 is the IP address of a camera when connected via USB.
cameraStartRecording = 'http://192.168.12.1/control/startRecording';
cameraStopRecording = 'http://192.168.12.1/control/stopRecording';

% Set Content-Type using HeaderFields instead of MediaType
% to avoid having a semicolon after json in CharacterEncoding,
% which would cause Error 400 Bad Request.
options = weboptions('HeaderFields',{'Content-Type' 'application/json'});

% EMPTY DATA STRUCTURE 
data = struct();

% Start recording
responseStart = webwrite(cameraStartRecording,data,options);

% PAUSE
pause(2);

% Stop recording
responseStop = webwrite(cameraStopRecording,data,options);
