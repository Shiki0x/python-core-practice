print("=== Game Library Tracker ===")

games = []

while True:
    print("\nOptions:")
    print("1. Add a game")
    print("2. View games")
    print("3. Remove a game")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        game = input("Enter game name: ")
        games.append(game)
        print(f"{game} added to library.")

    elif choice == "2":
        if not games:
            print("Your library is empty.")
        else:
            print("\nYour Games: ")
            for i, game in enumerate(games, start=1):
                print(f"{i}. {game}")

    elif choice == "3":
        game = input("Enter game name to remove: ")
        if game in games:
            games.remove(game)
            print(f"{game} removed.")
        else:
            print("Game not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")