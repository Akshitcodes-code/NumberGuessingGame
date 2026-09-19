import random


def difficulty():
    print("\nE - Easy | H - Hard | I - Insane")

    while True:
        diff = input("Enter the difficulty level (E/H/I): ").lower()

        if diff in ["e", "h", "i"]:
            break

        print("Invalid difficulty choice")

    if diff == "e":
        return 10
    elif diff == "h":
        return 5
    else:
        return 2


def calculate_score(count, give_tries):
    score = 1000

    if give_tries == 10:
        score -= count * 100
    elif give_tries == 5:
        score -= count * 200
    elif give_tries == 2:
        score -= count * 500

    return max(0, score)


def get_number():
    while True:
        try:
            number = int(input("\nEnter any number from (0-100): "))

            if 0 <= number <= 100:
                return number
            else:
                print("Enter a number between 0 and 100 only.")

        except ValueError:
            print("Please enter a valid number.")


def game():
    print("------- NUMBER GUESSING GAME -----------")

    while True:
        give_tries = difficulty()

        random_number = random.randint(0, 100)
        count = 0

        while count < give_tries:

            guess = get_number()
            count += 1

            if guess == random_number:
                print("You win! 🎉")
                break

            elif guess > random_number:
                print("Too High!")

            else:
                print("Too Low!")

        else:
            print("YOU LOST! ALL YOUR CHANCES ARE OVER.")
            print("The number was:", random_number)

        print("You took", count, "tries")

        print(
            "Your score is",
            calculate_score(count, give_tries),
            "points"
        )

        choice = input(
            "\nDo you want to play again? (Y/N): "
        ).lower()

        if choice == "n":
            print("Thanks for playing!")
            break

        elif choice != "y":
            print("Invalid choice.")


if __name__ == "__main__":
    game()