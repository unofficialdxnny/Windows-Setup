## This is a addon to the choco package manager for personal downloads.(apps that arent available)

import requests
from time import sleep
import keyboard as kb
import os


menu = '''



9. All
0. Exit


'''
os.system('cls')
print(f'{menu}')
while True:

    main_input = input('Select an option : ')
