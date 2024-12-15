
num = eval(input("Enter no. of right triangles: "))

for x in range(0,6):
    for x in range(0, num):
        for y in range(1, x +1):
            print("*", end=" ")
        for a in range(6, x, -1):
            print(" ", end= " ")
        print(end=" ")
    print()
        