import random

while True:
    print("=== Number Guessing Game ===")

    secret_number = random.randint(1, 20)
    attempts = 5

    print("I'm thinking of a number between 1 and 20.")
    print(f"You have {attempts} attempts to guess it!")

    while attempts > 0:
        guess = input("\nEnter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess == secret_number:
            print(f"🎉 Coorect! The number was {secret_number}. You win!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        attempts -= 1
        print(f"Attempts left: {attempts}")

    if attempts == 0:
        print(f"\n😢 Out of attempts! The number was {secret_number}. Better luck next time!")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break