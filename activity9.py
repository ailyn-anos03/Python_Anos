# for x in range(1,16,4):
#     print(x)

# for y in range (11,1, -1):
#     print(y)

limit = eval(input("Enter a Number: "))
factorial  = 1



for z in range (limit, 0, -1):
    factorial *= z

print(f"The factorial of number {limit} is {factorial}")