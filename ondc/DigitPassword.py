import string
import pyautogui
import keyboard

DIGITS = string.digits

def guess_iter(currentPassword: str, depth: int, maxDepth: int) -> None:
    for digit in DIGITS:
      if not keyboard.is_pressed("q"):
        if depth + 1 < maxDepth:
          guess_iter(currentPassword + digit, depth + 1, maxDepth)
        else:
          # print(currentPassword + digit)
          pyautogui.write(currentPassword + digit + "\n")
          if pyautogui.locateOnScreen('locked.png') is None:
            pyautogui.alert(f"Password is somehwere around: {currentPassword + digit} remember that there is a delay in when onenote registers the correct password so this number may be off by a couple digits")
            exit()

def start_guessing(pasBoxX: float, pasBoxY: float, start: int, digits: int) -> None:
    pyautogui.moveTo(pasBoxX, pasBoxY)
    pyautogui.click()
    
    for i in range(start, digits + 1):
      guess_iter("", 0, i)
  
