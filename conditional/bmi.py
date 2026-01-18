ht = float(input("Enter height (mts): "))
wt = float(input("Enter weight (kgs): "))

bmi = wt/(ht*ht)
if(bmi < 15):
    print("Starvation")
elif(bmi >= 15.1 and bmi < 17.5):
    print("Anorexic")
elif(bmi >= 17.5 and bmi < 18.5):
    print("Underweight")
elif(bmi >= 18.5 and bmi < 24.9):
    print("Ideal")
elif(bmi >= 24.9 and bmi < 25.9):
    print("overweight")
elif(bmi >= 25.9 and bmi < 39.9):
    print("Obese")
else:
    print("Moridity obese")
