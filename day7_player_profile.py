print("=== Player Profile Manager ===")

player = {}

while True:
    print("n\Options:")
    print("1. Create profile")
    print("2. View profile")
    print("3. Update stat")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        player["name"] = input ("Enter name: ")
        player["class"] = input ("Enter class: ")
        player["level"] = int(input("Enter level: "))
        player["hp"] = int(input("Enter HP: "))
        print("Profile created!")

    elif choice  == "2":
        if not player:
            print("No profile found.")
        else:
            print("\nPlayer Profile:")
            for key, value in player.items():
                print(f"{key}: {value}")

    elif choice == "3":
        if not player:
            print("Create a profile first.")
        else:
            stat = input("Which stat to update? ").lower()
            if stat in player:
                player[stat] = input("Enter new value: ")
                print(f"{stat} updated.")
            else:
                print("Stat not found.")
    
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")