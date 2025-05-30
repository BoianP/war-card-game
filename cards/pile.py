from card import Card
import random

class Pile:
    """
    Defines a pile of cards. It supports placing a card at the top of the pile, the bottom of the pile, or random location.
    It can also take a card from the top, bottom, or random location.
    It can be shufelled and sorted.
    The class assumes that it comes from a single deck. So no repetitions are allowed.
    """ 
    def __init__(self, cards: list[Card]=None): # cards is a  list of cards
        self.cards = list(cards) if cards else []

    def _ensure_not_duplicate(self, card: Card):
        if card in self:
            raise ValueError(f"Card {card} already in pile.")
    
    def __contains__(self, card: Card):
        return card in self.cards

    def __str__(self): 
        dc = self.group_by_suit()
        display_string ='' # initializes a string to display
        for s in dc:
            display_string += (s.symbol + ' ')
            for c in dc[s]:
                display_string += (c.short_symbol() + ' ')
            display_string += '\n'  
        return display_string     
    
    def group_by_suit(self) -> dict:
        from card import Suit
        suit_map = {suit: [] for suit in Suit} #creates the empty hand to fill
        for card in self.cards:
            suit_map[card.suit].append(card)
        for cards in suit_map.values():
            cards.sort()
        return suit_map

    def place_top(self, card: Card) -> None: #places cards at the top of the pile
        self._ensure_not_duplicate(card)
        self.cards.append(card)

    def place_bottom(self, card: Card) -> None: #places a card at the bottom of the Pile
        self._ensure_not_duplicate(card)
        self.cards.insert(0, card)

    def place_random(self, card: Card) -> None: #places a card at a random location
        self._ensure_not_duplicate(card)
        s = self.size()
        index = random.randint(0, s-1)
        self.cards.insert(index, card)
        return index

    def take_top(self, n=1)  -> list[Card]: #takes a number of cards from the top and returns the clist of cards
        if n > self.size():
            raise ValueError(f"List contains only {self.size()} elements. Cannot draw {n}.")
        cards=[]
        for _ in range(n):
            c = self.cards.pop()
            cards.append(c)
        return cards

    def take_bottom(self, n=1) -> list[Card]:  #takes a number of cards from the bottom and returns them as a list
        if n > self.size():
            raise ValueError(f"List contains only {self.size()} elements. Cannot draw {n}.")
        cards = []
        for _ in range(n):
            c = self.cards.pop(0)
            cards.append(c)
        return cards

    def take_random(self, n=1) -> list[Card]: #take a number of cards from random locations and returns them as a list
        if n > self.size():
            raise ValueError(f"List contains only {self.size()} elements. Cannot draw {n}.")
        cards = []
        s = self.size() 
        for _ in range(n):
            index = random.randint(0,s-1)
            c = self.cards.pop(index)
            cards.append(c)
            s -= 1 #decrease the size of the collection
        return cards

    def remove(self, card) -> None: #removes a given card from a pile and returns None, if the card is not there. 
        if self.contains(card):
            return self.cards.remove(card)
        else:
            return None

    def shuffle(self) -> FileNotFoundError: #shuffles the pile
        random.shuffle(self.cards)

    def sort(self) -> None: #sorts the pile in order suits are put alphabetically in order
        self.cards.sort()

    def join(self, other) -> "Pile": #joins two piles together
        return Pile(self.cards+other.cards)

    def size(self) -> int: #gives the size of the pile
        return len(self.cards)
    
if __name__ == "__main__":
    hand = Pile([Card(2,1), Card(13, 1), Card(10, 1), Card(11,2), Card(14,3), Card(8,3), Card(10,4), Card (14, 4)])
    empty = Pile()
    print(hand)
    print(empty)

