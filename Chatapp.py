import random
from datetime import datetime as dt
import os
greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["what's the date","please tell me date", "date", "today's date"]
timeIntent = ["what's the time","please tell me time", "time", "current time"]
songsIntent = ["play song", "music", "play music", "song"]
movieIntent=["play movie","movie bc","movie lagaao"]
photosIntent=["pic dekh","ss de","photo"]

while True:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in greetIntent:
        ans = random.choice(greetIntent)
        print(ans.title())
    elif msg in dateIntent:
        current_date = dt.now().date()
        print(current_date.strftime("%d %B, %Y, %A"))
    elif msg in timeIntent:
        current_time = dt.now().time()
        print(current_time.strftime("%H:%M:%S, %p"))
    elif msg in songsIntent:
        songs_dir = r"G:\Music\Music"
        songs_list = os.listdir(songs_dir)
        song = random.choice(songs_list)
        song_path = songs_dir + "/" + song
        os.startfile(song_path)
    elif msg in movieIntent:
        movies_dir = r"G:\movies\Bhediya (2022) Hindi 2GB 1080p HQ S-Print Rip x264 AAC - QRips"
        movies_list = os.listdir(movies_dir)
        movie = random.choice(movies_list)
        movie_path = movies_dir + "/" + movie
        os.startfile(movie_path)
    elif msg in photosIntent:
        photos_dir = r"G:\Realme\Camera"
        photos_list = os.listdir(photos_dir)
        photo = random.choice(photos_list)
        photo_path = photos_dir + "/" + photo
        os.startfile(photo_path)
    elif msg == "bye":
        print("Bye..Take Care")
        break
    else:
        print("I don't understand...")
