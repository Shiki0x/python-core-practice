import json

FILENAME = "party.json"

def load_party():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_party(party):
    with open(FILENAME, "w") as file:
        json.dump(party, file, indent=4)

party = load_party()

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
        if not party:
            print("Party is empty.")
        else:
            for i, member in enumerate(party, start=1):
                print(f"{i}. {member['name']} - {member['class']} (Lvl. {member['level']})")

    elif choice == "3":
        save_party(party)
        print("Party saved.")
        break