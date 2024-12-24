import pydoc
import unittest
import pygame
from unittest.mock import MagicMock
from hardMath import HardMath


class TestHardMath(unittest.TestCase):
    '''
            Author: Rachel Ha
            Purpose: Unit testing for HardMath
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

    def test_always_positive(self):
        '''
            Test: function always_positive
            Check return value is always a positive integer
            :return:
        '''
        hm = HardMath(self.screen, None)
        hm.math_choice = 2
        hm.math_choice2 = 4
        hm.always_positive()
        self.assertEqual(hm.math_choice, 4)
        self.assertEqual(hm.math_choice2, 2)

    def test_answer_multiplication(self):
        '''
            Test: function answer_multiplication
            Test multiplication algorithm
            :return:
        '''
        hm = HardMath(self.screen, None)
        hm.operation = 'multiple'
        hm.math_choice = 2
        hm.math_choice2 = 4
        self.assertEqual(hm.answer(), 8)

    def test_answer_division(self):
        '''
            Test: function answer_division
            Test division algorithm
            :return:
        '''
        hm = HardMath(self.screen, None)
        hm.operation = 'divide'
        hm.math_choice = 4
        hm.math_choice2 = 2
        self.assertEqual(hm.answer(), 2.0)

    def test_get_random_image1(self):
        '''
            Test: function get_random_image1
            Test if the function is able to load images
            :return:
        '''
        hm = HardMath(self.screen, None)
        pygame.image.load = MagicMock(return_value=pygame.Surface((200, 200)))
        img = hm.get_random_image1()
        self.assertIsInstance(img, pygame.Surface)

    def test_get_random_image2(self):
        '''
            Test: function get_random_image2
            Test if the function is able to load images
            :return:
        '''
        hm = HardMath(self.screen, None)
        pygame.image.load = MagicMock(return_value=pygame.Surface((200, 200)))
        img = hm.get_random_image2()
        self.assertIsInstance(img, pygame.Surface)

    def test_multiple_choice(self):
        '''
            Test: function multiple_choice
            Test multiple choice options
            :return:
        '''
        hm = HardMath(self.screen, None)
        hm.eqn_ans = 8
        hm.hardMath = {str(i): pygame.Surface((200, 200)) for i in range(10)}
        options = hm.multiple_choice()
        self.assertIn(8, options)
        self.assertEqual(len(options), 4)

    def test_check_answer_correct(self):
        '''
            Test: function check_answer
            Test using correct answer
            :return:
        '''
        hm = HardMath(self.screen, None)
        hm.selected_option = 5
        hm.eqn_ans = 5
        self.assertTrue(hm.check_answer())

    def test_check_answer_incorrect(self):
        '''
            Test: function check_answer
            Test using incorrect answer
            :return:
        '''
        hm = HardMath(self.screen, None)
        hm.selected_option = 3
        hm.eqn_ans = 5
        self.assertFalse(hm.check_answer())

    def test_next_question(self):
        '''
            Test: function next_question
            Test if the equation answer and options are not None
            :return:
        '''
        hm = HardMath(self.screen, None)
        hm.next_question()
        self.assertNotEqual(hm.eqn_ans, None)
        self.assertNotEqual(hm.options, None)


if __name__ == '__main__':
    unittest.main()
