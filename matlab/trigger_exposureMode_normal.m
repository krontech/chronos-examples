% 192.168.12.1 is the IP address of a camera when connected via USB.
cameraCtrlP = 'http://192.168.12.1/control/p';

% Set Content-Type using HeaderFields instead of MediaType
% to avoid having a semicolon after json in CharacterEncoding,
% which would cause Error 400 Bad Request.
options = weboptions('HeaderFields',{'Content-Type' 'application/json'});

% choosing exposureMode for trigger
% available modes 'normal' , 'shutterGating', 'frameTrigger'
exposure_mode = 'normal';

% packing data structure with parameters
dataStruct = struct('exposureMode', exposure_mode);

% Start
response = webwrite(cameraCtrlP,dataStruct,options);
disp(response)