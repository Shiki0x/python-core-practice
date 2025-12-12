import random

def get_valid_guess():
    while True:
        try:
            guess = int(input("Guess a number (1-10): "))
            if 1 <= guess <= 10:
                return guess
            print("Out of range.")
        except ValueError:
            print("Invalid input.")

def check_guess(guess, secret):
    return guess == secret

def main():
    secret = random.randint(1, 10)

    while True:
        guess = get_valid_guess()
        if check_guess(guess, secret):
            print("Correct!")
            break
        else:
            print("Wrong, try again.")

main()