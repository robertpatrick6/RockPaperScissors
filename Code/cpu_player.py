# Author: Robert Patrick
#
# This script contains a class implementing the functionality of the
# CPU player in the rock, paper, scissors game


import random
from combined_learner import CombinedLearner


MOVES = ["rock","paper","scissors"]


class CPUPlayer:

    # Class variables
    # --------------------
    # self.learner
    # self.memory_list
    # self.current_interval_move
    # self.MAX_MOVE_MEMORY
    # self.UPDATE_INTERVAL


    # Constructor
    # --------------------
    # Creates a new cpu player and its internals
    def __init__(self):
        self.learner = None
        
        self.UPDATE_INTERVAL = 6
        self.MAX_MOVE_MEMORY = 50

        self.current_interval_move = 0

        self.memory_list = []


    # Private methods
    # --------------------
    # Updates learner after a certain interval of moves have
    # been made
    # The learner will use 5-move sequences as features, with
    # the following move being the classifier
    def _update_learner(self):
        move_x = []
        move_y = []
        
        for i in range(len(self.memory_list) - 5):
            move_x.append(self.memory_list[i:i+5])
            move_y.append(self.memory_list[i+5])

        self.learner = CombinedLearner(move_x, move_y)


    # Public methods
    # --------------------
    # Makes a move based upon predictions from previous 5 moves
    def make_move(self):
        if (self.learner == None):
            return random.choice(MOVES)

        else:
            prediction = self.learner.predict([self.memory_list[-5:]])[0]

            if (prediction == 0):
                return "paper"
            elif (prediction == 1):
                return "scissors"
            else:
                return "rock"

    # Takes the players previous move and adds it to a list to
    # allow for a memory of the previous moves in the game,
    # up to a certain maximum memory
    def remember_moves(self, player_move):
        if (player_move == "rock"):
            self.memory_list.append(0)
        elif (player_move == "paper"):
            self.memory_list.append(1)
        else:
            self.memory_list.append(2)

        if (len(self.memory_list) > self.MAX_MOVE_MEMORY):
            self.memory_list = self.memory_list[1:]

        self.current_interval_move += 1
        if (self.current_interval_move >= self.UPDATE_INTERVAL):
            self.current_interval_move = 0
            self._update_learner()
