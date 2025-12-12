import random

secret = random.randint(1, 10)

while True:
    try:
        guess = int(input("Guess a number (1-10): "))
        if guess < 1 or guess > 10:
            print("Number must be between 1 and 10.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if guess == secret:
        print("Correct!")
        break
    else:
        print("Wrong, try again.")