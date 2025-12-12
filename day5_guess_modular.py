import random

def generate_number():
    return random.randint(1, 20)

def get_guess():
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        return None
    return int(guess)

def check_guess(guess, secret):
    if guess == secret:
        return "correct"
    elif guess < secret:
        return "low"
    else:
        return "high"
    
def play_game():
    secret_number = generate_number()
    attempts = 5
    print("I'm thinking of a number between 1 and 20.")

    while attempts > 0:
        guess = get_guess()
        if guess is None:
            continue
        
        result = check_guess(guess, secret_number)

        if result == "correct":
            print(f"🎉 Correct! The number was {secret_number}.")
            return
        elif result == "low":
            print("Too low!")
        else:
            print("Too high")
        
        attempts -= 1
        print(f"Attempts left: {attempts}")

    print(f"😢 Out of attempts! The number was {secret_number}.")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break

main()