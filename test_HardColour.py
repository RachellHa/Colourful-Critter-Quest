import pydoc
import unittest
import pygame
from HardColour import HardColour


class TestHardColour(unittest.TestCase):
    '''
            Author: Ethne Au
            Purpose: Unit testing for HardColour
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

    def test_check_answer(self):
        '''
            Test: function randomize_choices
            Check if answer does not match unexpected answer
            :return:
        '''
        hard = HardColour(self.screen, None)
        hard.question[2] = "Blue"
        result = hard.check_answer("Orange")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
