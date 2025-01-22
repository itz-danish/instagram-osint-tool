import sys
import os
from instagrapi import Client
import banner,menu,login


#function to clear the terminal
def clear_terminal():
    os.system('cls' if sys.platform == 'win32' else 'clear')

#using UTF-8 encoding to handle printing emojis
sys.stdout.reconfigure(encoding='utf-8')

#clearing terminal before starting the tool
clear_terminal()

#printing top banner
print(f"{banner.head()}")

#defining session file
SESSION_FILE = 'session.pkl'

session_found= False
#check for previous session file
if os.path.exists(SESSION_FILE):
    session_found=True
    Login_menu='''\033[33m--- You must Login to continue using this tool (use temporary account) ---\033[0m
      \033[36mAn old session file is found!\033[0m
      
      please choose an option:
      1. Use previouly saved session file to login
      2. Login with a new account
      3. Exit'''
else:
    Login_menu='''\033[33m--- You must Login to continue using this tool (use temporary account) ---\033[0m
      please choose an option:
      1. Login with a new account
      2. Exit'''

cl = login.login(Login_menu, session_found, SESSION_FILE, Client)
input("Press ENTER to continue...")

folder_path = "target_dump"
if not os.path.exists(folder_path):
    # Create the folder
    os.makedirs(folder_path)

#entering the taget's username
clear_terminal()
print(banner.head())
target_username=input("\033[33mEnter the username of target(eg. _target_username_): @\033[0m")

#remove spaces and @ in cases of mistake
target_username=target_username.replace(" ","")
target_username=target_username.replace("@","")

#data dump folder path for the target
target_folder="target_dump/"+target_username

#creating an folder for the target if it doesn't exists
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

#main menu iv- for invalid previous input in main menu
menu.main_menu(cl, target_username,sys,target_folder,iv=False)