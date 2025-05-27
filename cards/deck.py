from cards import Card, Hand

class Deck(Hand):
    """
    Class to represent a standard deck (or shoe) of cards.
    The variable AceHigh determines whether Ace is treated as high (default) or low.
    Inherits from Hand; uses Hand's methods for card management.
    """
    
    def __init__(self, AceHigh = True):
        super().__init__(self.make_deck(AceHigh)) #calls the Hand constructor

    @staticmethod
    def make_deck(AceHigh):
        cards = []
        for suit in range(4):
            if AceHigh:
                for rank in range(2,15): #Ace is the higherst in this case
                    card = Card(suit, rank)
                    cards.append(card) #creates s list of Card objects
            else:
                for rank in range(1,14): #Ace is the lowest in this case
                    card = Card(suit, rank)
                    cards.append(card) #creates s list of Card objects
        return cards
    
    def shuffle(self):
        from random import shuffle
        shuffle(self.cards)

    def deal(self, n): #deals a hand of cards
        dealt = self.cards[:n] #creates a list of dealt cards
        self.cards = self.cards[n:]
        return Hand(dealt)