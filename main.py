import os
import requests
from requests.exceptions import ConnectionError
import getpass
from time import sleep
import keyboard as kb
import ctypes
import sys
from pystyle import Write, Colorate, Colors
import random
from urllib.parse import urlparse


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

    
    def install_choco():
        filesize = os.path.getsize("choco.t")
        if filesize == 0:
            print("0 applications need to be installed: " + str(filesize))
        else:
            Write.Print(f"Make Sure You Installed Chocolatey...", Colors.blue_to_green, interval=0.05)
            with open(f'choco.t', 'r') as a:
                lines = a.readlines()
                for line in lines:
                    app = line
                    os.system(f'choco install {app} -y --force')
                    print('')        
    install_choco()


    def install_exe():
        filesize = os.path.getsize("exe.t")
        if filesize == 0:
             print("0 executables need to be installed: " + str(filesize))
        else:
            Write.Print(f"Installing Your executables!", Colors.blue_to_green, interval=0.05)
            print('')
            with open(f'exe.t', 'r') as b:
                lines = b.readlines()
                for line in lines:
                    url = line
                    r = requests.get(url, allow_redirects=True)
                    t = urlparse(url).netloc
                    print ('.'.join(t.split('.')[-2:]))
                    open(f'{t}.exe', 'wb').write(r.content)
                    print('')
    install_exe()

    def install_zip():
        filesize = os.path.getsize("zip.t")
        if filesize == 0:
            print("0 zip files need to be installed: " + str(filesize))
        else:
            Write.Print(f"Installing Your zip files!", Colors.blue_to_green, interval=0.05)
            print('')
            with open(f'zip.t', 'r') as c:
                lines = c.readlines()
                for line in lines:
                    url = line
                    r = requests.get(url, allow_redirects=True)
                    t = urlparse(url).netloc
                    print ('.'.join(t.split('.')[-2:]))
                    open(f'{t}.zip', 'wb').write(r.content)
                    print(f'Successfully installed {t}.zip')
                    print('')
    install_zip()


else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)