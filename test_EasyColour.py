import pydoc
import unittest
import pygame
from EasyColour import EasyColour


class TestEasyColour(unittest.TestCase):
    '''
            Author: Ethne Au
            Purpose: Unit testing for EasyColour
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

    def test_new_question(self):
        '''
            Test: function new_question
            Should not be equal, should randomize the colours
            :return:
        '''
        easy = EasyColour(self.screen, None)
        not_expected = ["Red", "Orange", "Yellow", "Green"]
        easy.new_question()
        self.assertNotEqual(not_expected, easy.choices)


if __name__ == '__main__':
    unittest.main()
