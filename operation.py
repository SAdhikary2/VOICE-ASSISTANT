import speech_recognition as sr
import pyttsx3
import time
import datetime
from time import ctime
import webbrowser
import playsound
import wikipedia
import os
import random
from gtts import gTTS
import smtplib

#____________________SPEAKING FUNCTION______________

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#___________________GRETTING USER__________________
def Gretting_user():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Friends!!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon Friends !!!")
    else:
        speak("Good Evening friends!!!")
    speak("I am pepper. please tell me how may i help you!!!")


#_________________________WORKING FEATURES___________________________________
    while True:
        query = Microphone_input().lower()

        if 'wikipedia' in query:
            speak("Searching the wikipedia.....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to the wikipedia....")
            speak(result)
            print(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            String_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,The time is now {String_time}")
            print(String_time)
        elif 'tell me about yourself' in query:
            speak("I am Pepper sir.... i am a voice assistant and i am developed by the software engineer Sukalyan Adhiakry")

        elif 'exit' in query:
            speak("Thank you so much sir .Have a nice day!!!!")
            exit()
        # _________________FOR EMAIL_________________
    """
    elif 'email to harry' in query:
          try:
              speak("What should I say?")
              content = takeCommand()
              to = "harryyourEmail@gmail.com"    
              sendEmail(to, content)
              speak("Email has been sent!")
          except Exception as e:
              print(e)
              speak("Sorry my friend harry bhai. I am not able to send this email")  
    """


#________________MICROPHONE INPUT TAKING____________

def Microphone_input():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recogniging.....")
        query=r.recognize_google(audio,language='en-in')
        speak(query)
        print(f"User Said : {query}\n")

    except Exception as e:
        print("say that again please....")
        return "None"
    return query


#_________________FUNCTION FOR SEND EMAIL__________
"""
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
"""

















