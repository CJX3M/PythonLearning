import random

guess = 0
count = 0
randNumber = random.randint(1, 5)

while guess != randNumber:
    guess = input("Guess a number between 1 and 5: ")
    count += 1
    if guess.isnumeric():
        guess = int(guess)

print(f'You guessed in {count} tries!')
