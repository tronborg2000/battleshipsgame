import copy as c
import os
import random as rand

"""
Defining the Game class to make it easier to 
understand the code further in the project
"""


class Game(object):
    def __init__(self, players):
        self.guesses = 5
        self.player_list = []
        for player in range(players):
            self.player_list.append(self.guesses)
        self.current_player = 1
        self.board = self.create_matrix(5, 5)
        self.board_visible = c.deepcopy(self.board)
        self.ship_row = rand.randint(0, 4)
        self.ship_col = rand.randint(0, 4)
        self.guess_row = 0
        self.guess_col = 0
