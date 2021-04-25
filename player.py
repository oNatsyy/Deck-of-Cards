#-------------------------------------------------------
# Name:        player.py
# Purpose:     Education purposes only, copying will be subject to plagiarism
# Author:      Syed Natiq Ali Abidi
# Created:     23-April-2021
# Updated:     25-April-2021
#-------------------------------------------------------


from typing import List
from cards import Card
from deck import Deck

class Player:
    """
    Represents a player that will play the cards.

    === Public Attributes ===
    name:
        Name of the player.
    points:
        The number of points that the player has.
    player_deck:
        The collection of cards allocated to the player. Cards are allocated
        evenly amongst the players.
    """
    name : str
    points : int
    player_deck : List[Card]

    def __init__(self, name: str) -> None:
        """
        Initialize a player with the given name and allocated deck. The player's
        current card is None at the start.

        """
        self.name = name
        self.points = 0
        self.player_deck = []

    def __str__(self) -> str:
        """
        String representation of the player.

        >>> p1 = Player("Ali")
        >>> str(p1)
        'Ali has joined the game!'
        """
        return f'{self.name}' + ' has joined the game!'

    def play_move(self, type: str, val: str) -> bool:
        """
        Plays a move from the players deck. <type> represents the suit and
        <val> represents the value of the card.

        >>> d = Deck()
        >>> d.populate()
        >>> d.randomize()
        >>> p1 = Player("Ali")
        >>> p2 = Player("Mohammad")
        >>> p1.play_move('Clubs', 'KING')
        Invalid Move
        False
        """
        player_card = Card(type, val)

        if str(player_card) in self.player_deck:

            for item in self.player_deck:
                if item == str(player_card):
                    self.player_deck.remove(item)

            self._current_card = None

            print(f'{self.name}' + ' has played ' + str(player_card))
            return True

        else:
            print("Invalid Move")
            return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
