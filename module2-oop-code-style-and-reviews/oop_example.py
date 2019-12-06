from random import random
#This is actually the docstring for the file itself:
"""
Classes to represent games.
"""
#convention for classes is capital letter for class
#lowercase for instances
class Game:
    """
    General representation of an abstract game
    """
    # features or fields inside of a class
    # remember you can set defaults to specific values.
    def __init__(self,rounds=2, player1="Nicole", player2="Kumar"):
        self.rounds = rounds
        self.steps = 5
        self.player1 = player1
        self.player2 = player2

    def print_players(self):
        """
        Prints out the game players, and their relationship.
        """
        print(f'{self.player1} is playing {self.player2}')

    def add_round(self):
        """
        increment rounds by 1
        """
        self.rounds += 1

    def winner(self):
        """
        randomly pick a winner
        """
        return self.player1 if random()>0.5 else self.player2

class Tic(Game):
    """
    subclass of Game for Tic Tac Toe
    """
    def __init__(self,rounds = 3, player1 = 'Superman', player2 = 'Stephanie'):
        super().__init__(rounds,player1,player2)

    def print_players(self):
        print(f'{self.player1}, is playing tic tac toe with {self.player2}')
