party = []

FILENAME = "party.txt"

def load_party():
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                name, role, level = line.strip().split(",")
                party.append({
                    "name": name,
                    "class": role,
                    "level": int(level)
                })
    except FileNotFoundError:
        pass

def save_party():
    with open(FILENAME, "w") as file:
        for member in party:
            file.write(f"{member['name']},{member['class']},{member['level']}\n")

load_party()

while True:
    print("\n1. Add member")
    print("2. View party")
    print("3. Save & exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        role = input("Class: ")
        level = int(input("Level: "))

        party.append({
            "name": name,
            "class": role,
            "level": level
        })
    
    elif choice == "2":
        for i, member in enumerate(party, start=1):
            print(f"{i}. {member['name']} - {member['class']} (Lvl {member['level']})")

    elif choice == "3":
        save_party()
        print("Party saved.")
        break