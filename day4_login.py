print("=== Simple Login System ===")

correct_password = "gamer123"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted! Welcome!")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. Attempts left: {attempts}")

if attempts == 0:
    print("Too many failed attempts. Access locked.")