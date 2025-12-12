def add_member(party):
    name = input("Name: ")
    role = input("Class: ")
    level = int(input("Level: "))

    party.append({
        "name": name,
        "class": role,
        "level": level
    })

def view_party(party):
    if not party:
        print("Party is empty.")
        return
    
    for i, member in enumerate(party, start=1):
        print(f"{i}. {member["name"]} - {member["class"]} (Lvl {member["level"]})")

def main():
    party = []

    while True:
        print("\n1. Add member")
        print("2. View party")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_member(party)
        elif choice == "2":
            view_party(party)
        elif choice == "3":
            break

main()