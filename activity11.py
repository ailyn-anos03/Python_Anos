
isRepeat = True

while isRepeat == True:
    name = input("Enter a Name: ")
    print(f"Hi {name}")

    if name.lower() == "ailyn":
        print("LOOP TERMINATED")
        isRepeat = False
        break