__version__ = "0.0.1"
__author__ = "SpideyZac#8044 (Discord)"

import pyautogui
import keyboard
import ondc.DigitPassword as DigitPassword

pyautogui.alert("Welcome to OneNote Password Digit Cracker!")
pyautogui.alert(f"You are using version: {__version__}")
pyautogui.alert(f"This program was made by: {__author__}")
pyautogui.alert("I am not responsible for any damages caused by this program, please use responsibly")

mode = pyautogui.confirm('Enter an Cracker Mode', buttons=['Digit Cracker'])
confirm = pyautogui.confirm("Do you understand that you are responsible for anything that happens while using this program?")

if confirm == "OK":
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
    locked = pyautogui.screenshot('locked.png', region=(corner1x, corner1y, abs(corner2x - corner1x), abs(corner2y - corner1y)))
    startDepth = int(pyautogui.prompt('Please enter the start depth (the start length of the password)'))
    maxDepth = int(pyautogui.prompt('Please enter the max depth (the max length of the password)'))
    pyautogui.alert("Starting... press 'q' to stop")
    DigitPassword.start_guessing(mouseX, mouseY, startDepth, maxDepth)