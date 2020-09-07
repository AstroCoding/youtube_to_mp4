# YouTube to MP4 - Python Script

## Description

Meant for downloading educational videos from YouTube and saving them locally to a device.

## SOP

-- Collecting the Video from YouTube --
1. Perform backups and Make sure that all folders do not contain any important or required files that could be overwritten during download.
2. Head to YouTube and find the desired video you would like to download.
   - Take note of the YouTube videos title and length in seconds, as the script will confirm these details with you.
   - Copy the link of the video
3. Launch the script using the following command: `python3 ./youtube_to_mp4.py`. If the file is renamed for any reason, then make sure that you reflect that update in the command.
4. Once the script is launched, you will be brought through a step-by-step guide. Here, you will paste the link to the video, as well as confirm that the video is indeed what you expect before downloading.
5. Double check after script exits that the desired video can be found in the `videos/{date}` folder.