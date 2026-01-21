"""  
text to speech
speech to text
GUI 
operation logic
multi-threading
pip install tkinter
pip install speechrecognition
pip install pyttsx3
pip install pyaudio
"""
# import pyttsx3
# engine = pyttsx3.init()
# words = "HI I am testing the python voice output"
# engine.say(words)
# engine.runAndWait()

import pyttsx3
import speech_recognition as sr
recognizer = sr.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty('rate',150)
print("PLease speak something")
speaker.say("Please speak something")
while True:
    
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source,timeout = 5,phrase_time_limit = 5)
            text = recognizer.recognize_google(audio)
            print(text)
            
            if text.lower() == "exit" or text.lower() == "terminate":
                print("Good Bye")
                speaker.say("I am terminating now.")
                break
            speaker.say(text)
            speaker.runAndWait()
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        speaker.say("Sorry, I could not understand.")
        
    except sr.RequestError:
        print("Sorry, could not process the speech")
        speaker.say("Sorry, could not process the speech")