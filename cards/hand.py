class Hand:
    """
    The class represents hands of cards. They can be as big as needed. 
    """
    def __init__(self, cards = None):
        self.cards = cards if cards is not None else []
    
    def add_card(self, card):
        if card in self.cards:
            raise ValueError("Card is already in hand.")
        else:
            self.cards.append(card)
   
    def remove_card(self, card):
        if card not in self.cards:
            raise ValueError("Card is not in hand.")
        else:
            self.cards.remove(card)
    
    def sort_hand(self):
        self.cards.sort()
    
    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        return '\n'.join(str(card) for card in self.cards)