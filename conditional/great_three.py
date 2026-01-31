a = int(input("Enter first num : "))
b = int(input("Enter second num : "))
c = int(input("Enter third num : "))

# if a>b and a>c :
#     print("A is greater")
# elif b>a and b>c :
#     print("B is greater")
# elif c>a and c>b :
#     print("C is greater")
# elif a == b and a>c :
#     print("A and B are equal and greater than C")
# elif b == c and b>a :
#     print("B and C are equal and greater than A")
# elif a == c and a>b :
#     print("A and C are equal and greater than B")
# else :
#     print("All are equal")

max = max(a,b,c)

if a == b == c :
    print("All are equal")
else :
    if a == max :
        print("A is greater")
    if b == max :
        print("B is greater")
    if c == max :
        print("C is greater")