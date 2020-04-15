% 192.168.12.1 is the IP address of a camera when connected via USB.
cameraURL = 'http://192.168.12.1/control/p';

% Parameters to be used for the new resolution.
hRes = 640;
vRes = 480;
bitDepth = 12;

% Set Content-Type using HeaderFields instead of MediaType
% to avoid having a semicolon after json in CharacterEncoding,
% which would cause Error 400 Bad Request.
options = weboptions('HeaderFields',{'Content-Type' 'application/json'});

% When setting parameters inside another parameter, they should be nested.
dataInside = struct('hRes', hRes, 'vRes', vRes, 'bitDepth', bitDepth);
dataOutside = struct('resolution', dataInside);

% Change resolution via an HTTP POST request.
response = webwrite(cameraURL,dataOutside,options);
