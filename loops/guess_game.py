import random
jack = random.randint(1,100)

guess = int(input("Guess the number : "))

count = 1
while guess != jack:
     if guess  < jack:
         print("Sorry! Guess higher ...")
     else:
         print("Sorry! Guess lower ...")

     guess = int(input("Guess the number : "))
     count += 1
else:
     print("You guessed it correct !!")
     print("Number of attempts made :",count)
