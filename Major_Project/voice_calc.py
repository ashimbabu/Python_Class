"""
1. Add 2 and 2
2. what is the result of 4.0 multiply by 3.0
3. what if 15 is divided by 5
4. is number 16 even or odd
5. what is the result of 3.555 plus 7.9
isdigit()
split()

"""
import speech_recognition as sr
import pyttsx3
import threading
from tkinter import *
import math
tts_engine = pyttsx3.init()
recognizer = sr.Recognizer()
tts_engine.setProperty("rate",150)

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    global stop_listening
    stop_listening = False
    with sr.Microphone() as source:
        while not stop_listening:
            try:
                #gui ko logic
                audio = recognizer.listen(source,timeout = 7,phrase_time_limit = 5)      # it listens the voice input of user
                command = recognizer.recognize_google(audio)        # it converts the audio data into text data
                # gui ko logic
                result = calculate(command)
                if result is not None:
                    print("This is the result from calculate function")
                    #gui logic - show the result to the user in gui
            except sr.WaitTimeoutError:
                print("Time out error")
                # gui logic - show the time out error in gui
            except sr.UnknownValueError:
                print("I didnt understand")
                # gui logic - show the error like "I did not understand"
            except sr.RequestError:
                print("You are offline")
                # gui logic - show error like "your internet is not available"
                



def calculate(command):
    #  what if 15 is divided by 5  
    #  what if 15 is divided by 5  then add 5 to it.
    #  Add 2 and 2   ->     [add,2,and,2]
    #  what is the result of 3.555 plus 7.9  ->   [what,is,the,result,of,3.5.55,plus,7.9]
    
    operators = [word    for word in command  if word in ["+","-","*","/"]]
    if len(operators) > 1:
        speak("Multiple operators detected")
        result = "Unsupported operation"
        return result
    
    else:
        command = command.lower()
        try:
            if "add" in command or "+" in command or "plus" in command or "addition" in command or "sum" in command :
                numbers = [ float(n)     for n in command.split()     if  n.replace('.',"",1).isdigit()  ]
                result = sum(numbers)
            
            elif "subtract" in command or "-" in command or "minus" in command :
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                result = numbers[0] - numbers[1]
                
            elif "multiply" in command or "*" in command or "x" in command or "X" in command or "times" in command:
                numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
                result = numbers[0] * numbers[1]
                
            elif "divide" in command or "/" in command or "divided" in command:
               numbers = [ float(n)    for n in command.split()    if n.replace('.',"",1).isdigit() ]
               result = numbers[0]/numbers[1] 
               
            # sin, cos, tan
            # even/odd
            # prime/composite
            # power
            # square/square root
            # cube cube root
            # hcf / lcm
            # percentage