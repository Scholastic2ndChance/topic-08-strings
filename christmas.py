# Print the menu
def menu():
    print("\n=== Christmas Gift Tracker ===")
    for key, value in user_menu.items():
        print(f"{key}. {value}")
    
    choice = input("Choose an option: ").strip()
    return choice


def view_gifts():
    while True:
        print("\n=== View Gifts ===")
        for key, value in view_sub_menu.items():
            print(f"{key}. {value}")

        choice = input("Choose an option: ").strip()

        # View full list
        if choice == "1":
            print("\n--- Full Gift List ---")
            for person, gifts in gift_tracker.items():
                print(f"{person}: {', '.join(gifts)}")

        # View one person
        elif choice == "2":
            person = input("Enter the person's name: ").strip()
            if person in gift_tracker:
                print(f"\n{person}'s gifts:")
                for gift in gift_tracker[person]:
                    print(f"- {gift}")
            else:
                print("Person not found.")

        # Alphabetize full list
        elif choice == "3":
            print("\n--- Alphabetized Gift List ---")
            for person in sorted(gift_tracker.keys()):
                sorted_gifts = sorted(gift_tracker[person])
                print(f"{person}: {', '.join(sorted_gifts)}")

        # Back to main menu
        elif choice == "4":
            return

        else:
            print("Invalid choice. Try again.")


def modify_gifts():
    while True:
        print("\n=== Modify Gifts ===")
        for key, value in edit_sub_menu.items():
            print(f"{key}. {value}")

        choice = input("Choose an option: ").strip()

        # Add a gift
        if choice == "1":
            person = input("Enter the person's name: ").strip()
            if person in gift_tracker:
                gift = input("Enter the gift to add: ").strip()
                gift_tracker[person].append(gift)
                print(f"Added '{gift}' to {person}.")
            else:
                print("Person not found.")

        # Move a gift to another person
        elif choice == "2":
            source = input("Gift currently belongs to who? ").strip()
            if source not in gift_tracker:
                print("Person not found.")
                continue

            gift = input("Which gift do you want to move? ").strip()
            if gift not in gift_tracker[source]:
                print("Gift not found.")
                continue

            target = input("Move gift to which person? ").strip()
            if target not in gift_tracker:
                print("Target person not found.")
                continue

            # Perform the move
            gift_tracker[source].remove(gift)
            gift_tracker[target].append(gift)
            print(f"Moved '{gift}' from {source} to {target}.")

        # Remove a gift
        elif choice == "3":
            person = input("Enter the person's name: ").strip()
            if person not in gift_tracker:
                print("Person not found.")
                continue

            gift = input("Enter the gift to remove: ").strip()
            if gift in gift_tracker[person]:
                gift_tracker[person].remove(gift)
                print(f"Removed '{gift}' from {person}.")
            else:
                print("Gift not found.")

        # Back to main menu
        elif choice == "4":
            return

        else:
            print("Invalid choice. Try again.")


# initialize Dictionaries.
user_menu = {
    "1": "View Gifts",
    "2": "Modify Gifts",
    "3": "Exit"
}

view_sub_menu = {
    "1": "View full list",
    "2": "View one person",
    "3": "Alphabetize full list",
    "4": "Back"
}

edit_sub_menu = {
    "1": "Add Gift",
    "2": "Move gift to another person",
    "3": "Remove Gift",
    "4": "Back"
}

gift_tracker = {
    "Dad": ["New drill bits", "Coffee sampler"],
    "Mom": ["Knitting yarn", "Spa gift card"],
    "Sister": ["Cookbook", "Bluetooth speaker"],
    "Brother": ["Board game", "Running socks"],
    "Grandma": ["Puzzle set", "Tea assortment"],
    "Grandpa": ["History book", "Warm slippers"]
}

# Main loop
while True:
    choice = menu()
    if choice == "1":
        view_gifts()
    elif choice == "2":
        modify_gifts()
    elif choice == "3":
        break

print("Goodbye!")
