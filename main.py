## This is a addon to the choco package manager for personal downloads.(apps that arent available)

import requests
from time import sleep
import keyboard as kb
import os
import sys


menu = '''



9. All
0. Exit


'''
os.system('cls')
print(f'{menu}')
choco = ['choco', 'install']
while True:

    main_input = input('Select an option : ').lower()
    x = main_input.split()

    if choco[0] in main_input:
        if choco[1] in main_input:
            os.system(f'{main_input}')

        
