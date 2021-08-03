import pyautogui
import time

time.sleep(20)
with open("Enter the path for your text file that contains the code") as f:
   text = f.read()

pyautogui.write(text,interval=0.01)

