#Anos, Ailyn C. (BSIT-1B)
name = input("Please Enter your Name: ")
grade = int(input("Please input your average grade:"))

if grade >= 97:
        result = '1.00'
elif grade >= 94:
        result = '1.25'
elif grade >= 91:
        result = '1.50'
elif grade >= 88:
        result = '1.75'
elif grade >= 85:
        result ='2.00'
elif grade >= 82:
        result = '2.25'
elif grade >= 79:
        result = '2.50'
elif grade >= 76:
        result = '2.75'
elif grade >= 74:
        result = '3.00'
else:
        result = 'FAILED'


print(f"Hi {name}, The Equivalence for your Graded Average {grade} is {result}")


