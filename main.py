######################
# Name: Darren Bowers
# Audio File Updater
# Purpose: Quickly cycle through a folder and change names of mp3/wav/flac files to match the title in the metadata if necessary.
######################


import mutagen
import os
from distutils.log import info
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.wave import WAVE

user_choice = "open"
while user_choice != "exit":
    user_choice = input("To continue enter a folder location, to exit type exit: ")
    if os.path.isdir(user_choice):
        folder = user_choice + "\\" 
        print(folder, "found")
        for file_name in os.listdir(folder):
            if file_name.endswith('.mp3'):
                print("File name:", file_name)
                source = folder + file_name
                audio = EasyID3(source)
                try:
                    title = ''.join(audio["title"])
                except:
                    title = file_name[:-4]
                    print("No title found for file")
                destination = folder + title +".mp3"
                try:
                    if not os.path.isfile(destination):
                        os.rename(source, destination)
                        print("File Renamed")
                    else:
                        print("Unnable to rename file")
                except:
                    print("Title contains invalid characters")
            elif file_name.endswith('.flac'):
                print("File name:", file_name)
                source = folder + file_name
                audio = FLAC(source)
                try:
                    title = ''.join(audio["title"])
                except:
                    title = file_name[:-5]
                    print("No title found for file")
                destination = folder + title + ".flac"
                try:
                    if not os.path.isfile(destination):
                        os.rename(source, destination)
                        print("File Renamed")
                    else:
                        print("Unnable to rename file")
                except:
                    print("Title contains invalid characters")
            elif file_name.endswith('.wav'):
                print("File name:", file_name)
                source = folder + file_name
                audio = WAVE(source)
                try:
                    title = ''.join(audio["TIT2"])
                except:
                    title = file_name[:-4]
                    print("No title found for file")
                destination = folder + title +".wav"
                try:
                    if not os.path.isfile(destination):
                        os.rename(source, destination)
                        print("File Renamed")
                    else:
                        print("Unnable to rename file")
                except:
                    print("Title contains invalid characters")
            else:
                print(file_name, "Is an unsupported file type")
    elif user_choice == "exit":
        print("Exiting")
    else:
        print("folder not found")