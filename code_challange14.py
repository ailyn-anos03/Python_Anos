# Anos, Ailyn C.
# BSIT-1B
# Bank Simulator


import os
total = 0

bal = 0 

def overall_den():

    print("\nThis is your current bank money denomination\n")
    print("0", "-1000") 
    print("0", "-500")
    print("0", "-200")
    print("0", "-100")
    print("0", "-50")
    print("0", "-20")
    print("0", "-10")
    print("0", "-1")

def fil_denom():   
    
    a = total // 1000
    aa= total % 1000

    b = aa // 500
    bb= aa % 500

    c = bb // 200
    cc= bb % 200

    d = cc // 100
    dd = cc % 100

    e = dd // 50
    ee = dd % 50

    f = ee // 20
    ff = ee % 20

    g = ff // 10
    gg = ff % 10

    h = gg // 1
    hh = gg % 1

    print(f"\nHi {nm}, the new total denomination of your money is ₱{total}\n") 

    print(a, "-1000")
    print(b, "-500")
    print(c, "-200")
    print(d, "-100")
    print(e, "-50")
    print(f, "-20")
    print(g, "-10")
    print(h, "-1\n\n")

con = True  
while con == True: 
    print("Welcome to bank simulation")
    num = input("\nDo you wish to create an account?    yes|no  ")
    
    if num.lower()== "no": 
        
        print("LOGGED OUT")
        break
        conn = False
        

    else:
        
        nm = input("Please Enter your Account Name ---->  ")
        print(f"Welsome {nm}")
        sum = int(input("Enter the amount of your initial deposit ---->  "))
        total += sum
        print(f"You successfully deposited ₱{sum}! Your account's current balance is : ₱{total}.\n")
        fil_denom()
       

        # qa = total // 1000
        # aa= total % 1000

        # qb = aa // 500
        # bb= aa % 500

        # qc = bb // 200
        # cc= bb % 200

        # qd = cc // 100
        # dd = cc % 100

        # qe = dd // 50
        # ee = dd % 50

        # qf = ee // 20
        # ff = ee % 20

        # qg = ff // 10
        # gg = ff % 10

        # qh = gg // 1
        # hh = gg % 1

        # print(qa, "-1000")
        # print(qb, "-500")
        # print(qc, "-200")
        # print(qd, "-100")
        # print(qe, "-50")
        # print(qf, "-20")
        # print(qg, "-10")
        # print(qh, "-1")
     
        print("\n\nDo you wish to continue?\nPress ENTER key to continue\nType NO to stop  ")


        conn = True
        while conn == True:
            choice = input("---->  ")
            if choice.lower() == "no":
                print("Bank Simulation Closed")
               
                break 
                conn == False
                con == False
            ch = True
            while ch == True:
                
                print("\n\n1 -- Deposit")
                print("2 -- Withdraw")
                print("3 -- Check Balance")
                print("4 -- EXIT")
                choose = input("----> ")
                os.system('cls')
                if choose == "1":
                    

                    depo = True
                    while depo == True :
                        deposit = eval(input("Enter the amount you will deposit ----> "))
                        total += deposit
                        print(f"You successfully deposited an amount of ₱{deposit}. Your new account balance is : ₱{total}.\n")
                        fil_denom()
                        # wa = total // 1000
                        # aa= total % 1000

                        # wb = aa // 500
                        # bb= aa % 500

                        # wc = bb // 200
                        # cc= bb % 200

                        # wd = cc // 100
                        # dd = cc % 100

                        # we = dd // 50
                        # ee = dd % 50

                        # wf = ee // 20
                        # ff = ee % 20

                        # wg = ff // 10
                        # gg = ff % 10

                        # wh = gg // 1
                        # hh = gg % 1

                        # print(wa, "-1000")
                        # print(wb, "-500")
                        # print(wc, "-200")
                        # print(wd, "-100")
                        # print(we, "-50")
                        # print(wf, "-20")
                        # print(wg, "-10")
                        # print(wh, "-1")
                        again = True
                        while again == True:
                                
                                print("Press 1 if you wish Deposit Again\nPress 2 if you want to Exit")
                                cont = input("----> ")
                                if cont == "1":
                                    os.system('cls')
                                    break
                                elif cont == "2":
                                    os.system('cls')
                                    depo = False
                                    again = False
                                else :
                                    os.system('cls')
                                    print("ERROR, Please choose between 1 and 2 only!")
                                    continue
                elif choose == "2":
                   
                    print(f"Your current balance is ₱{total}") 
                    withdraw = eval(input("Enter the amount you want to withdraw ---->  "))
                     
                    if withdraw <= total:
                        print(f"Withdrawal Successful, You have withdrawn ₱{withdraw} from your account.")
                        total -= withdraw  
                        fil_denom()
                        
                    elif withdraw > total :
                        print("\n\nInsufficient Balance! Please try again.")
                        

                     
                        # ra = sum // 1000
                        # aa= sum % 1000

                        # rb = aa // 500
                        # bb= aa % 500

                        # rc = bb // 200
                        # cc= bb % 200

                        # rd = cc // 100
                        # dd = cc % 100

                        # re = dd // 50
                        # ee = dd % 50

                        # rf = ee // 20
                        # ff = ee % 20

                        # rg = ff // 10
                        # gg = ff % 10

                        # rh = gg // 1
                        # hh = gg % 1

                        # print(ra, "-1000")
                        # print(rb, "-500")
                        # print(rc, "-200")
                        # print(rd, "-100")
                        # print(re, "-50")
                        # print(rf, "-20")
                        # print(rg, "-10")
                        # print(rh, "-1")


                elif choose == "3":
                      print(f"Your current account balance is, ₱{total}")
                      fil_denom()
                      
                elif choose == "4":
                      print("The Bank Simulation is now Closed")
                      break
                      conn = False
                else :
                    
                    print("ERROR, Please select from 1 - 4 only!")
                    break

          


            
