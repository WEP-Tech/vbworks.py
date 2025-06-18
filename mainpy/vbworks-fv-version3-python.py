# VB WORKS Dev mode - not for public

#Unless you are a programmer, please don't look at the code. It ruins some minigames...
#This is available on KhanAcademy.org  & Github too! (I would like it if somebody remixed and made this into a better project)

admin_id = 'SD7Jf0 + UF9r'
import time
import random
from time import sleep 

#Problem: Does not save password and username after creation
#Code: Copyright, (C) 2025 The Ruki Company
#Domain name example.com is not mine.
# I don't know why but I put variables for Sng and Lg
#I DONT HAVE ANY GOOD IDEAS AHHHHHHHH

sng = "sng"
lg = "lg"
version = "v3" + ' Full Version - DEVLOPER MODE'

print("Welcome to VBWORKS " + version + " (DEVELOPER MODE NOT FOR PUBLIC)")
print("Copyright, (C) 2025 WEP Technoligies, commAn Tech (REGD: SD7Jf0 + UF9r)")
print("")
print("Connecting to system...")
time.sleep(5)
print("Loading libraries...")
time.sleep(5)
print(" ")
print("Registration Process...")
time.sleep(2)
Registration = input("Login (If sign up type sng and hit enter if not "+
                         "type lg and hit enter) ")
#sng reged
if Registration == sng:
    print("Sign up process...")
    time.sleep(2)
    nme_usrsmg = input("Name:")
    age_usrsmg = input("Age:")
    dmy_usrsmg = input("Date of Birth (D/M/Y): ")
    print("")
    print("Account Creation")
    usr_namesmg = input("Username: ")
    email_global = print("Your email is " + usr_namesmg + "@example.com")
    password_acc = input("Choose a password: ")
    print("Account created! ")
    print("Welcome " + nme_usrsmg)

#LG REgistration
if Registration == lg:
    print("Log in")
    email_lg = input("Email: ")
    password_lg = input("Password: ")
    name_lg = input("Name: ")
    print("Loading...")
    time.sleep(5)
    print("Welcome back " + name_lg)

print("")
ask_user_what = input("What do you want to do? "
+ "DocTyper, New Post, Game, Practice Sentences, The Database (Game 2)")

if ask_user_what == "DocTyper":
    print("Connecting to DOCTYPER SYSTEM...")
    time.sleep(5)
    print("Libraries...")
    time.sleep
    print("Type a document: ")
    title = input("Title of document: ")
    doctyped = input("Type your document here: ")
    saveorno = input("Do you want to save your document? ")
    no = "no"
    NO = "NO"
    yes = "yes"
    YES = "YES"
    if saveorno == no:
        aresure = input("Ok. Are you sure?: ")
    if saveorno == NO:
        aresure = input("Ok. Are you sure?: ")
    if saveorno == YES:
        print("Ok.")
    if saveorno == yes:
        print("Ok.")
    print("Create a value to be stored in the computer")
    val1 = input("1. ")
    val2 = input("2. ")
    val3 = input("3. ")
    
    input("Hit enter when information is needed: ")
    print(val1)
    print(val2)
    print(val3)
    
    print("Thank you for chosing Document Typer" + " " + version)

if ask_user_what == "doc typer":
    print("Type a document: ")
    title = input("Title of document: ")
    doctyped = input("Type your document here: ")
    saveorno = input("Do you want to save your document? ")
    no = "no"
    NO = "NO"
    yes = "yes"
    YES = "YES"
    if saveorno == no:
        aresure = input("Ok. Are you sure?: ")
    if saveorno == NO:
        aresure = input("Ok. Are you sure?: ")
    if saveorno == YES:
        print("Ok.")
    if saveorno == yes:
        print("Ok.")
    print("Create a value to be stored in the computer")
    val1 = input("1. ")
    val2 = input("2. ")
    val3 = input("3. ")
    
    input("Hit enter when information is needed: ")
    print(val1)
    print(val2)
    print(val3)
    
    print("Thank you for chosing DOCTYPER")
    
if ask_user_what == "doctyper":
    print("Type a document: ")
    title = input("Title of document: ")
    doctyped = input("Type your document here: ")
    saveorno = input("Do you want to save your document? ")
    no = "no"
    NO = "NO"
    yes = "yes"
    YES = "YES"
    if saveorno == no:
        aresure = input("Ok. Are you sure?: ")
    if saveorno == NO:
        aresure = input("Ok. Are you sure?: ")
    if saveorno == YES:
        print("Ok.")
    if saveorno == yes:
        print("Ok.")
    print("Create a value to be stored in the computer")
    val1 = input("1. ")
    val2 = input("2. ")
    val3 = input("3. ")
    
    input("Hit enter when information is needed: ")
    print(val1)
    print(val2)
    print(val3)
    
    print("Thank you for chosing Document Typer" + " " + version)

if ask_user_what == "New Post":
    input("Name of post:")
    input("Type here:")
    print("")
    print("PUBLISHING")
    private_public = input("Private or Public? (pr for private " 
                           + "and pb for public)")
    if private_public == "pb":
        print("Post is public")
    
    if private_public == "pr":
        print("Post is private")

    print("")

if ask_user_what == "new post":
    input("Name of post:")
    input("Type here:")
    print("")
    print("PUBLISHING")
    private_public = input("Private or Public? (pr for private " 
                           + "and pb for public)")
    if private_public == "pb":
        print("Post is public")
    
    if private_public == "pr":
        print("Post is private")

    print("")

if ask_user_what == "Game":
    numberSecret = random.randint(1, 10)
    atempt = input("Guess the number from 1-10: ")
    if atempt == numberSecret:
        print("You won!")
    else:
        print("Sorry! You lose the correct number is " + str(numberSecret))
        


if ask_user_what == 'admin': 
    #this is a dependency . 
    consoleVer = '1.2.1'
    #Dependency 1
    admin_id = 'SD7Jf0 + UF9r'
    def adminGame(): 
        type_the_fll = 'OFDJ56'
        print("Hello Admin! Let's check if you're actually an admin!")
        admin_id_check = input("Enter your ADMIN ID: ")
        if admin_id_check == admin_id:
            print(' ')
            print('Ok looks like you need to verify if you are a robot!')
            type_the_following = input('Type the following : OFDJ56 ')
            if type_the_following == type_the_fll:
                print('You have succeed, redirecting to ADMIN CONSOLE')
                print(' ')
                print('CONSOLE')
                console = input('(Type /help to start console) > ')
                if console == '/help':
                    print('List of commands')
                    print('/data - Provides console info')
                    print('/logout - Log out of the admin console easily')
                    print('/minigames - Play some minigames (not added to vbworks yet.)')
                    print('Starting console...')
                    inpu1 = input('> ')
                    if inpu1 == '/data':
                        print('CONSOLE Ver' + consoleVer)
                        updte1 = input('Found new update. Want to install it? (y / n) ')
                        if updte1 == 'n':
                            print('Ok.')
                        if updte1 == 'y':
                            print('Installing...')
                            time.sleep(5)
                            print('Restarting console...')
                            print('< --------- Loading ---------- >')
                            print('Welcome back!')
                    if inpu1 == '/logout':
                        print('Logging out...')
                        time.sleep(5)
        else:
            print('Incorrect id. ERROR CODE : IW283')
            time.sleep(2)
            print('Logging you out for security reasons')
            print('Logging out')
            time.sleep(2)
            print('Logged out!')
    adminGame()
if ask_user_what == 'practice sentences':
    print("PRACTICE SENTENCES (Hit enter to skip)")
    print("New added everyday!")
    sent1 = print("The sun was bright, filled with the orange color. " + 
          "Samuel was astonished and loved the orange color")
    input("A. ")
    print("I love butter. Butter is good on bread, it is creamy and juicy. ")
    input("A. ")
    print(" ")
    print('Thanks for using PRTYPER')

if ask_user_what == 'the database' and 'the database game' and 'thedatabase':
    def helpg():
        print("LIST OF FUNCTIONS:")
        print("/chtgrp | See Chat Group.")
        print("/str | Store a value")
        print("/hack.admin | Hacks a random person")
        print("/help | For list of functions")

    def hack():
        print("Hacking....")
        sleep(7)
        print("Hacked.")

    def chat():
        print("@them2749: Hey let's hack @cakelover45")
        sleep(3)
        print("@thehacker: OKK")
        sleep(2)
        print("@cakelover45: What are u guys doin")
        sleep(3)
        print("@thehacker: nothin")

    def sstr():
        print("What value is to be stored:")
        str1 = input("1... ")
        str2 = input("2... ")
        str3 = input("3... ")
        input("Click enter when needed: ")
        print(str1)
        print(str2)
        print(str3)

    def attacked():
        print("1. Launch a nuke")
        print("2. Sabotage your team and help the others")
        #cntinue later

    # Actual code :) 

    first = input("> (Type /help for help) ")
        
    if first == "/help":
        helpg()
        
    if first == "/hack.admin":
        hack()
        
    if first == "/str":
        sstr()
        
    if first == "/chtgrp":
        chat()
    
    second = input("> (Type /help for help) ")
        
    if second == "/help":
        helpg()
        
    if second == "/hack.admin":
        hack()
        
    if second == "/str":
        sstr()
        
    if second == "/chtgrp":
        chat()
    
    three = input("> (Type /help for help) ")
        
    if three == "/help":
        helpg()
        
    if three == "/hack.admin":
        hack()
        
    if three == "/str":
        sstr()
        
    if three == "/chtgrp":
        chat()

    print("Oh NO a country is atacking your teritory look at the following" 
      + " options")
    attacked()
    ans = input("(1/2)")
    if ans == "1":
        print("You became loyal to your teritory GAME ENDING : LOYAL ENDING")
    if ans == "2":
        print('You have a few options!')
        print(' NOTE : THIS IS BETA AND THERE IS NOTHING AFTER THIS.')

# Copyright, (C) 2025 WEP Tech, commAn Tech 
# Bug : VS Code is not importing Admin Game do I added it to the file and the whole admin feature is not working
#Bug fixed. But can't import. 
# Dev note : Thanks for all the people using VBWORKS. Im so grateful.
# idk i was bored
#Bug Admin 1
