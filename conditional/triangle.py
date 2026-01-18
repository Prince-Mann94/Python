a = int(input("Enter side 1 = "))
b = int(input("Enter side 2 = "))
c = int(input("Enter side 3 = "))

if(a+b > c and b+c> a and a+c > b):
    print("Triangle is valid")
    if(a == b and b == c and a == c):
        print("Equilateral Triangle")
    elif(a == b or b==c or c==a):
        print("isosceles")
    elif((a*a) + (b*b) == (c*c) or (a*a) + (c*c) == (b*b) or (c*c) + (b*b) == (a*a)):
        print("Right angled triangle")
    else:
        print("Scalene") 
else:
    print("Triangle is not valid")