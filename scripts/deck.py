from random import shuffle
from copy import deepcopy
class Deck:

    def __init__(self, cards = []):
        self.cards = cards

    def shuffle(self, times = 1):
        result = deepcopy(self.cards)
        for _ in range(times):
            shuffle(result)

        return Deck(result)

    def top(self, number = 1):
        result = deepcopy(self.cards[:number])

        return result

    def draw(self, number = 1):
        result = self.cards[:number]
        self.cards = self.cards[number:]

        return result




