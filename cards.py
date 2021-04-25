#-------------------------------------------------------
# Name:        cards.py
# Purpose:     Education purposes only, copying will be subject to plagiarism
# Author:      Syed Natiq Ali Abidi
# Created:     23-April-2021
# Updated:     25-April-2021
#-------------------------------------------------------

SUITS = ["Clubs", "Spades", "Hearts", "Diamonds"]
CARDS = ["ACE", "KING", "QUEEN", "JACK", "2", "3", "4", "5", "6", "7", "8",
         "9", "10"]

class Card:
    """
    Represents a card that will be used by players.

    === Public Attributes ===
    suit:
        The suit of the card.
    value:
        The type of the card.
    power:
        The strength of the card.
    """
    suit : str
    value : str
    power : int

    def __init__(self, suit: str, value: str) -> None:
        """
        Creates a card object.

        """
        self.suit = suit
        self.value = value
        self.power = 0

        if self.value == "ACE":
            self.power = 20
        elif self.value == "KING":
            self.power = 19
        elif self.value == "QUEEN":
            self.power = 18
        elif self.value == "JACK":
            self.power = 17
        else:
            for x in range(2, 11):
                if self.value == str(x):
                    self.power = x

    def __str__(self) -> str:
        """
        Creates a string representation of the card.
        """
        return f'{self.value}' + " of " + f'{self.suit}'

    def compare(self, other) -> bool:
        """
        Return True if this card is stronger than the other card.

        Precondition:

        - Cards that are being compared must have the same suit.

        >>> c1 = Card("Diamonds", "ACE")
        >>> c2 = Card("Diamonds", "JACK")
        >>> c1.compare(c2)
        True
        >>> c3 = Card("Diamonds", "QUEEN")
        >>> c2.compare(c3)
        False
        """
        return self.power > other.power

if __name__ == "__main__":
    import doctest
    doctest.testmod()
