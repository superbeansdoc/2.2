import random
number = random.randint(1,20)
guess = int(input("what do you think the number is?"))
while True:
    if guess == number:
        print ("good job correct")
        break
    if guess > number:
        print("its less")
        guess = int(input("what do you think the number is?"))
    if guess < number:
        print("its more")
        guess = int(input("what do you think the number is?"))
        