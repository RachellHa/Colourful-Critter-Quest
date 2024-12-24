import pygame
import pydoc

class GameState:
    """
    Author: Lily So
    This class is used to store the current state of the game.
    """
    def __init__(self, curr_state):
        """
        This method initializes the current state of the game.
        :param curr_state: the current state of the game
        """
        self.curr_state = curr_state
        self.prev_state = None
    
    def get_state(self):
        """
        This method returns the current state of the game.
        :return: the current state of the game
        """
        return self.curr_state
        
    def set_state(self, new_state):
        """
        This method sets the current state of the game.
        :param new_state: the new state of the game
        """
        self.prev_state = self.curr_state
        self.curr_state = new_state

    def get_prev_state(self):
        """
        This method returns the previous state of the game.
        :return: the previous state of the game
        """
        return self.prev_state
    