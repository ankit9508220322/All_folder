import random

game = random.randint(1, 100)
guess = int(input("Enter a number between 1 and 100: "))
counter = 1

while guess != game:
    if guess < game:
        print("Guess a higher number")
    else:
        print("Guess a lower number")

    guess = int(input("Please enter the correct number: "))
    counter += 1

else:
    print(f"🎉 Correct! The number was {game}")
    print(f"Attempts: {counter}")
