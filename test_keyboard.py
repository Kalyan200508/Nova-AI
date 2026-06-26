import time
from automation.keyboard import keyboard

print("You have 10 seconds to click inside Notepad...")

time.sleep(10)

keyboard.write("Hello Kalyan!")
keyboard.press("enter")
keyboard.write("Nova can type now.")