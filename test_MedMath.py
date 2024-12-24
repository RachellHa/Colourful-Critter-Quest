import pydoc
import unittest
import pygame
from unittest.mock import MagicMock
from medMath import MedMath


class TestMedMath(unittest.TestCase):
    '''
            Author: Rachel Ha
            Purpose: Unit testing for MedMath
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
        mm = MedMath(self.screen, None)
        mm.math_choice = 2
        mm.math_choice2 = 4
        mm.always_positive()
        self.assertEqual(mm.math_choice, 4)
        self.assertEqual(mm.math_choice2, 2)

    def test_answer_addition(self):
        '''
            Test: function answer_addition
            Test addition algorithm
            :return:
        '''
        mm = MedMath(self.screen, None)
        mm.operation = 'adding'
        mm.math_choice = '2'
        mm.math_choice2 = '4'
        self.assertEqual(mm.answer(), 6)

    def test_answer_subtraction(self):
        '''
            Test: function answer_subtraction
            Test subtraction algorithm
            :return:
        '''
        mm = MedMath(self.screen, None)
        mm.operation = 'subtracting'
        mm.math_choice = '4'
        mm.math_choice2 = '2'
        self.assertEqual(mm.answer(), 2)

    def test_get_random_image1(self):
        '''
            Test: function get_random_image1
            Test if the function is able to load images
            :return:
        '''
        mm = MedMath(self.screen, None)
        pygame.image.load = MagicMock(return_value=pygame.Surface((200, 200)))
        img = mm.get_random_image1()
        self.assertIsInstance(img, pygame.Surface)

    def test_get_random_image2(self):
        '''
            Test: function get_random_image2
            Test if the function is able to load images
            :return:
        '''
        mm = MedMath(self.screen, None)
        pygame.image.load = MagicMock(return_value=pygame.Surface((200, 200)))
        img = mm.get_random_image2()
        self.assertIsInstance(img, pygame.Surface)

    def test_multiple_choice(self):
        '''
            Test: function multiple_choice
            Test multiple choice options
            :return:
        '''
        mm = MedMath(self.screen, None)
        mm.eqn_ans = 8
        mm.medMath = {str(i): pygame.Surface((200, 200)) for i in range(50)}
        options = mm.multiple_choice()
        self.assertIn(8, options)
        self.assertEqual(len(options), 4)

    def test_check_answer_correct(self):
        '''
            Test: function check_answer
            Test using correct answer
            :return:
        '''
        mm = MedMath(self.screen, None)
        mm.selected_option = 5
        mm.eqn_ans = 5
        self.assertTrue(mm.check_answer())

    def test_check_answer_incorrect(self):
        '''
            Test: function check_answer
            Test using incorrect answer
            :return:
        '''
        mm = MedMath(self.screen, None)
        mm.selected_option = 3
        mm.eqn_ans = 5
        self.assertFalse(mm.check_answer())

    def test_next_question(self):
        '''
            Test: function next_question
            Test if the equation answer and options are not None
            :return:
        '''
        mm = MedMath(self.screen, None)
        mm.next_question()
        self.assertNotEqual(mm.eqn_ans, None)
        self.assertNotEqual(mm.options, None)


if __name__ == '__main__':
    unittest.main()
