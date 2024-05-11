
import speech_recognition as sr
import pyttsx3
import datetime
#import time
import wikipedia
import pywhatkit

# Initialization part
listener =sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('pitch',0.7)
engine.setProperty('rate',160)


# making ai to talk
def talk(text):
    engine.say(text)
    engine.runAndWait()

# fetching the data from the google

from googlesearch import search
from itertools import islice
import webbrowser



def google_search(query):
    try:
        results = search(query)
        talk(f"Top 3 results for '{query}'")
        talk('Here are your Google search results')
        for i, result in enumerate(results, start=1):
            if i > 3:
                break
            print(f"{i}. {result}")
            try:
                webbrowser.open(result)
            except Exception as e:
                print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
# Example usage




# main funtion
def take_command():
    try:
      with sr.Microphone() as source:
        print("listening.....(start the command by saying jarvis)")
        voice = listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        if 'jarvis' in command:
            command = command.replace('jarvis','')
            return command
    except:
        pass
       
    

def run_jarvis():
    
    command = take_command()
    print(command)
    if command:
       if 'youtube' in command:
        video =command.replace('play','').replace('on','').replace('youtube','')
        talk("playing"+video)
        print('playing video')
        pywhatkit.playonyt(video)
       elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak = time.replace('0','')
        talk('current time is'+speak)
       elif 'wikipedia' in command:
        person =command.replace('wikipedia','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
       elif 'google' in command:
        search = command.replace('google','')
        google_search(search) 
       else:
          talk("sorry i am under development phase try with keyword") 
    else:
       talk('sorry i cant able to understand')
    

while True:
    
    run_jarvis()