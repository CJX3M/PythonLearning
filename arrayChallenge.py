import random 
stacks = ['Diamante', 'Corazon', 'Trebol', 'Espada']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Joto', 'Reina', 'Rey', 'Az']
cards = []

for stack in stacks:
    for rank in ranks:
        cards.append(f'{rank} de {stack}')

print(f'There are {len(cards)} cards in the deck.')

print('Dealing...')

hand = []

while len(hand) < 5:
    card = random.choice(cards)
    cards.remove(card)
    hand.append(card)

print(f'There are {len(cards)} cards in the deck.')

print(f'Player hand: {hand}')
