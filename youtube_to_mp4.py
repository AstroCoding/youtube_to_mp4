from pytube import YouTube
from pytube.cli import on_progress
from datetime import datetime
import os

# Following are the properties (information about the YouTube video) of the YouTube object which we can access.
# 1. Title
# 2. Length
# 3. Thumbnail_URL
# 4. Description
# 5. Views*
# 6. Rating*
# 7. Age Restricted
# 8. Video Id

# Get Link from User
link = str(input("Please paste the link to the video you would like to download: \n"))

# Get video object
try:
    reqVideo = YouTube(link, on_progress_callback=on_progress)
    # Get Confirmation on Video
    response = str(
        input(f"Please Confirm (y/n) - {reqVideo.title} ({reqVideo.length}sec): "))

    while response != 'y' and response != 'n':
        response = str(input(
            f"Sorry, Please Confirm (y/n) - {reqVideo.title} ({reqVideo.length}sec): "))

    # Depending on Confirmation, preform actions and exit.
    if response == 'y':
        print("Video Confirmed. Downloading...")
        date = datetime.today().strftime('%Y-%m-%d')
        reqVideo.streams.filter(file_extension='mp4').get_highest_resolution().download(f'{os.path.curdir}/videos/{date}/')
        print('\nFinished. Exiting...\n')
        exit(0)
    else:
        print("Wrong video input, exiting...")
        exit(0)
except EOFError as err:
    print(err)
    exit(1)
