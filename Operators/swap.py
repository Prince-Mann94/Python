# Method 1 for swapping
a = int(input("Enter first num : "))
b = int(input("Enter second num : "))

print("Before swapping : ",a,b)
# a,b = b,a
# print("After swapping : ",a,b)

# Method 2 for swapping
temp = a
a = b
b = temp

print("After swapping : ",a,b)



