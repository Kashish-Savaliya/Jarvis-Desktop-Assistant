import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import os
import datetime
# import distutils

speaker = win32com.client.Dispatch("SAPI.SpVoice")
def say(text):
    speaker.Speak(text)
        # print("Enter the word you want the computer to speak")
        # s = input()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said:", query)
    except sr.UnknownValueError:
        # print("Sorry, I couldn't understand what you said. Please try again.")
        query = f"Sorry, I couldn't understand what you said . Please try again."
    return query

if __name__ == "__main__":
    # say("How can I help you")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google", "https://www.google.com"],
                 ["instagram", "https://www.instagram.com"],["gmail", "https://www.gmail.com"],["spotify","https://www.spotify.com"]]
        # say(query)
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])
        # if "open music" in query:
        #     musicPath = "C:\\Users\\abc\\Desktop\\AI Project\\downfall-21371.mp3"
        #     import subprocess, sys
        #     opener = "open" if sys.platform == "win32" else "xdg-open"
        #     subprocess.call([opener, musicPath])
        #
        if "open music" in query :
            musicPath = "\\Users\\abc\\Desktop\\AI Project\\downfall-21371.mp3"
            os.system(f"open {musicPath}")
        if "the time" in query :
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")