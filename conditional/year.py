year = int(input("Enter year : "))
days = 0
for y in range(1,year):
 if(y %4 == 0 and y%100 != 0) or (y%400 == 0):
    days+=366
 else:
    days+=365

total_days = days%7
match total_days:
    case 0:
        print("Monday")
    case 1:
        print("Tuesday")
    case 2:
        print("Wednesday")
    case 3:
        print("Thursday") 
    case 4:
        print("Friday")
    case 5:
        print("Saturday")
    case 6:
        print("Sunday")
