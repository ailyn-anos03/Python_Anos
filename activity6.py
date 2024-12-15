#introduction to decision structures

password = "secret"
passw = "hello"

mypass= input("Enter Password: ")

if password ==mypass.lower():
    print("Access Granted")
    print("Welcome User")

elif password == passw.lower():
    print("Access Granted")
    print("Welcome to the System")

else:
    print("Incorrect Password")
    print("Access Denied")
    