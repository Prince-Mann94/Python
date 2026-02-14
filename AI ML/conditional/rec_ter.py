l1,w1 = map(int,input("Enter length and breadth of R1 : ").split())
l2,w2 = map(int,input("Enter length and breadth of R2 : ").split())
l3,w3 = map(int,input("Enter length and breadth of R3 : ").split())

p1 = 2*(l1+w1)
p2 = 2*(l2+w2)
p3 = 2*(l3+w3)
                            # p = perimeter , l = length , w = width
print("P1 = ",p1)
print("P2 = ",p2)
print("P3 = ",p3)

max = p1 if (p1>p2 and p2>p3) else (p3 if p3>p2 else p2) 
print("Max perimeter is : ",max)
