import unittest
import pygame
from unittest.mock import Mock
from animalEasy import AnimalEasy
import pydoc

class TestAnimalEasy(unittest.TestCase):
    """
    Author: Lily So
    This class is used to test the AnimalEasy class.
    """
    def setUp(self):
        """
        This method sets up the test.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.animals = {
            "Lion": {"image": Mock()},
            "Tiger": {"image": Mock()},
            "Bear": {"image": Mock()},
            "Horse": {"image": Mock()},
            "Cat": {"image": Mock()},
        }
        self.aEasy = AnimalEasy(self.screen, self.animals, None)

    def tearDown(self):
        """
        This method closes the test.
        """
        pygame.quit()

    def test_multiple_choice(self):
        """
        This method tests the multiple_choice method.
        """
        animal_keys = ["Lion", "Tiger", "Bear", "Horse", "Cat"]
        
        options = self.aEasy.multiple_choice(animal_keys)

        self.assertIsInstance(options, list)
        self.assertEqual(len(options), 4)

    def test_check_answer(self):
        """
        This method tests the check_answer method.
        """
        self.aEasy.correct_answer = "Lion"
        self.aEasy.selected_option = "Lion"

        self.assertFalse(self.aEasy.check_answer())


if __name__ == '__main__':
    unittest.main()
