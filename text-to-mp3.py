from gtts import gTTS 
import os

src = input("File Name: ")

dst = input("Destination: ")

file = open(src + ".txt", "r").read().replace("\n", " ")

speech = gTTS(text = str(file),lang='bn',slow = False)

speech.save(dst + ".mp3")