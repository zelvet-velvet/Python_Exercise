import os 

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while True:
    cls()
    print("Que tal? ")
    a=input()
    print("You use "+str(len(a.replace(" ","")))+" words to discribe your feeling.030")
    b=input()
    print("  (Press enter to restart.)")
    b=input()
