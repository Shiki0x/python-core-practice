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

def add_member(party):
    name = input("Name: ")
    role = input("Class: ")
    while True:
        try:
            level = int(input("Level: "))
            break
        except ValueError:
            print("Please enter a number.")

    party.append({
        "name": name,
        "class": role,
        "level": level
    })

def remove_member(party):
    name = input("Enter name to remove: ")
    found = False

    for member in party:
        if member["name"] == name:
            party.remove(member)
            print(f"{name} removed.")
            found = True
            break

    if not found:
        print("Member not found.")

def view_party(party):
    if not party:
        print("Party is empty.")
        return
    
    for i, member in enumerate(party, start=1):
        print(f"{i}. {member['name']} - {member['class']} (Lvl {member['level']})")

def main():
    party = load_party()

    while True:
        print("\n1. Add member")
        print("2. View party")
        print("3. Remove member")
        print("4. Save & Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_member(party)
        elif choice == "2":
            view_party(party)
        elif choice == "3":
            remove_member(party)
        elif choice == "4":
            save_party(party)
            print("Party saved!")
            break
        else:
            print("Enter a number between 1 and 4.")

main()