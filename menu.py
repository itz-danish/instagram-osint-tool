from main_menu import *
import banner
import os
def display_menu():
    print('''\033[33m--- Main menu ---\033[0m
1. Basic Profile Information(eg. Name, bio, Followers Count)
2. List of followings
3. List of followers
4. Posts data
5. Exit
''')

def main_menu(cl,target_username,sys,target_folder,iv):

    os.system('cls' if sys.platform == 'win32' else 'clear')
    print(banner.head())

    #display the main menu selction list
    display_menu()

    #for invalid previous input
    if iv:
        print("\033[31mInvalid selection! Please try again...\033[0m")
    entry=input("Select an option from above: ")
    #check for empty selecetion
    if len(entry)==0:
        print("\033[31mInvalid selection!\033[0m")
        main_menu(cl,target_username,sys,target_folder,iv=True)
    
    #for basic profile info
    elif entry[0]=="1":
        print("Data extraction has started... Please wait...")
        basic_info.extract_basic_data(cl,target_username,target_folder,sys)

        #return to main menu
        main_menu(cl,target_username,sys,target_folder,iv=False)
    
    #for followings
    elif entry[0]=="2":
        #max_limit
        limit=input("Enter the max. number of followings to scrape (Recomended 200): ")
        limit=limit.replace(" ","")
        try:
            limit=int(limit)
        except:
            print("Invalid input! Limit set to default 200.")
            limit=200
        
        print("Data extraction has started... Please wait...")
        followings.extract_followings(cl,target_username,target_folder,sys,limit)
        
        #return to main menu
        main_menu(cl,target_username,sys,target_folder,iv=False)

    #for following
    elif entry[0]=="3":
        #max_limit
        limit=input("Enter the max. number of followers to scrape (Recomended 200): ")
        limit=limit.replace(" ","")
        try:
            limit=int(limit)
        except:
            print("Invalid input! Limit set to default 200.")
            limit=200

        followers.extract_followers(cl, target_username, target_folder, sys, limit)

        #return to main menu
        main_menu(cl,target_username,sys,target_folder,iv=False)

    #for posts data
    elif entry[0]=="4":
        print("Data extraction has started... Please wait...")
        posts.extract_posts_data(cl, target_username, target_folder, sys)

        #return to main menu
        main_menu(cl,target_username,sys,target_folder,iv=False)


    #for exit
    elif entry[0]=="5":
        sys.exit()

    #when entry is invalid
    else:
        print("\033[31mInvalid selection!\033[0m")
        #return to main menu
        main_menu(cl,target_username,sys,target_folder,iv=True)
        
