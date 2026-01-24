a = int(input("Enter first side : "))
b = int(input("Enter second side : "))

c = ((a*a) + (b*b))**(1/2)
print("Hypotenuse = %.2f"%c) # %.2f takes upto 2 decimal value

import math
# c = ((a*a) + (b*b))
# print("Hypotenuse using built-in function (math.sqrt) : %.2f" %math.sqrt(c))
print("Another funtion (math.hypot)%.2f" %math.hypot(a,b))
