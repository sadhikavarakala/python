import random

secret_number = random.randint(1, 200)
attempts = 0

print("Guess the  number between 1 and 200")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("too low, try again")
    elif guess > secret_number:
        print("too high, try again")
    else:
        print(f"Congrats, you passed in {attempts} attempts.")
        break