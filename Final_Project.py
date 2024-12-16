

import os


def activities():
    os.system('cls')
    print("\nTHIS ARE ALL OF MY ACTIVITIES\n")
    for a in range (1,21):
        print(f"{a}.) Activity {a}" )
        

def codeChallange():
    os.system('cls')
    print("\nTHIS ARE ALL OF MY CODE CHALLANGE\n")
    for b in range (1,15):
        print(f"{b}.)Code Challange {b}")
        


    

def exitAct():
    q1 = input("\nDo you want to exit? yes|no\n:")
    if q1.lower() == "yes":
           print("THANK YOU FOR CHECKING MY PROJECT")
           
           
           
           
    else:
           contin = True





     
name = input("\nEnter your name: ")
print(f"\nHi {name.upper()}, This is my Final Project\n")
    
    
contin = True
while contin == True:
        print("__________________________")
        print("DASHBOARD\n\n1.)PYTHON ACTIVITIES\n2.)PYTHON CODE CHALLANGE\n3.)EXIT")
        ch = input(" --->")
        
        if ch == "1":
    
                activities()
                act= input("\nEnter the number of the Activity you want to open:  ")
            

                if act == "1":
                        from activity1 import hello
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A PRINT MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
                                

                elif act == "2":
                        from activity2 import Hi
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A COMMENT MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "3":
                        from activity3 import name
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A SIMPLE INPUT STRUCTURE MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "4":
                        from activity4 import fh
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A FAHRENHEIT CONVERTER MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True

                elif act == "5":
                        from activity5 import x
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A USE OF ASSIGNMENT OPERATORS MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "6":
                        from activity6 import password
                        """THIS IS A PROGRAM THAT WILL SHOWS THE INTRODUCTION TO DECISION STRUCTURES MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "7":
                        from activity7 import aa
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A FOR LOOP STRUCTURE MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "8":
                        from activity8 import aa
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A FOR LOOP, IN RANGE OF 11 MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "9":
                        from activity9 import limit
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A FOR LOOP WITH FACTORIAL MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "10":
                        from activity10 import a
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A FOR LOOP TRIANGLES MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                if act == "11":
                        from activity11 import name
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A WHILE LOOP WITH A BREAK CONDITION MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "12":
                        from activity12 import x
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A FOR LOOP INVERTED TRIANGLES MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "13":
                        from activity13 import num
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A FOR LOOP STRUCTURE MULTIPLICATION TABLES MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            os.system('cls')
                            contin = True
                elif act == "14":
                        from activity14 import num
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A FOR LOOP STRUCTURE OF TRIANGLES MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "15":
                        from activity15 import con
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A WHILE LOOP CONDITIONS STRUCTURE MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "16":
                        from activity16 import tuloy
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A FOR WHILE LOOP WITH A BOOLEAN VARIABLE AND TRIGGER MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "17":

                        from activity17 import greet_Someone
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A USE OF BUILT-IN FUCTIONS OF PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "18":
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A DOCSTRING MADE FROM PYTHON"""
                        from activity18 import greet
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "19":
                        """THIS IS A PROGRAM THAT WILL SHOW YOU LISTING MADE FROM PYTHON"""
                        from activity19 import fruits
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif act == "20":
                        from activity20 import modules
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A USE OF MODULES MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True


                else:
                       print("WARNING: 1-20 ARE THE ONLY SELECTION")



        elif ch == "2":
                
                codeChallange()
                cc = input("\nEnter the number of the Code you want to open:  ")       
                
                if cc == "1":
                        from code_challange1 import hi
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A BASIC ESCAPE SEQUENCE OF PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif cc == "2":
                        from code_challange2 import name
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A ESCAPE SEQUENCE AND INPUT CODES"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif cc == "3":
                        from code_challange3 import n1
                        """THIS IS A PROGRAM THAT WILL SHOW YOU THE ARITHMETIC OPERATORS OF PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif cc == "4":
                        from code_challange4 import name
                        """THIS IS A PROGRAM THAT WILL SHOW YOU THE ARITHMETIC OPERATORS (DENOMINATION) OF PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif cc == "5":
                        from code_challange5 import name
                        """THIS IS A PROGRAM THAT WILL SHOW YOU THE RELATIONAL OPERATORS (GRADING SYSTEM) OF PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif cc == "6":
                        from code_challange6 import name
                        """THIS IS A PROGRAM THAT WILL SHOW YOU THE RELATIONAL OPERATORS (AGE ANALYSIS) OF PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif cc == "7":
                        from code_challange7 import name
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A GROCERY SIMULATOR MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                if cc == "8":
                        from code_challange8 import x
                        """THIS IS A PROGRAM THAT WILL SHOW YOU THE CALCULATION OF ODDS AND EVENS MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif cc == "9":
                        from code_challange9 import a
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A INVERTED PYRAMID MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif cc == "10":
                        from code_challange10 import a
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A PATTERNED DIAMOND (EVEN) MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif cc == "11":
                        from code_challange11 import a
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A PATTERNED DIAMOND (ODD) MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif cc == "12":
                        from code_challange12 import a
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A PATTERNED ARROW MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif cc == "13":

                        from code_challange13 import conn
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A WHILE LOOP THAT SUM'S UP ODDS AND EVENS MADE FROM PYTHON"""
                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True
                elif cc == "14":

                        from code_challange14 import con
                        """THIS IS A PROGRAM THAT WILL SHOW YOU A BANK SIMULATION MADE FROM PYTHON"""

                        q1 = input("\nDo you want to exit? yes|no\n:")
                        if q1.lower() == "yes":
                                print("THANK YOU FOR CHECKING MY PROJECT")
                                break
           
                        else:
                            contin = True

                else:
                        print("WARNING: 1-14 ARE THE ONLY SELECTION")

        elif ch == "3":
               print("________________________________")
               print(f"THANK YOU FOR CHECKING MY PROJECT {name.upper()}")
               print("The system is now CLOSED\n")
               break
            


     
