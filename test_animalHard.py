import unittest
import pygame
from unittest.mock import Mock
from animalHard import AnimalHard
import pydoc

class TestAnimalHard(unittest.TestCase):
    """
    Author: Lily So
    This class is used to test the AnimalHard class.
    """
    def setUp(self):
        """
        This method sets up the test.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.animals = {
            "Alpaca": {"image": Mock()},
            "Coyote": {"image": Mock()},
            "Donkey": {"image": Mock()},
            "Flamingo": {"image": Mock()},
            "Yak": {"image": Mock()},
        }
        self.aHard = AnimalHard(self.screen, self.animals, None)

    def tearDown(self):
        """
        This method closes the test.
        """
        pygame.quit()

    def test_shuffle_options(self):
        """
        This method tests the shuffle_options method.
        """
        options = self.aHard.shuffle_options(self.animals)

        self.assertIsInstance(options, list)

    def test_check_answer(self):
        """
        This method tests the check_answer method.
        """
        self.aHard.correct_answer = "Alpaca"
        user_input = "alpaca"

        self.assertFalse(self.aHard.check_answer(user_input))
    
if __name__ == '__main__':
    unittest.main()