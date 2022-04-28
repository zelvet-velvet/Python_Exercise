import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

"""-----------------------------"""
#code beneath
cls()
while True:
    print("Enter a Integer between 1~1000")
    a=input()
    if a<1 or a>1000 :
        print("Please enter a number\nbetween \"1~1000\"")
        b=input()
    elif (a%2)==0 : 
        print("It is a even number.")
        b=input()
    else :
        print("It is a odd numver.")
        b=input()


    cls()



