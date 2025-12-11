name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("What city do you live in? ")
hobby = input("What is your favorite hobby? ")

next_age = age + 1

print("\n--- Profile Summary ---")
print(f"Hello {name}! You live in {city}.")
print(f"You're {age} years old, and next year you'll be {next_age}.")
print(f"Your favorite hobby is {hobby}. That's awesome!")