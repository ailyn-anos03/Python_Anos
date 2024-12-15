#Anos, Ailyn C. (BSIT-1B)

name = input("Enter your name : ")
age = int(input("Enter your Age: "))
pr = input("Have you purchased anything today? ( Yes | No ): ")

if pr.lower() == "yes":
    product = input("What product did you buy? ")
    price = float(input("How much does the product cost? "))
    py = float(input("Please enter the amount you will pay ---->   " ))
    
#if the price is less than 4000 the tax is 0.123 or 12.3%
    if price <= 3999:
        
        tax = price * 0.123
        taxed = tax + price 
        ch = py - taxed
        print(f"\n Hi {name}, thank you for purchasing.\n")
        print(f"\nThe added tax to your product is {tax:.2f}.")
        print(f"The taxed price of the product you purchased is {taxed:.2f}.")
        print(f"The change for your payment {py:.2f} is {ch:.2f} \n")

        
    #if the costumer is more than 60 years old the will be a 12.3% discount
        if age >= 60 and age <= 150:
                print(f"\nBecause you are already {age} years old, you will be discounted by 12.3% off \n")
                tax = price * 0.123
                taxed = tax + price 
                dis = taxed * 0.123
                ds = taxed - dis
                ch = py - ds
                print(f"{name}, your new total is summed below.\n")
                print(f"The added tax to your product is {tax:.2f}.")
                print(f"The taxed price of the product you purchased is {taxed:.2f}")
                print(f"Your discount is {dis:.2f}")
                print(f"\nThe discounted price will be {ds:.2f}")
                print(f"The change for your payment {py:.2f} is {ch:.2f} \n")
                
   #if the price is more than 4000 the tax is 0.0.038 or 3.8% 
    elif price >= 4000:
        tax = price * 0.038
        taxed = tax + price 
        ch = py - taxed
        print(f"\nHi {name}, thank you for purchasing.\n")
        print(f"The added tax to your product is {tax:.2f}")
        print(f"The taxed price of the product you purchased is {taxed:.2f}")
        print(f"The change for your payment {py:.2f} is {ch:.2f} \n")
            
         #if the costumer is more than 60 years old the will be a 12.3% discount, the difference is that the tax is 3.8% here 
        if age >= 60 and age <= 150:
                print(f"\nBecause you are already {age} years old, you will be discounted by 12.3% off\n")
                tax = price * 0.038
                taxed = tax + price 
                dis = taxed * 0.123
                ds = taxed - dis
                ch = py - ds
                print(f"{name}, your new total is summed below.\n")
                print(f"The added tax to your product is {tax:.2f}.")
                print(f"The taxed price of the product you purchased is {taxed:.2f}.")
                print(f"Your discount is {dis:.2f}")
                print(f"\nThe discounted price will be {ds:.2f}")
                print(f"The change for your payment {py:.2f} is {ch:.2f} \n")
           
                
        else:
                print("You should purchase first to use the system!")
           
   
    else:
        print("You should purchase first to use the system!")

else:
    print("You should purchase first to use the system!")