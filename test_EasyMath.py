import pydoc
import unittest
import pygame
from unittest.mock import MagicMock
from easyMath import EasyMath


class TestEasyMath(unittest.TestCase):
    '''
            Author: Rachel Ha
            Purpose: Unit testing for EasyMath
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
        em = EasyMath(self.screen, None)
        em.math_choice = 2
        em.math_choice2 = 4
        em.always_positive()
        self.assertEqual(em.math_choice, 4)
        self.assertEqual(em.math_choice2, 2)

    def test_answer_addition(self):
        '''
            Test: function answer_addition
            Test addition algorithm
            :return:
        '''
        em = EasyMath(self.screen, None)
        em.operation = 'adding'
        em.math_choice = '2'
        em.math_choice2 = '4'
        self.assertEqual(em.answer(), 6)

    def test_answer_subtraction(self):
        '''
            Test: function answer_subtraction
            Test subtraction algorithm
            :return:
        '''
        em = EasyMath(self.screen, None)
        em.operation = 'subtracting'
        em.math_choice = '4'
        em.math_choice2 = '2'
        self.assertEqual(em.answer(), 2)

    def test_get_random_image1(self):
        '''
            Test: function get_random_image1
            Test if the function is able to load images
            :return:
        '''
        em = EasyMath(self.screen, None)
        pygame.image.load = MagicMock(return_value=pygame.Surface((200, 200)))
        img = em.get_random_image1()
        self.assertIsInstance(img, pygame.Surface)

    def test_get_random_image2(self):
        '''
            Test: function get_random_image2
            Test if the function is able to load images
            :return:
        '''
        em = EasyMath(self.screen, None)
        pygame.image.load = MagicMock(return_value=pygame.Surface((200, 200)))
        img = em.get_random_image2()
        self.assertIsInstance(img, pygame.Surface)

    def test_multiple_choice(self):
        '''
            Test: function multiple_choice
            Test multiple choice options
            :return:
        '''
        em = EasyMath(self.screen, None)
        em.eqn_ans = 8
        em.easyMath = {str(i): pygame.Surface((200, 200)) for i in range(10)}
        options = em.multiple_choice()
        self.assertIn(8, options)
        self.assertEqual(len(options), 4)

    def test_check_answer_correct(self):
        '''
            Test: function check_answer
            Test using correct answer
            :return:
        '''
        em = EasyMath(self.screen, None)
        em.selected_option = 5
        em.eqn_ans = 5
        self.assertTrue(em.check_answer())

    def test_check_answer_incorrect(self):
        '''
            Test: function check_answer
            Test using incorrect answer
            :return:
        '''
        em = EasyMath(self.screen, None)
        em.selected_option = 3
        em.eqn_ans = 5
        self.assertFalse(em.check_answer())

    def test_next_question(self):
        '''
            Test: function next_question
            Test if the equation answer and options are not None
            :return:
        '''
        em = EasyMath(self.screen, None)
        em.next_question()
        self.assertNotEqual(em.eqn_ans, None)
        self.assertNotEqual(em.options, None)


if __name__ == '__main__':
    unittest.main()
