#Anos, Ailyn C. (BSIT-1B)
name = input("Please Enter your Name: ")
age = int(input("Enter your age:"))


if age <= 8:
        result = 'Toddler'
elif age <= 14:
        result = 'Preteen'
elif age <= 18:
        result = 'Teenager'
elif age <= 27:
        result = 'Early Adulthood'
elif age <= 44:
        result = 'Middle Age'
elif age <= 59:
        result = 'Past Adulthood'
elif age <= 80:
        result = 'Senior'
elif age <= 90:
        result = 'Congratulation on reaching that age'
elif age <= 100:
        result = 'Congratulations, you are a healthy person'


print(f"Hi {name}, {result} at age of {age}")