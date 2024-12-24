import pydoc
import unittest
import pygame
from MedColour import MedColour


class TestMedColour(unittest.TestCase):
    '''
            Author: Ethne Au
            Purpose: Unit testing for MedColour
    '''

    def setUp(self):
        '''
            Set up pygame
            :return:
        '''
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))

    def tearDown(self):
        '''
            Quit pygame
            :return:
        '''
        pygame.quit()

    def test_randomize_choices(self):
        '''
            Test: function randomize_choices
            First assert: check if the answer is in the choices
            Second assert: check if choices are randomized
            :return:
        '''
        med = MedColour(self.screen, None)
        med.question = ["Blue", "Yellow", "Green"]
        not_expected = ["Red", "Orange", "Yellow", "Green"]
        options = med.randomize_choices()
        self.assertTrue("Green" in options)
        self.assertNotEqual(not_expected, med.choices)


if __name__ == '__main__':
    unittest.main()
