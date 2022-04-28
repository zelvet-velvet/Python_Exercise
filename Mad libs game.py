
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while True:
    cls()
    N1=input("Who?: ")
    N2=input("Where?: ")
    N3=input("Using what?:")
    N4=input("To what?: ")
    N5=input("Why?: ")
    cls()
    a="\tOnce upon of time, {}, a bixxx who was be known as a toxic mouth. He lived in {}. \n\tOne day he took a {} on his hand. {} was going to {}, since {}. Than, he died, since he was too toxic."

    print(a.format(("\033[1;32m"+N1+"\033[1;0m"),"\033[1;32m"+N2+"\033[1;0m","\033[1;32m"+N3+"\033[1;0m","\033[1;0m"+N1+"\033[1;0m","\033[1;32m"+N4+"\033[1;0m","\033[1;32m"+N5+"\033[1;0m"))
    c=raw_input("\n\n  (Press enter to restart.)")

