# Anos,AilynC.
# BSIT-1B



conn = True
sum = 0
even = 0
odd = 0


while conn == True:

    num = eval(input("Please Enter a number ---> "))
    if  num % 2 == 0:
          even += num
        
    elif num % 2== 1:
            odd += num 
    if num == 0:
        print("LOOP HAS ENDED ")
        print(f"The sum of all the numbers given is {odd + even}.")
        print(f"The sum of all numbers the EVEN numbers only is {even}")
        print(f"The sum of all numbers the ODD numbers only is {odd}")

        break  
        conn = False
    
        sum += num
        
        
    else:
        continue
      

      
