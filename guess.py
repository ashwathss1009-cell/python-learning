import random

l = random.randint(1,50)
while True :
    print("1. play\n"
           "2. exit")
    choice = int(input("Enter your choice   "))
    if choice == 1:
            guess = int(input("Enter any number 1-50 :" ))

            if l == guess:
                print(f"you guessed correct number {l}")
            elif l < guess:
                print("you guessed a higher number")
            elif l > guess:
                print("you guessed a bit lower number")
            else :
                print("enter the current number in give range 1-50")
                
    if choice == 2:
        break