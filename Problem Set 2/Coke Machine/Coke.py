# Coke.py

def main():
    # Cost of a Coke bottle
    cost = 50

    # Accepted coin denominations
    accepted_coins = [25, 10, 5]

    # Initialize the total amount inserted by the user
    total_inserted = 0

    # Prompt the user to insert coins until the total is at least 50 cents
    while total_inserted < cost:
        # Display the amount due
        amount_due = cost - total_inserted
        print(f"Amount due: {amount_due} cents")

        # Prompt the user to insert a coin
        coin = int(input("Insert a coin (25, 10, 5): ").strip())

        # Check if the inserted coin is accepted
        if coin in accepted_coins:
            total_inserted += coin
        else:
            print("Invalid coin. Please insert a coin in the denomination of 25, 10, or 5 cents.")

    # Calculate the change owed
    change_owed = total_inserted - cost

    # Output the change owed to the user
    print(f"Change owed: {change_owed} cents")

if __name__ == "__main__":
    main()