import math


a=int(input("value_1:"))
b=int(input("value_2:"))
c=int(input("value_3:"))

s =(a+b+c)/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)
