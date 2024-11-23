import random


def guess_number():
    secret_number = random.randint(1, 100)

    print("Random Number Guessing Game!")
    print("Guess the numbers from 1 - 100.")

    while True:
        guess = input("Guess the number here: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid Input!")
            continue


        if guess < secret_number:
            print(f"{guess} is too low. Try again")
        elif guess > secret_number:
            print(f"{guess} is too high. Try again")
        else:
            print(f"You guessed right! The secret number is {guess}!")
            break
if __name__ == "__main__":
    guess_number()
