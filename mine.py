import random


while True:
    
    randomnum = random.randint(1,10)

    guess = int(input("guess a number between 1 and 10 :"))

    if guess == randomnum :
        print("correct !")
    elif guess < randomnum :
        print("your number is low")
    else:
        print("your number is big")