import math
a = 6
b = 7
c = 8

if a+b>c and b+c>a and a+c>b :
 s = (a+b+c)/2
 g = s*((s-a)*(s-b)*(s-c))
 area = math.sqrt(g)
 print("Area of triangle = %.2f" % area)

else:
 print("Triangle inequality is not valid")