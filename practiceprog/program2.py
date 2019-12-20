import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r=sr.Recognizer()
    r.recognize_google(audio)
    with sr.Microphone as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    
    return query

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!") 

    speak("I am Cortana Mam. Please tell me how may I help you")   



if __name__ == "__main__":
    wishme()
    
    
    while True:
        query=takecommand()

        if 'my username is' in query:
            try:
                speak("What should I say") 
                content=takecommand()
                print(content) 
                
                speak("your username is ")

            except Exception as e:
                print(e)
                speak("Sorry Mam . I am not able to listen")

            
           