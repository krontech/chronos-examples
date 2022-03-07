#!/usr/bin/python3
import os
import sys
import argparse
import time
import json
import requests
import ffmpeg

def verify_chronos_connection(chronos_ip_address):
    """ Verify connection to Chronos camera """
    CHRONOS_URL_API = chronos_ip_address + '/control'

    # Check if able to talk to Kron IP's address
    response = requests.get(chronos_ip_address)
    if response.status_code != 200:
        print("Error: Unable to talk to Kron")
        return False

    # Check if able to talk to Kron API
    response = requests.get(CHRONOS_URL_API + '/describe')
    if response.status_code != 200:
        print("Error: Unable to talk to Kron API")
        return False
    
    # Check that there are methods available
    response = requests.get(CHRONOS_URL_API + '/availableCalls')
    if response.status_code != 200:
        print("Error: Unable to get calls")
        return False
    
    # Everything works
    return True

def record_video(chronos_ip_address, rec_mode="normal", recording_time=5):
    """ Record a video with chronos camera """
    CHRONOS_URL_API = chronos_ip_address + '/control'

    # Flush recording before we start recording
    response = requests.post(CHRONOS_URL_API + '/flushRecording')

    # Record a 10 second video
    # To-do: Incorporate server-sent events handling
    payload = {
        'recMode': rec_mode,
    }
    print("Begin new recording of " + str(recording_time) + " seconds")
    response = requests.post(CHRONOS_URL_API + '/startRecording', payload)
    if response.status_code == 200:
        # Wait for specified recording time then stop recording
        time.sleep(recording_time)
        requests.post(CHRONOS_URL_API + '/stopRecording', payload)
        print("Stop recording")
        return True
    else:
        # Stop recording, just in case
        requests.post(CHRONOS_URL_API + '/stopRecording', payload)
        print("Bad recording")
        return False

def save_video_smb(chronos_ip_address, video_path):
    """ Save video with chronos camera to SMB File Share """
    CHRONOS_URL_API = chronos_ip_address + '/control'

    # Stop saving video files, just in case
    requests.get(CHRONOS_URL_API + '/stopFilesave')
    time.sleep(2)

    # Start video saving and wait till it finishes
    MEDIA_PATH_SMB = '/media/smb'
    video_file_name = 'helloworld' # To-do: put timestamp
    video_file_path = video_path + '/' + video_file_name + '.mp4'

    # Check if able to write to path
    # Python natively only looks on local paths (i.e not remote paths)
    path_found = False
    if os.path.exists(video_path):
        path_found = True
        if os.path.exists(video_file_path) and os.path.isfile(video_file_path):
            print("Caution: File already exists. Will not override file")
    else:
        print("Error: Unable to find path. Is it a remote path?")
        return False

    # Prepare payload
    payload = {
        # 'bitrate': 0.25,
        'device': 'smb',
        'filename': video_file_name, # From host's perspective, best to set your own filename
        'format': 'h264', # To-do: change video format
        'framerate': 60, # Default at 60 FPS
        # 'length': 10*1069, # Number of frames to be saved
        'start': 0 # Start at frame 0
    }

    print("Saving video file to SMB location...")
    response = requests.post(CHRONOS_URL_API + '/startFilesave', payload)
    if response.status_code == 200:
        # Wait for 2 seconds before we start checking progress
        time.sleep(2)
        response = requests.get(CHRONOS_URL_API + '/p/' + 'videoState')
        playback_JSON = json.loads(response.text)
        video_state = playback_JSON['videoState']
        is_saving = False

        # Will not write to path if there is a matching filename at destination
        if video_state != "filesave":
            print("Error: Unable to enter filesave state.")
            print("Current camera videoState: " + video_state)
            return False
        else:
            is_saving = True
            response = requests.get(CHRONOS_URL_API + '/p/' + 'playbackLength')
            playback_JSON = json.loads(response.text)
            current_playback_length = playback_JSON['playbackLength']
            current_playback_position = 0

        # Wait till video file finishes saving
        while is_saving:
            # Check progress
            response = requests.get(CHRONOS_URL_API + '/p/' + 'playbackPosition')
            playback_JSON = json.loads(response.text)
            current_playback_position = playback_JSON['playbackPosition']

            # Check if saving is done
            response = requests.get(CHRONOS_URL_API + '/p/' + 'videoState')
            playback_JSON = json.loads(response.text)
            video_state = playback_JSON['videoState']

            # Exit Loop cause file is saved
            if video_state != "filesave":
                is_saving = False
                requests.post(CHRONOS_URL_API + '/stopFilesave', payload)
                print("Finishing saving file " + video_file_name + '.mp4')
                return (video_file_name + '.mp4')
            # Print current progress then sleep for 2 seconds
            else:
                print(
                    "Saving Frame: " + str(current_playback_position) + " / " +
                    str(current_playback_length)
                )
                time.sleep(2)
    else:
        print("Error when attempting to save video file!")
        print(response.text)

        requests.post(CHRONOS_URL_API + '/stopFilesave', payload)
        return False

def verify_file(video_path):
    """ Verify video integrity using FFmpeg """
    if os.path.exists(video_path) and os.path.isfile(video_path):
        print("Verifying video interity at " + video_path)

        # Could use more work than simply trying to "play" the video
        # See https://github.com/kkroening/ffmpeg-python/issues/282
        try:
            (
                ffmpeg
                .input(video_path)
                .output("null", f="null", loglevel="error")
                .run()
            )
        except ffmpeg._run.Error:
            print("Video is corrupted")
            return False
        else:
            print("Video verified")
            return True
    else:
        print("Error! File does not exist at " + video_path)
        return False

if __name__ == "__main__":
    # Parse Arguments
    parser = argparse.ArgumentParser(description='Record and save video files via Windows SMB')
    parser.add_argument('chronos_ip_address', type=str, help="Chronos Camera's IP Address")
    parser.add_argument('video_path', type=str, help="Path to Windows SMB file location")

    # Store Arguments into variables
    args = parser.parse_args()
    chronos_ip_address = args.chronos_ip_address
    video_path = args.video_path

    # Record and save video to SMB file
    if verify_chronos_connection(chronos_ip_address):
        record_video(chronos_ip_address, "normal", 5)
        video_filename = save_video_smb(chronos_ip_address, video_path)

    # Verify video if it exists
    if video_filename and type(video_filename) is str:
        verify_file(video_path + '/' + video_filename)
