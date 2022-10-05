import string
import pyautogui

DIGITS = string.digits

def guess_iter(currentPassword: str, depth: int, maxDepth: int) -> None:
  '''
  Preforms a guess iteration
  
  Parameters:
    currentPassword: str = the current guessed password
    depth: int = the depth of this password
  '''
  
  for digit in DIGITS:
    if depth + 1 <= maxDepth:
      guess_iter(currentPassword + digit, depth + 1, maxDepth)
    else:
      pyautogui.click()
      pyautogui.write(currentPassword + digit + "\n")

def start_guessing(pasBoxX: float, pasBoxY: float, digits: int) -> None:
  '''
  Guesses all possible passwords with only digit characters.
  
  Parameters:
    pasBoxX: float = the position of the password box X on screen
    pasBoxY: float = the position of the password box Y on screen
    digits: int = The maximum number of digits in the password
  '''
  
  pyautogui.moveTo(pasBoxX, pasBoxY)
  
  for i in range(digits + 1):
    guess_iter("", 0, i)
  
