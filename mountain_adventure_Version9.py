import random

def check_backpack(backpack):
    required_items = {"rope", "food", "bottle of water", "treasure map"}
    backpack_items = set(item.lower() for item in backpack)
    return "complete" if required_items.issubset(backpack_items) else "incomplete"

def mark_treasure_location():
    print("\nYou use the treasure map to mark the spot!")
    mountain_map = [
        "    /\\",
        "   /  \\",
        "  /    \\",
        " /  X   \\",
        "/        \\",
        "----------",
        "    "
    ]
    for line in mountain_map:
        print(line)
    print("Treasure location marked with 'X' on the mountain!\n")

def mountain_adventure(backpack):
    print("\n--- Backpack Checklist ---")
    checklist = ["Rope", "Food", "Bottle of Water", "Treasure Map"]
    for item in checklist:
        print(f"[{'X' if item.lower() in [i.lower() for i in backpack] else ' '}] {item}")
    print("-------------------------\n")
    if check_backpack(backpack) == "complete":
        print("Backpack is complete. Going to the base of the mountain...")
        print("Arrived at the base of the mountain. Proceeding to the trail!")
        if "treasure map" in [item.lower() for item in backpack]:
            mark_treasure_location()
            n = random.randint(1, 10)
            print(f"Aleatory number: {n}")
            if n % 2 == 0:
                print("Pair number! Happy ending: You found the treasure!")
            else:
                print("Odd number! No treasure this time.")
        return "trail"
    else:
        print("Backpack is incomplete. Returning home.")
        return "home"

if __name__ == "__main__":
    print("What items do you want to put in your backpack for the mountain trip?")
    print("Checklist of items you need:")
    print(" - Rope\n - Food\n - Bottle of Water\n - Treasure Map\n")
    print("Separate your items with commas.")
    user_input = input("Enter items: ")
    my_backpack = [item.strip() for item in user_input.split(",") if item.strip()]
    mountain_adventure(my_backpack)