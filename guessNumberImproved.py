import random

guess = 0
count = 0
randNumber = random.randint(1, 10)

print("Guess a number between 1 and 10")

while guess != randNumber:
    count += 1
    guess = input(f"Enter guess #{count}: ")

    if guess.isnumeric():
        guess = int(guess)
    else:
        print("Numbers only, please!")
        count -= 1
        continue
    
    if guess > randNumber:
        print("Your guess is too high, try again!")
    elif guess < randNumber:
        print("Your guess is too low, try again!")

print(f"You gussed it in {count} tries!")