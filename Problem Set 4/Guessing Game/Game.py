import random

def main():
    level = get_level()
    target = random.randint(1, level)
    guess = None

    while guess != target:
        guess = get_guess()
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass
        print("Please enter a positive integer.")

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass
        print("Please enter a positive integer.")

if __name__ == "__main__":
    main()