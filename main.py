import os
import requests
import getpass
from time import sleep
import keyboard as kb
import ctypes
import sys
from pystyle import Write, Colorate, Colors

banner = '''


                                             
    ___     / __      ___      ___      ___    
  //   ) ) //   ) ) //   ) ) //   ) ) //   ) ) 
 //       //   / / //   / / //       //   / /  
((____   //   / / ((___/ / ((____   ((___/ /   

Supports : exe, zip            
Version : v1.0.0
'''
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    print(Colorate.Color(Colors.red, banner, True))
    print('')
    username = getpass.getuser()

    ## install chocolatey
    powershell = f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Windows PowerShell/Windows PowerShell'

    os.startfile(powershell)
    
    sleep(2)
    kb.write("Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")
    kb.press('enter')
    kb.write('exit')
    kb.press('enter')
    
    Write.Print(f"Installing Your Applications!", Colors.blue_to_green, interval=0.05)
    def install():
        with open(f'exe.t', 'r') as a:
            lines = a.readlines()
            for line in lines:
                r = requests.get(f'{lines}')
                print(r.content)




else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)