import time

import random
from pynput.keyboard import Controller, Key

keyboard = Controller()  # Create the controller

def type_string_with_delay(string):
    for character in string:  # Loop over each character in the string
        keyboard.type(character)  # Type the character
        delay = random.uniform(0.05, 0.08)
        if character == " ":
            delay = random.uniform(0.2, 0.5)
          
        time.sleep(delay)  # Sleep for the amount of seconds  generated

with open("cantor_function.py", "r") as f:
    strings = f.readlines()
time.sleep(2)
for string in strings:
  string = string.replace("  ", "")
  type_string_with_delay(string)
  with keyboard.pressed(Key.ctrl):
    keyboard.type('\n')

  time.sleep(1)