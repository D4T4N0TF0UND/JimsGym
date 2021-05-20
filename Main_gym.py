# a login system and user database for jim's gym with multiple functions
# functions:  3 memebership levels, silver gold and plat
# password and username database, password verification, password must have at least 8 chars(use len function)
# be able to print a list of customers using each membership(use finduser function from prev program, modify for multiple users)
# quit program function. (import sys and use sys.exit())


#import essential modules

from sys import *

#define variables

current_account = "failed"
global logged_in
logged_in = False
#current_account tells the program who, if anyone is logged on. in an actual scenario this is horribly insecure, and would likely be handled on a server instead of a client, along with the user database.


#management program

def control():
    global logged_in
    global current_account
    first_loop = True
    while True:
        if first_loop == True:       # different options if logged in, and a welcome message
            print("Welcome to Jim's Gym!")
            print("Please choose an option.")
            print("A: register an account")
            print("B: log into an account")
            print("C: print a list of users")
            print("D: print a list of users of a certain type")
            print("X/alt+F4: quit program")
            mainChoice = input()
            
            if mainChoice in ["A", "a"]:
                register_acc()
            
            elif mainChoice in ["B", "b"]:
                getUser()
            
            elif mainChoice in ["C", "c"]:
                user_list()
            
            elif mainChoice in ["D", "d"]:
                spec_user_list()
            
            elif mainChoice in ["X", "x"]:
                exit()
            
            first_loop = False
        
        elif first_loop == False and logged_in == False:      # different options if logged in, and a welcome message
            print("Please choose an option.")
            print("A: register an account")
            print("B: log into an account")
            print("C: print a list of users")
            print("D: print a list of users of a certain type")
            print("X/alt+F4: quit program")
            mainChoice = input()
            
            if mainChoice in ["A", "a"]:
                register_acc()
            
            elif mainChoice in ["B", "b"]:
                getUser()
            
            elif mainChoice in ["C", "c"]:
                user_list()
            
            elif mainChoice in ["D", "d"]:
                spec_user_list()
            
            elif mainChoice in ["X", "x"]:
                exit()
        
        elif logged_in == True and first_loop == False:                # different options if logged in, and a welcome message
            print("Please choose an option.")
            print("A: view membership level")
            print("B: change membership level")
            print("C: print a list of users")
            print("D: print a list of users of a certain type")
            print("E: log out")
            print("X/alt+F4: quit program")
            mainChoice = input()
            
            if mainChoice in ["A", "a"]:
                showDetails()
            
            elif mainChoice in ["B", "b"]:
                changeDetails()
            
            elif mainChoice in ["C", "c"]:
                user_list()
            
            elif mainChoice in ["D", "d"]:
                spec_user_list()
            
            elif mainChoice in ["E", "e"]:
                logged_in = False
                current_account = "failed"    # resets variables that tell the program the user is logged in
            
            elif mainChoice in ["X", "x"]:
                exit()
        
        

#register an account by getting details and writing them to a .txt file

def register_acc():
    goodPass = False
    goodMemb = False
    while goodPass == False:
        good_user = False
        while good_user == False:    # checks to see if the chosen username is taken, runs until a free username is detected
            print("please choose a username")
            new_user = input()
            textFile = open("user_cache.txt", "r")
            all_lines = textFile.readlines()
            stripped_all_lines = []
            for element in all_lines:    # for each item in the list containing all names, passwords and levels, removes trailing newline(\n)
                stripped_all_lines.append(element.strip())
            if new_user in stripped_all_lines:    # checks if chosen username is in the list
                print("sorry, that username is taken, please try again")
            else:
                good_user = True  # confirms that the program may continue
        print("please choose a password longer than 8 characters")
        new_pass = input()
        if len(new_pass) <= 7:
            print("password must be 8 or more characters")
        else:
            print("password succesful!")
            goodPass = True     # allows the program to continue
    while goodMemb == False:
        print("please choose a membership level")
        print("S: silver")
        print("G: gold")
        print("P: platinum")
        #check which choice is made
        membChoice = input()
        if membChoice in ["S", "s"]:
            yN = input("silver costs £10 a month, is that ok?[y/n]")
            new_memb = "silver"
        elif membChoice in ["G", "g"]:
            yN = input("gold costs £20 a month, is that ok?[y/n]")
            new_memb = "gold"
        elif membChoice in ["P", "p"]:
            yN = input("platinum costs £30 a month, is that ok?[y/n]")
            new_memb = "platinum"
        else:
            print("input not recognised, please try again")
        
        #looks at if customer agrees with price
        if yN in ["Y", "y"]:
            goodMemb = True
            print("welcome to Jim's Gym!")
    textFile = open("user_cache.txt", "a")
    textFile.write("\n")
    textFile.write(new_user)
    textFile.write("\n")
    textFile.write(new_pass)
    textFile.write("\n")
    textFile.write(new_memb)
    textFile.close()


#login system finds given name in db, looks one line down to find password
#main code for logging in
def getUser():
    global current_account
    global correct_pass
    global name_true
    print("please enter your username")
    log_in_name = input()
    findUser(log_in_name)
    if found_username == 0:
        print("user not found")
        current_account = "failed"
    else:
        print("hi", log_in_name, "welcome!")
    testPass()

#search database for given name
def findUser(name_to_find):
    line_number = 0
    global found_username
    found_username = 0
    with open("user_cache.txt", "r") as read_obj:
        for line in read_obj:
            line_number += 1
            if name_to_find in line:
                found_username = line_number
                current_account_name = name_to_find
    return int(found_username)

#checks if password is correct for given name and if succesful saves the current logged in account to the variable current_account
def testPass():
    global current_account
    global logged_in
    global correct_pass
    print("please enter your password")
    textFile = open("user_cache.txt", "r")
    all_lines = textFile.readlines()
    global correct_pass
    correct_pass = all_lines[found_username]
    correct_pass = correct_pass.rstrip("\n")
    correct_pass = correct_pass.rstrip()
    attempted_pass = input()
    if attempted_pass == correct_pass:
        current_account = found_username
        print("password correct")
        logged_in = True
    else:
        print("wrong")
        current_account = "failed"
    return current_account
    
#finds the current user's membership level by looking at the line 2 below the int value of the current_account variable    

def showDetails():
    global current_account
    textFile = open("user_cache.txt", "r")
    all_lines = textFile.readlines()
    details = all_lines[current_account + 1]
    print(details)



def changeDetails():
    global current_account
    goodMemb = False
    while goodMemb == False:
        print("please choose a membership level")
        print("S: silver")
        print("G: gold")
        print("P: platinum")
        #check which choice is made
        membChoice = input()
        if membChoice in ["S", "s"]:
            yN = input("silver costs £10 a month, is that ok?[y/n]")
            new_memb = "silver"
        elif membChoice in ["G", "g"]:
            yN = input("gold costs £20 a month, is that ok?[y/n]")
            new_memb = "gold"
        elif membChoice in ["P", "p"]:
            yN = input("platinum costs £30 a month, is that ok?[y/n]")
            new_memb = "platinum"
        else:
            print("input not recognised, please try again")
        
        #looks at if customer agrees with price
        if yN in ["Y", "y"]:
            goodMemb = True
    num_line = current_account + 1
    lines = open("user_cache.txt").read().splitlines()
    lines[num_line] = new_memb
    open("user_cache.txt", "w").write("\n".join(lines))

#starting at the first line this function calculates the amount of users registered, and then looks at every third line until it knows there are no users left. it then assigns each user to its own object in a list and prints the list, after some formatting like removing trailing newlines

def user_list():
    users_list = []
    textFile = open("user_cache.txt", "r")
    all_lines = textFile.readlines()
    current_line = 1
    num_of_lines = len(all_lines)/3   #  calculates amount of users
    for num in range(int(num_of_lines)):   #repeats the amount of users regeistered
        user_to_format = all_lines[current_line]   #assign a username to the variable user_to_format
        user_to_format = user_to_format.rstrip("\n")   # removes trailing newline from user_to_format
        users_list.append(user_to_format)    #   adds formatted username to list
        current_line = current_line + 3      #looks for next username
    print(str(users_list))   #   prints list of users


#print list of users of a specific membership level

def spec_user_list():

    
    rec_input = False
    while rec_input == False:
        print("what level of membership do you want to search for?")
        print("silver(s), gold(g) or platinum(p)?")
        chos_memb = input()
        if chos_memb in ["Silver", "silver", "SILVER", "S", "s"]:
            chos_memb = "silver"
            rec_input = True
        elif chos_memb in ["Gold", "gold", "GOLD", "g", "G"]:
            chos_memb = "gold"
            rec_input = True
        elif chos_memb in ["Platinum", "platinum", "PLATINUM", "P", "p"]:
            chos_memb = "platinum"
            rec_input = True
        else:
            print("membership level not recognised, please try again")
    users_list = []
    textFile = open("user_cache.txt", "r")
    all_lines = textFile.readlines()
    current_line = 1
    num_of_lines = len(all_lines)/3   #  calculates amount of users
    for num in range(int(num_of_lines)):   #repeats the amount of users regeistered
        user_to_format = all_lines[current_line]        #assign a username to the variable user_to_format
        memb_lev = all_lines[current_line + 2]
        user_to_format = user_to_format.rstrip("\n")   # removes trailing newline from user_to_format
        memb_lev = memb_lev.rstrip("\n")    #removes trailing newlines and spaces from the specific membership level
        memb_lev = memb_lev.rstrip(" ")
        if memb_lev == chos_memb:
            users_list.append(user_to_format)    #   adds formatted username to list
        current_line = current_line + 3      #looks for next username
    print(str(users_list))   #   prints list of users


control()