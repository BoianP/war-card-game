class Card:
    """Represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
                  '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    #None is used so that '2' will correspond to the element indexed by 2. 

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"
    
    def __eq__(self, other):
        return self.suit == other.suit and self.rank ==other.rank
    
    def _to_tuple(self): #converts to tuples
        return (self.suit, self.rank)
    
    def __lt__(self, other): #uses lexicographic ordering all clubs are less than any diamond etc. 
        return self._to_tuple() < other._to_tuple()
    
    def __le__(self, other):
        return self._to_tuple() <= other._to_tuple()
    
class Hand:
    """
    Handling hands of cards
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

class FullDeck(Hand):
    """Class to full Full decks - hands of all cards. The Variable AceHigh reprsents whether Ace is a high or low card"""
    
    def __init__(self, AceHigh = True):
        super().__init__(self.MakeDeck(AceHigh)) #calls the Hand constructor

    @staticmethod
    def MakeDeck(AceHigh):
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