import pyautogui

import time

print("We are automating WhatsApp")

time.sleep(5)

pyautogui.press("win")

time.sleep(1)

pyautogui.write("WhatsApp")

time.sleep(1)

pyautogui.press("enter")

time.sleep(1)

pyautogui.hotkey("ctrl","f")

time.sleep(1)

pyautogui.write("Python Class")

time.sleep(1)

pyautogui.press("enter")

time.sleep(1)

message = "Assignment: \n1. Use the concept of lambda and recursion to implement any simple logic. \n2. Use any standard library to implement simple logic. "

pyautogui.write(message)

time.sleep(1)

pyautogui.press("enter")

print("Message sent successfully")



print("Youtube opening automation")

time.sleep(3)

pyautogui.press("win")

time.sleep(1)

pyautogui.write("chrome")

time.sleep(1)

pyautogui.press("enter")

time.sleep(2)

pyautogui.write("youtube.com")

time.sleep(1)

pyautogui.press("enter")

print("Youtube opened successfully")
