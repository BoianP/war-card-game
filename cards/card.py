from enum import Enum

class Suit(Enum): 
    """
    This defines suits as the enumeration below, to be used in the card class. 
    the first integer is like an id for suits. It can be used for quick comparisons of suits, if needed. 
    It can also be used to identify a suit.
    """
    CLUBS = (1,'clubs', '\u2663', 'black')
    DIAMONDS = (2,'diamonds', '\u2666', 'red')
    HEARTS = (3, 'hearts', '\u2665', 'red')
    SPADES = (4,'spades', '\u2660', 'black')

    def __init__(self, idx, display_name, symbol, color):
        self.idx = idx
        self.display_name = display_name
        self.symbol = symbol
        self.color = color
    
    def __str__(self):
        return self.symbol
    
    @classmethod 
    def from_idx(cls, idx): #allows a reference to the suit from the id
        for member in cls:
            if member.idx == idx:
                return member
        raise ValueError(f"No suit with idx={idx}")

class Card:
    """The class represents a playing card from a standard deck with no jokers. There is no ordering, because that depends
    on the deck itself. When printing a card name, the unicode symbols for the suit are used. 
    Suits are done via an enumeration.
    """

    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
                  '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    #None is used so that '2' will correspond to the element indexed by 2. 
    #Having two 'Ace' position allows for aces to be both high and low

    def __init__(self, rank, suit):

        #first the rank is assigned, which must be an integer between 1 and 15
        if not isinstance(rank, int):
            raise ValueError("Rank must be an integer.")
        if not (1 <= rank <= 15):
            raise ValueError("Rank must be an integer between 1 and 15 inclusive.")
        self.rank = rank

        #the suit is handled. It must a member of suit. 
        if isinstance (suit, Suit): #returns an exception of suit is not a Suit variable
            self.suit = suit
        elif isinstance (suit, str): #what to do if suit is a string, ignoring case
            for s in Suit: #goes through Suit possibilities
                if suit.lower() == s.display_name:
                    self.suit = s
                    break
            else:
                raise ValueError(f"Unknown suit name: {suit}.")
        elif isinstance (suit, int): #what to do if suit is an integer
            self.suit=Suit.from_idx(suit)
        else:
            raise ValueError("Suit must be either an enum, a valid suit str, or a number between 1 and 4.")
        
    def color(self):
        return self.suit.color
 
    
    def __str__(self): 
        #prints only the first letter for face cards or the number otherwise. 
        #prints the symbol of the card instead of the suit. 
        s = self.short_symbol()
        return f"{s} {self.suit}"
        
    
    def short_symbol(self): #gets the symbol of the rank: the number or J Q K A
        s = Card.rank_names[self.rank] #gives the string of the card rank
        if self.rank == 10:
            return s
        else:
            return s[0]
   
    def __eq__(self, other):
        return self._to_tuple() == other._to_tuple()
    
    def _to_tuple(self): #converts to tuples
        return (self.suit, self.rank)
    
    def __lt__(self, other):
        return self._to_tuple() < other._to_tuple()
    
    def is_equal_rank(self, other):
        return self.rank == other.rank
    
    def is_lower_rank(self,other):
        return self.rank < other.rank
    
    def is_higher_rank(self, other):
        return other.is_lower_rank(self)
    
if __name__ == "__main__":
    qh = Card(12, 'Hearts')
    sixd = Card(6, 'Diamonds')
    #tens = Card(10, 'spade')
    #wrong_rank = Card(16, 1)
    #wrong2 = Card('King', 2)
    c = Card(5, 3)
   #d = Card(5,5)
    print(qh)
    print(sixd)
    #print(tens)
    #print(wrong_rank)
    #print(wrong2)
    print(c)
    #print(d)
    print(qh.color())
    print(sixd.color())
