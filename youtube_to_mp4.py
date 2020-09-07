from pytube import YouTube

# Get Link from User
link = str(input("Please paste the link to the video you would like to download: \n"))

# Get video object
reqVideo = YouTube(link)

# Following are the properties (information about the YouTube video) of the YouTube object which we can access.
# 1. Title
# 2. Length
# 3. Thumbnail_URL
# 4. Description
# 5. Views*
# 6. Rating*
# 7. Age Restricted
# 8. Video Id

response = str(input(f"Please Confirm (y/n) - {reqVideo.title} ({reqVideo.length}): "))

while response != 'y' and response != 'n':
    response = str(input(f"Sorry, Please Confirm (y/n) - {reqVideo.title} ({reqVideo.length}sec): "))

if response == 'y':
    print("Video Confirmed. Downloading...")
    stream = reqVideo.streams.first()
    stream.download('./videos/')
    print('Finished. Exiting...')
    exit(0)
else:
    print("Wrong video input, exiting...")
    exit(0)