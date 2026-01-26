import math
a = int(input("Enter first num : "))
b = int(input("Enter second num : "))
c = int(input("Enter third num : "))

if a+b>c and b+c>a and a+c>b:
s = (a+b+c)/2
area = s*(s-a)*(s-b)*(s-c)

print("Area of triangle using heron's formula : %.2f\n"% math.sqrt(area))
else:
printf("Triangle is not valid
