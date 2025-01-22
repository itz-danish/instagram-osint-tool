import os
import sys
import pickle
def login(Login_menu, session_found, SESSION_FILE, Client):
    print(Login_menu,)
    if session_found:

        entry=input("      ")
        #check for empty selecetion
        if len(entry)==0:
            print("\033[31mInvalid selection!\033[0m")
            sys.exit()

        #for entry 1. while session file is found
        elif entry[0] == "1":
            with open(SESSION_FILE, 'rb') as f:
                try:
                    cl = pickle.load(f)
                    print("\033[32mlogged in sucessfully using previous session... ;)\033[0m")
                    return cl
                except:
                    print("An error occured while login using session file...\nif it persist kindly use < 2.  Login with a new account >")
        #for entry 2.
        elif entry[0] == "2":
            #delete previous session file
            os.remove(SESSION_FILE)
            cl = Client()

            #username
            username=input("Please enter the username to login: ")
            #password
            password=input("Please enter the password to login: ")

            try:
                cl.login(username, password)
                print("\033[32mLogged in successfully... ;)\033[0m")
                with open(SESSION_FILE, 'wb') as f:
                    pickle.dump(cl, f)
                return cl
            except:
                print("\033[31mAn error while login... Please check your username and password!\033[0m")
                sys.exit()

        #when entry is 3
        elif entry[0] == "3":
            sys.exit()

        #when entry is invalid
        else:
            print("\033[31mInvalid selection!\033[0m")
            sys.exit()

    #when session file is not found        
    else:
        entry=input("      ")

        #check for empty selecetion
        if len(entry)==0:
            print("\033[31mInvalid selection!\033[0m")
            sys.exit()

        #for entry 1.
        if entry[0] == "1":

            cl = Client()

            #username
            username=input("Please enter the username to login: ")
            #password
            password=input("Please enter the password to login: ")
            print("Initiating Login process... Please wait...")

            try:
                cl.login(username, password)
                print("\033[32mLogged in successfully... ;)\033[0m")
                with open(SESSION_FILE, 'wb') as f:
                    pickle.dump(cl, f)
                return cl
            except:
                print("\033[31mAn error while login... Please check your username and password!\033[0m")
                sys.exit()
        #for entry 2
        elif entry[0] == "2":
            sys.exit()
        #for invalid entry
        else:
            print("\033[31mInvalid selection!\033[0m")
            sys.exit()
    
