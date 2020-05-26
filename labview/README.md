Introduction
====================
This VI is an example of how to control a camera using National Instruments LabVIEW.

Supported Functions
--------------------
 * Start/Stop recording
 * Save a portion of the buffer to the SD card in the camera
    - This is currently configured to save a 200-frame long region, starting 300 frames after the beginning of the recording.
 * Copy the most recent video from the camera to the computer which is controlling the camera.
 * Apply resolution
    - If you get an error saying the resolution could not be set, just press the Apply Resolution button a second time.

The example currently assumes that the camera is connected to the computer via the mini-USB or micro-USB connection on the side of the camera.

The "Copy from SD card to computer" block is heavily based on the "Downloader.vi" VI posted by CharlieRodway here: https://forums.ni.com/t5/LabVIEW/Can-LabVIEW-download-files-from-the-Internet-I-know-the-URLs-of/m-p/221719?profile.language=en#M123371
