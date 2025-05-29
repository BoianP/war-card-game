from card import Card
import random

class Pile:
    """
    Defines a pile of cards. It supports placing a card at the top of the pile, the bottom of the pile, or random location.
    It can also take a card from the top, bottom, or random location.
    It can be shufelled and sorted.
    """ 
    def __init__(self, cards): # cards is a  list of cards
        pass

    def __str__(self): #how to display the pile
        pass

    def place_top(self, card): #places a card at the top of the pile
        pass

    def place_bottom(self, card): #places a card at the bottom of the Pile
        pass

    def place_random(self, card): #places a card at a random location
        pass

    def take_top(self, n=1): #takes a number of cards from the top and returns the card
        pass

    def take_bottom(self, n=1):  #takes a number of cards from the bottom and returns a card
        pass

    def take_random(self, n=1): #take a number of cards from random locations
        pass

    def remove(self, card): #removes a given card from a pile and returns None, if the card is not there. 
        pass

    def shuffle(self): #shuffles the pile
        pass

    def sort(self): #sorts the pile in order suits are put alphabetically in order
        pass

    def join(self, other): #joins two piles together
        pass

    def size(self): #gives the size of the pile
        pass

    def contains(self, card): #checks to see if a card is in the pile or not
        pass

