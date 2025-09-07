import random

randomnum = random.randint(1,10)

while True:
    

    guess = int(input("guess a number between 1 and 10 :"))

    if guess == randomnum :
        print("correct !")
        break
    elif guess > 10 or guess < 1:
        print("enter a valible number")
        
    elif guess < randomnum :
        print("your number is low")
    else:
        print("your number is big")
