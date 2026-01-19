x1,y1 = map(int,input("Enter x1 and y1 : ").split())
x2,y2 = map(int,input("Enter x2 and y2 : ").split())
x3,y3 = map(int,input("Enter x3 and y3 : ").split())

s1 = (y2-y1)*(x3-x2)
s2 = (y3-y2)*(x2-x1)

if(s1 == s2):
    print("Collinear")
else:
    print("Not collinear")