import time

import random
from pynput.keyboard import Controller, Key


keyboard = Controller()

def type_string_with_delay(string):
    for character in string:
        keyboard.type(character)
        delay = random.uniform(0.05, 0.08)
        if character == " ":
            delay = random.uniform(0.1, 0.2)
          
        time.sleep(delay)

with open("cantor_function.py", "r") as f:
  strings = f.readlines()

time.sleep(2)

for string in strings:
  type_string_with_delay(string)
  time.sleep(1)