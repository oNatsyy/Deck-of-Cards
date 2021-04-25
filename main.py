#-------------------------------------------------------
# Name:        main.py
# Purpose:     Education purposes only, copying will be subject to plagiarism
# Author:      Syed Natiq Ali Abidi
# Created:     23-April-2021
# Updated:     25-April-2021
#-------------------------------------------------------


from typing import Tuple, List
from cards import Card
from deck import Deck
from player import Player

def play_cards_two(difficulty: str) -> Tuple[Player, Player]:
    """
    Creates a deck and splits it amongst 2 players.

    <difficulty> can be Easy, Medium or Hard.

    """
    d = Deck()
    d.populate()
    d.randomize()

    name1 = input("Enter player 1 name: ")
    name2 = input("Enter player 2 name: ")

    p1 = Player(name1)
    p2 = Player(name2)

    deck1, deck2 = d.split_half(difficulty)

    p1.player_deck.extend(deck1)
    p2.player_deck.extend(deck2)

    return p1, p2

def game_menu(p: Player) -> str:
    """
    A simple text UI for the game's menu.
    """

    print("-------------------------------------------------------")
    user_choice = input("What would " + str(p.name) + " like to do?:\n"
                                                      "1 = 'Show deck'\n"
                                                      "2 = 'Play your turn'\n"
                                                      "q = quit\nSelection: ")
    print("-------------------------------------------------------")

    return user_choice

def game_choice(p: Player) -> List:
    """
    Return True or False based on the player's choice.
    """

    user_choice = game_menu(p)

    if user_choice == "1":
        print(p.player_deck)
        return [True]

    elif user_choice == "2":
        suit, val = input("Enter your card's suit: "), input("Enter your card's value: ")
        c = Card(suit, val)
        print("\n")
        move = p.play_move(suit, val)
        print("\n")

        if move:
            final = [False]
            final.append(c)
            return final
        else:
            return [True]

    elif user_choice == "q":
        print("Game over!")
        return [False]


def play(size: int, difficulty: str) -> None:
    """
    Play the game, <size> represents the player size for this game.

    Rules:
        - Same suits, higher value gets you a point.
        - Different suits will always result in 0 points for both players
          regardless of card power.

    """
    if size == 2:

        p1, p2 = play_cards_two(difficulty)

        curr_round = 1

        while len(p1.player_deck) != 0 or len(p2.player_deck) != 0:

            print("\nRound " + str(curr_round) + " has started!"  + "\n")

            curr_round += 1

            p1_choice = True
            p2_choice = True

            choice_list = []

            while p1_choice:

                choice = game_choice(p1)

                if choice != [] and choice is not None:
                    if choice[0] == False and len(choice) == 2:
                        choice_list.append(choice[1])
                        p1_choice = False
                    elif choice[0] == False and len(choice) == 1:
                        p1_choice = False
                else:
                    print("\nInvalid Selection\n")

            while p2_choice:

                choice = game_choice(p2)

                if choice != [] and choice is not None:
                    if choice[0] == False and len(choice) == 2:
                        choice_list.append(choice[1])
                        p2_choice = False

                    elif choice[0] == False and len(choice) == 1:
                        p2_choice = False
                else:
                    print("\nInvalid Selection\n")

            if choice_list[0].suit == choice_list[1].suit:
                if choice_list[0].compare(choice_list[1]):
                    print("----------------------------------------------------"
                          "---")
                    print("\n" + str(p1.name) + " has won the round and "
                                                "secure a point!\n")
                    p1.points += 1

                elif choice_list[1].compare(choice_list[0]):
                    print("---------------------------------------------------"
                          "----")
                    print("\n" + str(p2.name) + " has won the round "
                                                "and secure a point!\n")
                    p2.points += 1
            else:
                print("-------------------------------------------------------")
                print("\nWe have different suits so no points awarded!\n")
                print("-------------------------------------------------------")

        if p1.points > p2.points:
            print("Congratulations! " + str(p1.name) + " has won the game with "
                  + str(p1.points) + " point(s)!" )
        elif p2.points > p1.points:
            print("Congratulations! " + str(p2.name) + " has won the game with "
                  + str(p2.points) + " point(s)!" )
        else:
            print("The game has ended with a tie!")



if __name__ == "__main__":
    play(2, "Easy")  #  Change this to support more player size and different
                     #  difficulty.
