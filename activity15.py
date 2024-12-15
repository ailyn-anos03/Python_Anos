# Anos, Ailyn C.
# BSIT-1B

import os 

con = True
nt = 0   #number of triangles

while con == True :
    ask = input("Do you wish to add triangle/s (yes or no) --->  ")

    if ask.lower() == "no":
        print("LOOP HAS ENDED")
        break
        con = False

    elif ask.lower() == "yes":
        os.system('cls')
        nt += 1
        for x in range (1, 6):
            for h in range(1, nt + 1):
                for y in range(1,x + 1):
                    print("•", end=" ")
                for z in range(6, x, -1):
                    print(" ", end=" ")
                print(end=" ")
            print()
        continue
    else:
        print("INVALID SELECTION")
        print("Please type YES or NO! ")
