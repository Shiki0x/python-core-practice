name = input("What is your name? ")

mood = input("How are you feeling today (happy, tired, bored, stressed)? ").lower()

print(f"\nHey {name}, based on your mood...")

if mood == "happy":
    print("You should play: Minecraft - super chill and creative.")

elif mood == "tired":
    print("You should play: Stardew Valley - relaxing and low effort.")

elif mood == "bored":
    print("You should play: Fallout 4 - big world, tons to explore.")

elif mood == "stressed":
    print("You should play: Skyrim - wander arund and unwind.")

else:
    print("Mood not recognized, so I recommend Resident Evil 4 because it's fire.")