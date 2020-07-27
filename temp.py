# -*- coding: utf-8 -*-
"""
Spyder Editor

Python classes for Point and Line
@author: Nikhil Bhargava
"""

import speech_recognition as sr
import os 
import json

'''
command2mp3 = "ffmpeg -loglevel quiet -i badshah.mp4 badshah.mp3"
command2wav = "ffmpeg -loglevel quiet -i badshah.mp3 badshah.wav"


os.system(command2mp3)
os.system(command2wav)
'''
AUDIO_FILE="sample_large.wav"
#Use Audio file as source
r=sr.Recognizer()  #Initialize the recognizer

with sr.AudioFile(AUDIO_FILE) as source:
   #r.adjust_for_ambient_noise(source, duration=0.5)
   audio=r.record(source)

try:
    text=r.recognize_google(audio,show_all=False)
    print(json.dumps(text, indent=2))
    #print("Audio file contains "+text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not find any words in "+"badshah.wav")
except sr.RequestError:
    print("Couldnot get the results from Google Speech Recognition")