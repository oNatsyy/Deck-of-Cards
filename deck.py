#-------------------------------------------------------
# Name:        deck.py
# Purpose:     Education purposes only, copying will be subject to plagiarism
# Author:      Syed Natiq Ali Abidi
# Created:     23-April-2021
# Updated:     25-April-2021
#-------------------------------------------------------


from typing import List, Tuple
from cards import Card
import random

SUITS = ["Clubs", "Spades", "Hearts", "Diamonds"]
CARDS = ["ACE", "KING", "QUEEN", "JACK", "2", "3", "4", "5", "6", "7", "8",
         "9", "10"]

class Deck:
    """
    Represents a deck of cards for the whole game.

    === Public Attributes ===
    deck:
        A collection of 52 cards that are divided into 13 types and 4 suits.

    """
    deck : List[str]

    def __init__(self) -> None:
        """
        Initialize a deck of cards.

        """
        self.deck = []

    def populate(self) -> None:
        """
        Populate the deck.

        >>> d = Deck()
        >>> d.populate()
        >>> len(d.deck) == 52
        True
        """
        for i in range(13):
            for j in range(4):
                self.deck.append(Card(SUITS[j], CARDS[i]).__str__())

    def randomize(self) -> None:
        """
        Shuffle the deck in random order.
        """
        random.shuffle(self.deck)

    def split_half(self, difficulty: str) -> Tuple[List[str], List[str]]:
        """
        Splits the deck into half if two players. Number of cards per deck is
        based on difficulty; Easy, Medium or Hard.

        >>> d = Deck()
        >>> d.populate()
        >>> d.randomize()
        >>> deal = d.split_half("Easy")
        >>> len(deal) == 2
        True
        """
        if difficulty == "Easy":
            return self.deck[:4], self.deck[4:8]
        elif difficulty == "Medium":
            return self.deck[:13], self.deck[13:26]
        elif difficulty == "Hard":
            return self.deck[:26], self.deck[26:]

    def split_quad(self) -> Tuple[List[str], List[str], List[str], List[str]]:
        """
        Splits the deck into 4 equal pieces if 4 players.

        >>> d = Deck()
        >>> d.populate()
        >>> d.randomize()
        >>> deal = d.split_quad()
        >>> len(deal) == 4
        True
        """
        return self.deck[:13], self.deck[13:26], self.deck[26:39], \
               self.deck[39:52]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
