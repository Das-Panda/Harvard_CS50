# Nutrition.py

def main():
    # Dictionary to store fruit names and their corresponding calorie counts
    fruits = {
        "apple": 95,
        "avocado": 240,
        "banana": 105,
        "cantaloupe": 60,
        "grapefruit": 52,
        "grapes": 62,
        "honeydew melon": 61,
        "kiwifruit": 42,
        "lemon": 17,
        "lime": 20,
        "nectarine": 62,
        "orange": 62,
        "peach": 58,
        "pear": 100,
        "pineapple": 50,
        "plums": 30,
        "strawberries": 4,
        "sweet cherries": 5,
        "tangerine": 47,
        "watermelon": 86
    }

    # Prompt the user to input a fruit name
    fruit = input("Enter a fruit: ").strip().lower()

    # Check if the fruit is in the dictionary and output its calories
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")
    else:
        print("Fruit not found")

if __name__ == "__main__":
    main()