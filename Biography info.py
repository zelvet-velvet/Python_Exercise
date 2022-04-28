
import os

def cls():
    os.system('clear')


while True :
    cls()
    while True:
        print("Enter your name.")
        name=input()
        if name.find("*")==(-1):
            cls()
            break
        else:
            cls()
            print("You enter a wrong format. Enter again.")
            
        
    while True:
        print("Enter your birth day. \ne.g: 2003/03/21 enter 2003/03/21")
        bday=input()
        if bday.find("*")==(-1):
            cls()
            break
        else:
            cls()
            print("You enter a wrong format. Enter again.")
            
    while True:
        print("Enter your address.")
        addr=input()
        if addr.find("*")==(-1):
            cls()
            break
        else:
            cls()
            print("You enter a wrong format. Enter again.")
    while True:
        print("Enter your goal recently.")
        goal=input()
        if goal.find("*")==(-1):
            cls()
            break
        else:
            cls()
            print("You enter a wrong format. Enter again.")
    cls()
    print("Name:"+name+"\nBirth:"+bday+"\nAddress:"+addr+"\nGoal:"+goal)
    
    print("Press enter to continue")
    a=input()











