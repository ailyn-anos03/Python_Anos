name = input("Hi, Please Enter your Name : ")
money = eval(input("Enter Amount to Deposit : "))

a = money // 1000
aa= money % 1000

b= aa // 500
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

print(f"Hi {name}, the total denomination of your money is; \n") 

print(a, "-1000")
print(b, "-500")
print(c, "-200")
print(d, "-100")
print(e, "-50")
print(f, "-20")
print(g, "-10")
print(h, "-1")

