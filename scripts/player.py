import deck
class Player:
    def __init__(self, name, op_deck, num_deck, hp = 10):
        self.name = name
        self.op_deck = op_deck
        self.num_deck = num_deck
        self.op_hand = []
        self.num_hand = []
        self.hp = hp
        self.status = "alive"

    def activate_card(self, operation_index, number_index, target):
        op_card = self.op_hand.pop(operation_index - 1)
        num_card = self.num_hand.pop(number_index - 1)

        return [op_card, num_card, target]

    def draw_card(self, deck, hand, number = 1):
        new_cards = deck.draw(number)
        hand.extend(new_cards)
    
