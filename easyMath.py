import pygame
import random
import pydoc
from saveGame import saveGame


class EasyMath:
    '''
            Author: Rachel Ha, Lily So
            Purpose: Class for easy level of the Math Mania game, runs 10 questions
    '''

    def __init__(self, screen, game_state):
        '''
            Initialize EasyMath class.
            Randomizes equation question: addition and subtraction.
            Loads images and sounds from files. 

            :param screen: The game screen surface:
            :param game_state: The game state manager:
        '''
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.game_state = game_state

        # setting up font
        self.font = pygame.font.SysFont("arial", 40)

        # dictionary to hold images for numbers
        self.easyMath = {
            "0": pygame.image.load('assets/images/0.png').convert_alpha(),
            "1": pygame.image.load('assets/images/1.png').convert_alpha(),
            "2": pygame.image.load('assets/images/2.png').convert_alpha(),
            "3": pygame.image.load('assets/images/3.png').convert_alpha(),
            "4": pygame.image.load('assets/images/4.png').convert_alpha(),
            "5": pygame.image.load('assets/images/5.png').convert_alpha(),
            "6": pygame.image.load('assets/images/6.png').convert_alpha(),
            "7": pygame.image.load('assets/images/7.png').convert_alpha(),
            "8": pygame.image.load('assets/images/8.png').convert_alpha(),
            "9": pygame.image.load('assets/images/9.png').convert_alpha(),
        }

        # button images
        self.button_img = pygame.image.load(
            "assets/images/mc_button.png").convert_alpha()
        self.button_hover_img = pygame.image.load(
            "assets/images/mc_hover_button.png").convert_alpha()

        # load finshed image
        self.finished = pygame.image.load(
            "assets/images/congrats.png").convert_alpha()

        # load next button
        self.next_button = pygame.image.load(
            "assets/images/next_button.png").convert_alpha()

        # load correct sound
        self.correct_sound = pygame.mixer.Sound(
            "assets/mathSounds/correctSound.mp3")

        # load incorrect sound
        self.incorrect_sound = pygame.mixer.Sound(
            "assets/mathSounds/incorrectSound.mp3")

        # load extra buttons on congrats image
        self.levels_button = pygame.image.load(
            "assets/images/levels.png").convert_alpha()
        self.next_level_button = pygame.image.load(
            "assets/images/nextLevel.png").convert_alpha()
        self.save_game_button = pygame.image.load(
            "assets/images/saveGame.png").convert_alpha()

        # load back button
        self.back_button = pygame.image.load(
            "assets/images/backButton.png").convert_alpha()

        # initialization of variables
        self.operation = random.choice(['adding', 'subtracting'])
        self.math_choice = random.choice(list(self.easyMath.keys()))
        self.math_choice2 = random.choice(
            list(self.easyMath.keys()))  # Initialize math_choice2
        self.eqn_ans = self.answer()  # gets the answer of the eqn
        self.options = self.multiple_choice()
        # new variable to track completion
        self.completed = False

        self.ans_index = 0  # gets the index of the answer

        self.selected_option = None
        self.correct_answer = False
        self.hovered = None
        self.questions_answered = 0
        self.score = 0  # set score
        self.saved = False

        # initialize images for operands
        self.img3 = pygame.transform.scale(
            self.easyMath[self.math_choice], (200, 200))
        self.img4 = pygame.transform.scale(
            self.easyMath[self.math_choice2], (200, 200))

    def always_positive(self):
        '''
            Swap numbers so the answer is always positive.
            :return:
        '''
        if self.math_choice < self.math_choice2:
            # swap choice1 and choice2
            self.math_choice, self.math_choice2 = self.math_choice2, self.math_choice

    def answer(self):
        '''
            Calculate the answer to the equation
            :return: answer
        '''
        if self.operation == 'adding':
            ans = int(self.math_choice) + int(self.math_choice2)
        else:
            self.always_positive()
            ans = int(self.math_choice) - int(self.math_choice2)
        return ans

    def get_random_image1(self):
        '''
            Get a random image from the dictionary
            :return: image
        '''
        img_number = random.randint(1, 5)
        return pygame.transform.scale(pygame.image.load(f'assets/images/{img_number}.png').convert(), (200, 200))

    def get_random_image2(self):
        '''
            Get a random image from the dictionary
            :return: image
        '''
        img_number = random.randint(1, 4)
        return pygame.transform.scale(pygame.image.load(f'assets/images/{img_number}.png').convert(), (200, 200))

    def multiple_choice(self):
        '''
            Generate multiple choice options
            Get 3 other options then add the value of self.eqn answer into list
            :return: generated options
        '''
        keys_list = [
            int(x) for x in self.easyMath]  # convert all key in dict into integer kust
        other_options = []
        for i in range(18):
            if i != self.eqn_ans:
                other_options.append(i)

        options = random.sample(other_options, 3)  # str list

        multiple_choice_options = []  # full list of numeral options
        multiple_choice_options = [self.eqn_ans]
        # extend rest of values by combining the two lists
        multiple_choice_options.extend(options)
        random.shuffle(multiple_choice_options)  # shuffle the list

        self.ans_index = multiple_choice_options.index(
            self.eqn_ans)  # obtain index of answer
        return multiple_choice_options

    # main function to run the game
    def run(self):
        ''' 
            Creates UI for the game and run the game.
            :return:
        '''
        # fill screen with white color
        self.screen.fill("beige")
        pygame.display.set_caption("Math Mania")
        font1 = pygame.font.SysFont("arialblack", 45)
        font2 = pygame.font.SysFont("arialblack", 200)

        # render question text
        img1 = font1.render("Solve the equation.", True, "black")
        self.screen.blit(img1, (140, 20))

        # display back button
        self.screen.blit(self.back_button, (40, 15))

        # display score
        score_text = font1.render("Score: " + str(self.score), True, "black")
        self.screen.blit(score_text, (900, 15))

        # blit operands and operation symbol
        self.screen.blit(self.img3, (15, 250))
        self.screen.blit(self.img4, (300, 250))
        operation_symbol = '+' if self.operation == 'adding' else '-'
        img5 = font2.render(operation_symbol, True, "black")
        self.screen.blit(img5, (200, 200))
        img6 = font2.render("?", True, "black")
        self.screen.blit(img6, (500, 200))

        col_value = 2
        row_value = 2
        button_width = 220
        button_height = 250
        horizontal_space = 25
        vertical_space = 25

        for i, item in enumerate(self.options):
            column = i % col_value
            row = i // row_value
            x = 695 + column * (button_width + horizontal_space)
            y = 100 + row * (button_height + vertical_space)

            button_img = self.button_hover_img if self.hovered == item else self.button_img

            self.screen.blit(button_img, (x, y))
            option_surface = self.font.render(str(item), True, "black")
            option_rect = option_surface.get_rect(
                center=(x + button_width // 2, y + button_height // 2))
            self.screen.blit(option_surface, option_rect)

        # check if user answer is correct or incorrect
        if self.selected_option is not None:
            self.check_answer()
            if self.check_answer():
                self.display_text("Correct! The answer is %s." %
                                  self.eqn_ans, "green")
                self.screen.blit(self.next_button, (1075, 650))
            else:
                self.display_text("Incorrect. The answer is %s." %
                                  self.eqn_ans, "red")
                self.screen.blit(self.next_button, (1075, 650))

        # level complete if 10 questions are answered
        if self.questions_answered == 10:
            # display finished screen
            self.screen.blit(self.finished, (315, 160))
            # show buttons
            self.screen.blit(self.levels_button, (368, 450))
            self.screen.blit(self.save_game_button, (561, 450))
            self.screen.blit(self.next_level_button, (753, 450))
            self.active = False
            self.answered = True

        pygame.display.update()
        self.clock.tick(60)

    # user input
    def user_input(self, event, save):
        '''
            Handle user input including button pressing
            :param event:
            :param save:
            :return:
        '''
        button_width = 220
        button_height = 250
        horizontal_space = 25
        vertical_space = 25

        pos = pygame.mouse.get_pos()

        if not self.completed:
            if event.type == pygame.MOUSEBUTTONDOWN and self.selected_option is None:
                # Handle button clicks during gameplay
                back_button = pygame.Rect(40, 15, 70, 70)
                if back_button.collidepoint(pos):
                    self.__init__(self.screen, self.game_state)
                    self.game_state.set_state('mathLevels')

                for i, option in enumerate(self.options):
                    column = i % 2
                    row = i // 2
                    x = 695 + column * (button_width + horizontal_space)
                    y = 100 + row * (button_height + vertical_space)
                    option_rectangle = pygame.Rect(
                        x, y, button_width, button_height)
                    if option_rectangle.collidepoint(pos):
                        self.selected_option = option

                        if self.check_answer():
                            self.correct_sound.play(loops=0)
                        else:
                            self.incorrect_sound.play(loops=0)
            # next button
            elif event.type == pygame.MOUSEBUTTONDOWN and self.selected_option is not None:
                next_rect = pygame.Rect(1075, 650, 175, 50)
                if next_rect.collidepoint(pos):
                    if self.check_answer():
                        self.update_score()
                        self.next_question()
                    else:
                        self.next_question()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.selected_option is not None:
                    self.next_question()
                else:
                    self.selected_option = None
            # mouse hover event
            elif event.type == pygame.MOUSEMOTION:
                self.mouseover()
        else:
            # Enable buttons only when clicking on the Finished screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                levels_rect = pygame.Rect(368, 450, 159, 65)
                saveGame_rect = pygame.Rect(561, 450, 159, 65)
                nextLevel_rect = pygame.Rect(753, 450, 159, 65)
                if levels_rect.collidepoint(pos):
                    if self.saved == False:
                        self.__init__(self.screen, self.game_state)
                    self.game_state.set_state('mathLevels')
                if saveGame_rect.collidepoint(pos):
                    self.saved = True
                    saveGame(save, 2, 1)
                if nextLevel_rect.collidepoint(pos):
                    if self.saved == False:
                        self.__init__(self.screen, self.game_state)
                    self.game_state.set_state('mathMed')

    # score
    def update_score(self):
        '''
            Update player's score
            :return:
        '''
        self.score += 10

    def check_answer(self):
        '''
            Check if the selected option matches the correct answer
            :return: True if correct, false otherwise
        '''
        if self.selected_option == self.eqn_ans:
            return True
        else:
            return False

    def mouseover(self):
        '''
            Handle mouse hover events
            :return:
        '''
        button_width = 220
        button_height = 250
        horizontal_space = 25
        vertical_space = 25

        pos = pygame.mouse.get_pos()

        # check if mouse is over any button and update hovered option
        for i, item in enumerate(self.options):
            column = i % 2
            row = i // 2
            x = 695 + column * (button_width + horizontal_space)
            y = 100 + row * (button_height + vertical_space)
            option_rectangle = pygame.Rect(x, y, button_width, button_height)
            if option_rectangle.collidepoint(pos):
                self.hovered = item
                return
        self.hovered = None

    def display_text(self, message, colour):
        '''
            Display answer on screen
            :param message:
            :param colour: Colour of text
        '''
        text = self.font.render(message, True, colour)
        # get text rectangle and center it on the screen
        text_rect = text.get_rect(center=(1280 // 2, 675))
        self.screen.blit(text, text_rect)

    def next_question(self):
        '''
            Generate a new question.
            :return:
        '''
        self.operation = random.choice(['adding', 'subtracting'])
        self.math_choice = random.choice(list(self.easyMath.keys()))
        self.math_choice2 = random.choice(
            list(self.easyMath.keys()))  # Initialize math_choice2
        self.eqn_ans = self.answer()  # gets the answer of the new eqn
        self.options = self.multiple_choice()  # get new choices
        self.ans_index = 0
        self.selected_option = None
        self.correct_answer = False
        self.questions_answered += 1
        # Check if 10 questions are answered to mark completion
        if self.questions_answered == 10:
            self.completed = True

        # initialize images for operands
        self.img3 = pygame.transform.scale(
            self.easyMath[self.math_choice], (200, 200))
        self.img4 = pygame.transform.scale(
            self.easyMath[self.math_choice2], (200, 200))
