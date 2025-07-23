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
        "----------"
    ]
    for line in mountain_map:
        print(line)
    print("Treasure clue is marked with an 'X' on the mountain!\n")

def mountain_adventure(backpack):
    print("\n--- Backpack Checklist ---")
    checklist = ["Rope", "Food", "Bottle of Water", "Treasure Map"]
    for item in checklist:
        print(f"[{'X' if item.lower() in [i.lower() for i in backpack] else ' '}] {item}")
    print("-------------------------\n")

    if check_backpack(backpack) == "complete":
        print("Backpack is complete. Going to the base of the mountain...")
        print("Arrived at the base of the mountain. Proceeding to the trail!")

        mark_treasure_location()
        n = random.randint(1, 6)
        print(f"Aleatory number: {n}")
        if n % 2 == 0:
            print("Pair number! You got an clue of the treasure, keep looking!")
            return True  # Success
        else:
            print("Odd number! No clue about the treasure this time.")
            return False  # Failure
    else:
        print("Backpack is incomplete. Returning home.")
        return None  # Incomplete

if __name__ == "__main__":
    score = 0
    streak = 0
    loop_count = 0
    print("=== Mountain Treasure Hunt ===")
    print("Checklist: Rope, Food, Bottle of Water, Treasure Map")
    print("Type 'sair' anytime to quit.\n")

    while True:
        loop_count += 1

        user_input = input("Prepare your backpack (comma-separated): ").strip()
        if user_input.lower() == "sair":
            print(f"\nGame over! Your final score: {score}")
            break

        my_backpack = [item.strip() for item in user_input.split(",") if item.strip()]
        result = mountain_adventure(my_backpack)

        if result is True:
            score += 1
            streak += 1
            if streak == 3:
                print("🔥 Streak bonus! +3 points!")
                score += 3
                streak = 0  # Reset streak
        elif result is False:
            streak = 0

        print(f"Current score: ⭐ { score } | Streak: {streak}\n")

        
        if score >= 10:
            print("🏆 YOU FOUND THE TREASURE, CONGRATULATIONS!")
            print("How many rounds until you win ?")
            print( loop_count)
            break
