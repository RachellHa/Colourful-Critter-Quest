import unittest
import pygame
from unittest.mock import Mock
from animalMed import AnimalMed
import pydoc

class TestAnimalMed(unittest.TestCase):
    """
    Author: Lily So
    This class is used to test the AnimalMed class.
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
        self.aMed = AnimalMed(self.screen, self.animals, None)

    def tearDown(self):
        """
        This method closes the test.
        """
        pygame.quit()

    def test_multiple_choice(self):
        """
        This method tests the multiple_choice method.
        """
        animal_keys = ["Alpaca", "Coyote", "Donkey", "Flamingo", "Yak"]
        
        options = self.aMed.multiple_choice(animal_keys)

        self.assertIsInstance(options, list)
        self.assertEqual(len(options), 4)

    def test_check_answer(self):
        """
        This method tests the check_answer method.
        """
        self.aMed.correct_answer = "Alpaca"
        self.aMed.selected_option = "Alpaca"

        self.assertFalse(self.aMed.check_answer())

if __name__ == '__main__':
    unittest.main()