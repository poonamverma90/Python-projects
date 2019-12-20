import os 
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

# pip install pyaudio
# pip install pydub
# pip install pandas
# pip install gTTS


def textToSpeech(text,filename):
    mytext=str(text)
    language = 'hi'
    myobj= gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

# this function returns pydubs audio segment

def mergeAudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined    

def generateSkeleton():
    audio=AudioSegment.from_mp3('railway.mp3')
    # 1-Generate kripya dhayan dijiye
    start = 
    finish =
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")

    # 2- is from-city
    start = 
    finish =
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")

    # 3 - Generate se chalkar
    start = 
    finish =
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3",format="mp3")

    # 4 - is via-city

    # 5-Generate ke raaste
    start = 
    finish =
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3",format="mp3")

    # 6- is to-city


    # 7- Generate ko jaane wali gadi sankhya
    start = 
    finish =
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3",format="mp3")

    # 8- is Train no and name


    # 9- Generate kuch hi samay mai platform sankhya
    start = 
    finish =
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3",format="mp3")

    # 10- is platform number

    # 11- generate par aa rahi hai
    start = 
    finish =
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3",format="mp3")





def generateAnnouncement(filename):
    df= pd.read_excel(filename)
    for index, item in df.iterrows():
        # 2 - Generate from - city
        textToSpeech(item['from'], '2_hindi.mp3')

        # 4 - Generate via -city
        textToSpeech(item['via'], '4_hindi.mp3')
       
        # 6 - Generate to- city
        textToSpeech(item['to'], '6_hindi.mp3')
       
        # 8 - Generate train no and name
        textToSpeech(item['train_no'], + " " + item['tain_name'], '8_hindi.mp3')
       
        # 10 - Generate platform number
        textToSpeech(item['plateform'], '10_hindi.mp3')

        audios= [f"{i}_hindi.mp3" for i in range(1,12)]

        announcement= mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")



if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print(" Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")

