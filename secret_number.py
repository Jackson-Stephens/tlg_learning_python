import random
secretnumber = random.randint(1, 100)

print("Guess the secret number.")
print(secretnumber) # for testing the code
guess = 0
while guess != secretnumber:
    guess = int(input("Guess any number between 1 and 100: "))

    if guess == secretnumber:
        print("You guessed it!")
        print("You win!")
        break

    elif guess < secretnumber:
        print("Your guess is too low, try again!")

    elif guess > secretnumber:
        print("Your guess is too high, try again!")







