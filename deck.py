def createDeck():
    suits = ["Corazones", "Tréboles", "Espadas", "Diamantes"]
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Joto", "Reina", "Rey", "Az"]
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} de {suit}')

    return deck