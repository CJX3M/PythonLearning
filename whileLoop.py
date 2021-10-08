import random

roll = 0
count = 0

# while roll != 5:
#     count += 1
#     roll = random.randint(1, 5)
#     print(roll)

# print(f'It took {count} rolls to roll a 5!')

print('First person to roll a 5 wins!')

while roll != 5:
    name = input("Enter a name or 'q' to quit: ")
    if name.strip() == '':
        continue

    if name.strip() == 'q':
        break

    count += 1
    roll = random.randint(1, 5)
    print(f'{name} rolled a {roll}')
else:
    print(f'{name} Wins!!!!')

print(f'You rolled the dice {count} times.')