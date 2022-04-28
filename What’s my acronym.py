import os

def cls():
    os.system('clear')

while True:
    cls()
    print("Enter a sentence you want to transfer into acronym:")  
    st=input()
    x=st.split()
    cls()
    print("What you want is:\n")
    for s in x:
        print(s[0].capitalize(), end='')
    print("\n\nPress enter to continue.")
    c=input()




















