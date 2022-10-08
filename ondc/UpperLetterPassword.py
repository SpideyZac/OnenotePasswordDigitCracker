import string
import pyautogui
import keyboard
import threading

CHARS = string.ascii_uppercase + " "

def guess_iter(currentPassword: str, depth: int, maxDepth: int, to_type) -> None:
    for digit in CHARS:
      if not keyboard.is_pressed("q"):
        if depth + 1 < maxDepth:
          guess_iter(currentPassword + digit, depth + 1, maxDepth, to_type)
        else:
          to_type.append(currentPassword + digit)

def start_guessing(pasBoxX: float, pasBoxY: float, start: int, digits: int, to_type) -> None:
    pyautogui.moveTo(pasBoxX, pasBoxY)
    pyautogui.click()

    threads = []
    
    for i in range(start, digits + 1):
      thread = threading.Thread(target=guess_iter, args=("", 0, i, to_type))
      thread.start()
      threads.append(thread)

    while True:
      for thread in threads:
        if thread.is_alive():
          break
      else:
        break