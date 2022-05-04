## This is a addon to the choco package manager for personal downloads.(apps that arent available)

import requests
from time import sleep
import keyboard as kb
import os
from pystyle import Write, Colorate, Colors

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
                         "$$.   e$$*$$c
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



9. All
0. Exit


'''

os.system('cls')
print(Colorate.Horizontal(Colors.red_to_purple, f'{banner}', 1))
print('')
print(Colorate.Horizontal(Colors.red_to_purple, f'{menu}', 1))
choco = ['choco', 'install']
while True:
    print('')
    main_input = Write.Input("Select an option from above > ", Colors.red_to_purple, interval=0.0025).lower()
    x = main_input.split()

    if choco[0] in main_input:
        if choco[1] in main_input:
            os.system(f'{main_input}')
    elif main_input == 'cls':
        os.system(f'cls')
        print(Colorate.Horizontal(Colors.red_to_purple, f'{banner}', 1))
        print(Colorate.Horizontal(Colors.red_to_purple, f'{menu}', 1))
    elif main_input == 'clear':
        os.system(f'cls')
        print(Colorate.Horizontal(Colors.red_to_purple, f'{banner}', 1))
        print(Colorate.Horizontal(Colors.red_to_purple, f'{menu}', 1))

    
