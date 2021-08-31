import os
import random


INPUT = "C:\\Users\\rakoc\\Downloads\\deerinit\\"
OUTPUT = "C:\\Users\\rakoc\\Downloads\\deerdata\\"

for filename in os.listdir(INPUT):
    fname = ""
    for x in range(0,5):
        fname += str(random.randint(1,9))
    
    src = INPUT+filename
    dst = INPUT+fname+".jpg"
    os.rename(src,dst)