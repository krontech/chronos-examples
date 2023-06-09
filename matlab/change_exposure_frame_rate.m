% 192.168.12.1 is the IP address of a camera when connected via USB.
cameraURL = 'http://192.168.12.1/control/p';

% Parameters to be used for the new Exposure and FrameRate.
exposurePeriod = 300000; % time in nanoseconds
frameRate = 300;         % Frames per second

% Set Content-Type using HeaderFields instead of MediaType
% to avoid having a semicolon after json in CharacterEncoding,
% which would cause Error 400 Bad Request.
options = weboptions('HeaderFields',{'Content-Type' 'application/json'});

% Packing new parameters to structures
dataExposure = struct('exposurePeriod', exposurePeriod);
dataFrameRate = struct('frameRate', frameRate);

% Change exposurePeriod via an HTTP POST request.
response = webwrite(cameraURL,dataExposure,options);

% Change frameRate via an HTTP POST request.
response = webwrite(cameraURL,dataFrameRate,options);