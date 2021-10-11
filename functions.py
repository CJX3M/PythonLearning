# def sayHello():
#     print(f"Hello World")

# sayHello()

# def sayHello(name):
#     print(f"Hello {name}")

# sayHello("Carlos")

# def sayHello(name="World"):
#     print(f"Hello {name}")

# sayHello()
# sayHello("Carlos")
# anotherName = "Bob"
# sayHello(anotherName)

# def sayHello(name="World", greeting=None):
#     if greeting == None:
#         print(f"Hello {name}!")
#     else:
#         print(f"{greeting} {name}!")

# sayHello()
# sayHello("Carlos")
# sayHello(greeting="Howdy")
# sayHello("Bob", "Good evening")

# def addTwoNumber(number1, number2):
#     return number1 + number2

# addTwoNumber(2, 3)
# result = addTwoNumber(6, 78)
# print(result)

# def create_deck():
#   suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
#   ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#   deck = []

#   for  suit in suits:
#     for rank in ranks:
#       deck.append(f'{rank} of {suit}')

#   return deck

# my_deck = create_deck()
# print(len(my_deck))

value = 1

def someValue():
    value = 10
    return value

print(value)
print(someValue())
print(value)