import pytube
import os

url = input("Enter the YouTube URL: ")
format_choice = int(input("Choose the download format: \n1 = .mp3\n2 = .mp4\n3 = .avi\n4 = .gif\n"))

yt = pytube.YouTube(url)
stream = None

if format_choice == 1:
    stream = yt.streams.filter(only_audio=True).first()
elif format_choice == 2:
    stream = yt.streams.filter(file_extension='mp4').first()
elif format_choice == 3:
    stream = yt.streams.filter(file_extension='avi').first()
elif format_choice == 4:
    stream = yt.streams.filter(file_extension='gif').first()

if stream:
    stream.download()
    print("Download completed.")
else:
    print("Invalid format choice or format not available.")
