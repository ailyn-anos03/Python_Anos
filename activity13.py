
num = eval(input(" +Enter a number to calculate: "))

# for x in range(1,11):
#     for y in range(1,10):
#         print(x * y, end="\t")


for x in range(1,11):
    for y in range(1,num + 1):
        print(f"{x} x {y} = {x + y}", end="\t")
   
    print()
