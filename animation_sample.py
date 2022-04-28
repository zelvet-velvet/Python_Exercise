import os
def cls():
    os.system('clear')
cls()
import time
animation = "|/-\\"
idx = 0
print("\n\n")
while True:
    print("\t\t"+animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)
