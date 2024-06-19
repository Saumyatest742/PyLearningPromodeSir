from math import factorial
#Find FACTROIAL of a number using function

num=int(input("Enter a number: "))
#num = 5
#Fac = 5*4*3*2*1 = 120

#fact = factorial(num)
#print(fact)
fact = 1
for a in range(1, num+1):

    fact = fact*a
print(fact)