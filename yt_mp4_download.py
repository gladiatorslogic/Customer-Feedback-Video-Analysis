from pytube import YouTube
from pytube.cli import on_progress

# where to save
SAVE_PATH = "C:\\Users\\Ankit Mishra\\PycharmProjects\\VideoIntelligence"

# link of the video to be downloaded
link = "https://www.youtube.com/watch?v=7m4zQpf3Ouo"

"""
    Running the code inside the try/except block
"""


# this is the handler/function for downloading the video
# the function takes the video url as an argument
def video_downloader(video_url):
    # passing the video url and progress_callback to the YouTube object
    my_video = YouTube(video_url, on_progress_callback=on_progress)
    # downloading the video in high resolution
    my_video.streams.get_highest_resolution().download()
    # return the video title
    return my_video.title


try:
    # getting the url from the user
    youtube_link = input('Enter the YouTube link:')
    print(f'Downloading your Video, please wait.......')
    # passing the url to the function
    video = video_downloader(youtube_link)
    # printing the video title
    print(f'"{video}" downloaded successfully!!')

except:
    print(f'Failed to download video')
