import requests
import sys 
import os 
import time 

# Defining Required Functions 
def animation_text(text, delay):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)

def clear():
    os.system("clear")

# Logo Section
logo = """

\033[1;34m================================================

 \t\033[1;36m _____  _____ ________      _______  
 \t|  __ \\|_   |__  /\\ \\    / /_   _| 
 \t| |) | | |    / /  \\ \\  / /  | |   
 \t|  _  /  | |   / /    \\ \\/ /   | |   
 \t| | \\ \\ | | / /__    \\  /   | |  
 \t||  \\\\/|    \\/   |_| 


       \033[1;32mAuthor   : Rizvi Ahmed
       Facebook : www.facebook.com/rijuorsiam 
       Github   : www.github.com/ahmedrizvisiam
       Group    : STLP TEAM

       Use the tool for Educational Purpose

\033[1;34m================================================\033[0m
"""

first_line = """\033[1;32m
------------------------------------------------
|                                              |
|     IP Tracker Tool Presented By STLP TEAM   |
|                                              |
------------------------------------------------\n\n\033[0m"""



def animation_text(text, delay):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)


# Main Program
clear()
animation_text(logo, 0.01)
animation_text(first_line,0.01)

option = "\n\n\t\033[1;35m1. Track Location Using IP\n\n\t2. Exit\n\033[0m"

animation_text(option,0.1)


choise = int(input("\n\n\tEnter your choise : "))



if choise == 1:



    ip = input("\n\n\tEnter your ip : ")
    
    wait = ("\n\n\t\t\033[1;32mProccessing Please wait.")
    animation_text(wait,0.05)
    time.sleep(1)
    
    request = requests.get("http://ip-api.com/json/"+ip)
    
    
    txt = request.json()
    
    
    print(f"\n\n\n\033[1;33mStatus : {txt['status']}\nCountry : {txt['country']}\nCountry_Code : {txt['countryCode']}\nDivision : {txt['regionName']}\nCity : {txt['city']}\nArea Zip Code : {txt['zip']}\nInternet Provider : {txt['isp']}")
    
else:
    pass
