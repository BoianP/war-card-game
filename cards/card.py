class Card:
    """The class represents a playing card from a standard deck with no jokers. There is no ordering, because that depends
    on the deck itself. When printing a card name, the unicode symbols for the suit are used
    """

    suit_names = ['clubs', 'diamonds', 'hearts', 'spades']#a list of standard suits, in lower case formats
    suit_symbols =['\u2663', '\u2666', '\u2665', '\u2660'] #a list of unicode encodings of symbols
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
                  '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    #None is used so that '2' will correspond to the element indexed by 2. 
    #Having two 'Ace' position allows for aces to be both high and low

    suit_to_int = {name: i for i, name in enumerate(suit_names)} #creates a mapping from suits to int
    int_to_suit = {i: name for i,name in enumerate(suit_names)} #creates a mapping from int to suit


    def __init__(self, rank, suit):

        #first the rank is assigned, which must be an integer between 1 and 15
        if not isinstance(rank, int):
            raise ValueError("Rank must be an integer.")
        if not (1 <= rank <= 15):
            raise ValueError("Rank must be an integer between 1 and 15 inclusive.")
        self.rank = rank

        #the suit is handled. Only integer values between 0 and 3 or string values from suit_names accepted. 
        #Suit attribute is stored and handled as integer
        if isinstance (suit, int): #handles number suits
            if not (0<= suit <= 3):
                raise ValueError("Suit integer must be between 0 and 3 inclusive.")
            self.suit = suit 
        elif isinstance(suit, str): #handles string suits
            if suit.lower() not in Card.suit_names: #converts to lower case to handle capitalization errors
                raise ValueError("Suit is not a valid suit.")
            self.suit = Card.suit_to_int[suit.lower()] 
        else:
            raise ValueError("Suit must be an integer between 0 and 3 or 'Clubs', 'Diamonds', 'Hearts', 'Spades'.")
    
    def isValid(self):
        return (1 <= self.rank <= 15) and (0 <= self.suit <= 3)

    @staticmethod
    def suit_color(s: int):
        if Card.int_to_suit[s] in ('clubs', 'spades'):
            return 'Black'
        elif Card.int_to_suit[s] in ('hearts', 'diamonds'):
            return 'Red'
        else:
            return None
        
    def color(self):
        return Card.suit_color(self.suit)
 
    
    def __str__(self): 
        #prints only the first letter for face cards or the number otherwise. 
        #prints the symbol of the card instead of the suit. 
        if self.rank == 10:
            return f"{int(Card.rank_names[self.rank])} {Card.suit_symbols[self.suit]}"
        else:
            return f"{Card.rank_names[self.rank][0]} {Card.suit_symbols[self.suit]}"
   
    def __eq__(self, other):
        return self.suit == other.suit and self.rank ==other.rank
    
    def _to_tuple(self): #converts to tuples
        return (self.suit, self.rank)
    
    def __lt__(self, other): #uses lexicographic ordering all clubs are less than any diamond etc. 
        return self._to_tuple() < other._to_tuple()
    
    def __le__(self, other):
        return self._to_tuple() <= other._to_tuple()
    
if __name__ == "__main__":
    qh = Card(12, 'Hearts')
    sixd = Card(6, 'Diamonds')
    tens = Card(10, 'spades')
    print(qh)
    print(sixd)
    print(tens)
    print(qh.color())
    print(sixd.color())
    print(tens.color())