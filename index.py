import os
import getpass
import random

username = getpass.getuser()


os.system('cls')
print('Make sure the data is in correct files provided')
print('')

print('')


with open(f'{username}.py', 'w') as a:
    with open(f'external.txt', 'r') as b:
        external = b.read()
        with open(f'internal.txt', 'r') as c:
            internal = c.read()
        a.write(f"""

     
     
## This is a addon to the choco package manager for personal downloads.(apps that arent available)

import requests
from time import sleep
import keyboard as kb
import os
from pystyle import Write, Colorate, Colors
import getpass
import random
from urllib.parse import urlparse 
from os.path import splitext

username = getpass.getuser()


external = '''

{external}

'''

internal = '''

{internal}

'''

banner = '''

            ee...      .....       .eeec.   ..eee..
          .d*"  """"*e..d*"""""**e..e*""  "*c.d""  ""*e.
         z"           "$          $""       *F         **e.
        z"             "c        d"          *.           "$.
       .F                        "            "            'F
       d                                                   J%
       3         .                                        e"
       4r       e"              .                        d"
        $     .d"     .        .F             z ..zeeeeed"
        "*beeeP"      P        d      e.      $**""    "
            "*b.     Jbc.     z*%e.. .$**eeeeP"
               "*beee* "$$eeed"  ^$$$""    "
                        '$$.     .$$$c
unofficialdxnny          "$$.   e$$*$$c   (Danial Ahmed)
                          "$$..$$P" '$$r
                           "$$$$"    "$$.           .d
               z.          .$$$"      "$$.        .dP"
               ^*e        e$$"         "$$.     .e$"
                 *b.    .$$P"           "$$.   z$"
                  "$c  e$$"              "$$.z$*"
                   ^*e$$P"                "$$$"
                     *$$                   "$$r
                     '$$F                 .$$P
                      $$$                z$$"
                      4$$               d$$b.
                      .$$%            .$$*"*$$e.
                   e$$$*"            z$$"    "*$$e.
                  4$$"              d$P"        "*$$e.
                  $P              .d$$$c           "*$$e..
                 d$"             z$$" *$b.            "*$L
                4$"             e$P"   "*$c            ^$$
                $"            .d$"       "$$.           ^$r
               dP            z$$"         ^*$e.          "b
              4$            e$P             "$$           "
                           J$F               $$
                           $$               .$F
                          4$"               $P"
                          $"               dP 
       
'''


menu = '''


1. External Install (EI)
2. Choco Install (CI)
3. All


0. Exit


'''


import ctypes, sys
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    os.system('cls')
    print(Colorate.Horizontal(Colors.red_to_purple, banner, 1))
    print('')
    print(Colorate.Horizontal(Colors.red_to_purple, menu, 1))
    choco = ['choco', 'install']
    while True:
        print('')
        main_input = Write.Input("Select an option from above > ", Colors.red_to_purple, interval=0.0025).lower()
        x = main_input.split()

    
        if main_input == 'ci':
            os.startfile(f'choco.ps1')
            with open(f'internal.txt', 'r') as b:
                for lines in b:
                    os.system(f'choco install {lines} -y --force')

        elif main_input == 'ei':
            with open(f'external.txt', 'r') as f:
                lines = f.readlines()
                print(f'Installing Your External Files')
                for url in lines:
                    path = urlparse(url).path
                    ext = splitext(path)[1]
                for line in lines:
                    url = line
                    r = requests.get(url, allow_redirects=True)
                    x = random.random()
                    open(f'{x}.{ext}', 'wb').write(r.content)
                    

                
            



        elif main_input == 'cls':
            os.system(f'cls')
            print(Colorate.Horizontal(Colors.red_to_purple, banner, 1))
            print(Colorate.Horizontal(Colors.red_to_purple, menu, 1))



        elif main_input == 'clear':
            os.system(f'cls')
            print(Colorate.Horizontal(Colors.red_to_purple, banner, 1))
            print(Colorate.Horizontal(Colors.red_to_purple, menu, 1))
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


    
    """)


run = input(f'Your file {username}.py has been made would you like to run it now? (y/n)')

if run == 'y':
    os.system(f'python {username}.py')
elif run == 'n':
    print('Thanks for using my tool :) - unofficialdxnny (Danial Ahmed)')
elif run != ['y', 'n']:
    n = random.randint(1,10000000)
    print(f'Invalid input exitting with error coded {n}')