#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:57:04 2020

@author: nikhil1.bhargava
"""

import speech_recognition as sr
AUDIO_FILE=("sample.WAV")

#Use Audio file as source
r=sr.Recognizer()  #Initialize the recognizer

with sr.AudioFile(AUDIO_FILE) as source:
   audio=r.record(source)

try:
    print("Audio file contains "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not find any words in "+AUDIO_FILE)
except sr.RequestError:
    print("Couldnot get the results from Google Speech Recognition")

