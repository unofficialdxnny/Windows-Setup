import os
import getpass
import random

username = getpass.getuser()


os.system('cls')
print('It is better to have The files in the cwd')
print('')
exter = input('Path to external download links file : > ')
inter = input('Path to choco download links file : > ')
print('')


with open(f'{username}.py', 'w') as a:
    with open(f'{exter}.txt', 'r') as b:
        external = b.read()
        with open(f'{inter}', 'r') as c:
            internal = c.read()
        a.write(f"""

      
## This is a addon to the choco package manager for personal downloads.(apps that arent available)

import requests
from time import sleep
import keyboard as kb
import os
from pystyle import Write, Colorate, Colors



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

os.system('cls')
print(Colorate.Horizontal(Colors.red_to_purple, banner, 1))
print('')
print(Colorate.Horizontal(Colors.red_to_purple, menu, 1))
choco = ['choco', 'install']
while True:
    print('')
    main_input = Write.Input("Select an option from above > ", Colors.red_to_purple, interval=0.0025).lower()
    x = main_input.split()

    if choco[0] in main_input:
        if choco[1] in main_input:
            os.system(main_input)
    elif main_input == 'cls':
        os.system(f'cls')
        print(Colorate.Horizontal(Colors.red_to_purple, banner, 1))
        print(Colorate.Horizontal(Colors.red_to_purple, menu, 1))

    

    elif main_input == 'clear':
        os.system(f'cls')
        print(Colorate.Horizontal(Colors.red_to_purple, banner, 1))
        print(Colorate.Horizontal(Colors.red_to_purple, menu, 1))
    
    
    """)


run = input(f'Your file {username}.py has been made would you like to run it now? (y/n)')

if run == 'y':
    os.system(f'python {username}.py')
elif run == 'n':
    print('Thanks for using my tool :) - unofficialdxnny (Danial Ahmed)')
elif run != ['y', 'n']:
    n = random.randint(1,10000000)
    print(f'Invalid input exitting with error coded {n}')