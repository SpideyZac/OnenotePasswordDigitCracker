__version__ = "0.0.2"
__author__ = "SpideyZac#8044 (Discord)"

import pyautogui
import keyboard
import ondc.DigitPassword as DigitPassword
import ondc.CharPassword as CharPassword
import ondc.LowerLetterPassword as LowerLetterPassword
import ondc.UpperLetterPassword as UpperLetterPassword
import ondc.LettersPassword as LettersPassword
import threading
import time
from collections import deque

to_type = []
last_values = deque([], 5)

pyautogui.alert("Welcome to OneNote Password Digit Cracker!")
pyautogui.alert(f"You are using version: {__version__}")
pyautogui.alert(f"This program was made by: {__author__}")
pyautogui.alert("I am not responsible for any damages caused by this program, please use responsibly")

mode = pyautogui.confirm('Enter an Cracker Mode', buttons=['Digit Cracker', "Char Cracker", "Lower Case Cracker", "Upper Case Cracker", "All Letters Cracker"])
confirm = pyautogui.confirm("Do you understand that you are responsible for anything that happens while using this program?")

m = None

last = None
start = time.time()

stop_writer = False

def checker(locked):
    global stop_writer

    while True:
        if pyautogui.locateOnScreen(locked) is None:
            stop_writer = True
            time.sleep(2)
            pyautogui.alert(f"The password is around '{last_values[0]}' - '{last_values[-1]}'\nChar Set: {m.CHARS}\nTook: {time.time() - start} seconds")
            return

def writer(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    global last

    while True:
        if keyboard.is_pressed("q"):
            break
        if not stop_writer:
            if len(to_type) > 0:
                to_write = to_type.pop(0)
                last = to_write
                last_values.append(last)
                pyautogui.write(to_write + "\n", interval=0.01)
        else:
            return

if confirm == "OK":
    if mode == "Digit Cracker":
        m = DigitPassword
    elif mode == "Char Cracker":
        m = CharPassword
    elif mode == "Lower Case Cracker":
        m = LowerLetterPassword
    elif mode == "Upper Case Cracker":
        m = UpperLetterPassword
    elif mode == "All Letters Cracker":
        m = LettersPassword

    pyautogui.alert("Please move your mouse to the password box and click the key ';'")
    mouseX = 0
    mouseY = 0
    while not keyboard.is_pressed(';'):
        mouseX, mouseY = pyautogui.position()
    pyautogui.alert("Please move your mouse to the top left of the text 'This section is password protected' and press ';'")
    corner1x = 0
    corner1y = 0
    while not keyboard.is_pressed(';'):
        corner1x, corner1y = pyautogui.position()
    pyautogui.alert("Please move your mouse to the bottom right of the text 'This section is password protected' and press ';'")
    corner2x = 0
    corner2y = 0
    while not keyboard.is_pressed(';'):
        corner2x, corner2y = pyautogui.position()
    locked = pyautogui.screenshot("locked.png", region=(corner1x, corner1y, abs(corner2x - corner1x), abs(corner2y - corner1y)))
    startDepth = int(pyautogui.prompt('Please enter the start depth (the start length of the password)'))
    maxDepth = int(pyautogui.prompt('Please enter the max depth (the max length of the password)'))
    pyautogui.alert("Starting... press 'q' to stop")
    thread = threading.Thread(target=writer, args=(mouseX, mouseY))
    thread.start()
    thread2 = threading.Thread(target=checker, args=("locked.png",))
    thread2.start()
    m.start_guessing(mouseX, mouseY, startDepth, maxDepth, to_type)