% 192.168.12.1 is the IP address of a camera when connected via USB.
cameraStartCalib = 'http://192.168.12.1/control/startCalibration';

% Set Content-Type using HeaderFields instead of MediaType
% to avoid having a semicolon after json in CharacterEncoding,
% which would cause Error 400 Bad Request.
options = weboptions('HeaderFields',{'Content-Type' 'application/json'});

% Data structure with parameters
data = struct('blackCal',true);

% Start Calibration
responseStart = webwrite(cameraStartCalib,data,options);
