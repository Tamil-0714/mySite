# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:03:12 2023

@author: 22ucs626
"""

x = int(input('enter a number'))
y = int(input('enter second number'))
sum = x+y
print(f"sum of two number : {sum}")

#--------------------------------------------

x = int(input('enter a number'))
y = int(input('enter second number'))
sum = x+y
sub = x-y
div = x/y
mul = x*y
print(f"sum of two number : {sum}\n\
		difference of two number is : {sub}\n\
		Division of two number is : {sub}\n\
		product of two number is :{mul}\
	")

#--------------------------------------------	

n = int(input('enter any number'))
res = n**4
print(f"{n} to the power 4 is {res}");

#--------------------------------------------	

a = int(input('enter the length of square : '))
l = int(input('enter the length of rectangle : '))
b = int(input('enter the breath of rectangle : '))
sqa = a*a
rec = l*b
print(f"area of square : {sqa}")
print(f"area of rec : {rec}")

#--------------------------------------------	

a = int(input('enter the length of square : '))
l = int(input('enter the length of rectangle : '))
b = int(input('enter the breath of rectangle : '))
sqa = 4*a
rec = (l*2)+(b*2)
print(f"perimeter of square : {sqa}")
print(f"perimeter of rec : {rec}")

#--------------------------------------------	

x = int(input('enter a number'))
y = int(input('enter second number'))
if(x>y):
	print(f"{x} is greater than {y}")
else:
	print(f"{y} is greater than {x}")
	
#--------------------------------------------	

x = int(input('enter a number'))
y = int(input('enter second number'))
z = int(input('enter third number'))

if(x>y and x>z):
	print(f"{x} is greater than {y} and {z}")
elif(y>x and y>z):
	print(f"{y} is greater than {x} and {z}")
else:
	print(f"{z} is greater than {x} and {y}")

#--------------------------------------------	
	
x = int(input('enter a number'))
if(x%2 == 0):
	print(f"{x} is even number")
else:
	print(f"{x} is add number")

#--------------------------------------------	
	
age = int(input('enter your age'))
if(age >= 18):
	print("your are eligible for vote")
else:
	print("your are not eligible for vote")
	


#--------------------------------------------	

principal = int(input('enter the principal amount : '))
rate = int(input('enter the rate of intrest : '))
time = int(input('enter the time period in years : '))

simple_intrest = principal*rate*time
compound_intrest = principal*(pow(1+rate/100,time))-principal
print(f"simple intrest : {simple_intrest}")
print(f"compound intrest : {compound_intrest}")



http://localhost:8888/?token=ec1c1e7020235615b9a6f2fd00298f2233eba9bf2ea466a2