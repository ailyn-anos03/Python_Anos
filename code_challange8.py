# Anos,AilynC.
# BSIT-1B



sum = 0
odd = 0
even = 0

for x in range(1,11):
    num = eval(input(f"Enter #{x} ---> "))
    sum += num

    if num % 2 == 0:
        even += num 
    else:
        odd += num 

print(f"The sum of all numbers given is {sum}")
print(f"The sum of all numbers the EVEN numbers only is {even}")
print(f"The sum of all numbers the ODD numbers only is {odd}")