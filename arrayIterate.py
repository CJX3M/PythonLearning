# numbers = [1, 3, 5]

# print(5 in numbers)
# print(8 in numbers)

# print(5 not in numbers)
# print(8 not in numbers)

# cities = ["Chicago", "London", "Tokyo"]

# for city in cities:
#     print(city)

# numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
# numbers.sort()

# for number in numbers:
#   if number > 42:
#     break
#   print(number)

# import random
# numbers = []

# while len(numbers) < 5:
#     numbers.append(random.randint(1, 100))

# for number in numbers:
#     print(number)
#     if number >= 90:
#         print("Found at least 1 number greater than 90")
#         break
# else:
#     print("No number greater than 90")

# print("Complete")

# values = ["laptop", 7, "phone", 4, "dslr", 5]
# equipment = []

# for value in values:
#     if not isinstance(value, str):
#         continue
#     equipment.append(value)

# print(equipment)

# suits = ["Corazones", "Diamantes", "Espadas", "Treboles"]
# ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Joto", "Reina", "Rey", "Az"]

# for suit in suits:
#     for rank in ranks:
#         print(f'{rank} de {suit}')

import random

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
selectedNumber = random.choice(numbers)
print(selectedNumber)

selectedNumbers = random.choices(numbers, k=3)
print(selectedNumbers)