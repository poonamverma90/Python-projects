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

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!") 

    speak("I am Cortana Mam. Please tell me how may I help you")   

def takecommand():
    #It takes microphone input from user and returns string output.

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
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

def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mysatinbox@gmail.com','18meraMAN14')
    server.sendmail('mysatinbox@gmail.com',to,content)
    server.close()
    

if __name__ == "__main__":
    wishme()
    
    while True:
        query=takecommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 


        elif 'play music' in query:
            music_dir="E:\\music"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))  

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")    

        elif 'open code' in query:
            code_path="C:\\Users\\poonam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
            os.startfile(code_path)

        elif 'email to poonam' in query:
            try:
                speak("What should I say") 
                content=takecommand()
                to="pihhue@gmail.com" 
                sendEmail(to,content) 
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Mam . I am not able to send this email")


