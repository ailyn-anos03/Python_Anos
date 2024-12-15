name = input("Please Enter your Name : ")





def average(gpa):
    if gpa >= 97:
        return '1.00'
    elif gpa >= 94:
        return '1.25'
    elif gpa >= 91:
        return '1.50'
    elif gpa >= 88:
        return '1.75'
    elif gpa >= 85:
        return '2.00'
    elif gpa >= 82:
        return '2.25'
    elif gpa >= 79:
        return '2.50'
    elif gpa >= 76:
        return '2.75'
    elif gpa >= 74:
        return '3.00'
    else:
        return 'FAILED'

ave = eval(input("Enter the your average grade: "))


if 0 <= ave <= 100:
    grade = average(ave)
    print(f"Hi{name},The Equivalence for the your Graded Average {ave} is {grade}")
else:
    print("Please input your Average Grade")


