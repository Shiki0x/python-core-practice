print("=== Party Manager ===")

# List holds many records.
# Dictionary holds one record.
# Keys such as "name", "class", "level" label the data.
party = []

while True:
    print("\nOptions:")
    print("1. Add member")
    print("2. View party")
    print("3. Remove member")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        name = input("Name: ")
        role = input("Class: ")
        level = int(input("Level: "))

        member = {
            "name": name,
            "class": role,
            "level": level
        }

        party.append(member)
        print(f"{name} added to the party.")
    
    elif choice == "2":
        if not party:
            print("Party is empty.")
        else:
            print("\nParty Members:")
            for i, member in enumerate(party, start=1):
                print(f"{i}. {member['name']} - {member['class']} - (Lvl {member['level']})")

    elif choice == "3":
        name = input("Enter name to remove: ")
        for member in party:
            if member["name"] == name:
                party.remove(member)
                print(f"{name} removed.")
                break
        else:
            print("Member not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")