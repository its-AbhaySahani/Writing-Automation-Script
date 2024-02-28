import pyautogui
import time

code ='''
Write Your Script Here....

'''

pyautogui.hotkey('alt', 'tab')
time.sleep(1)
conv=""
for i in code.split("\n"):
    conv+="#"+i+"\n"
# Type the text
pyautogui.write(conv, interval=0.01)