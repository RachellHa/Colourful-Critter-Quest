import pydoc
import pygame
import random
from saveGame import saveGame


class EasyColour:
    '''
        Author: Michelle Ko, Ethne Au, Lily So
        Purpose: Class for easy level of the Rainbow Rumble game, runs 10 questions
    '''

    def __init__(self, screen, game_state):
        '''
        Initialize EasyColour class.
        Create colour dictionary containing possible options/questions.
        Loads images and sounds from files. 

        :param screen: The game screen surface:
        :param game_state: The game state manager:
        '''
        self.font = pygame.font.SysFont("arial", 40)  # load font
        self.game_state = game_state
        # initialize window
        self.screen = screen
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Rainbow Rumble')

        self.colours = {
            # dictionary containing colours and their hex codes
            "Red": "#e63c3c",
            "Orange": "#e69545",
            "Yellow": "#f5e14e",
            "Green": "#4be34b",
            "Blue": "#2a79f7",
            "Purple": "#6e2999",
            "Pink": "#e69eab",
            "Black": "#000000",
            "White": "#FFFFFF",
            "Brown": "#523730",
            "Gray": "#616161"
        }

        self.correct_answer = False
        self.incorrect_answer = False
        self.play_sound = False

        self.next_button = pygame.image.load(
            "assets/colourEasyImgs/next_button.png").convert_alpha()  # next button to the next question
        # load correct sound
        self.correct_sound = pygame.mixer.Sound(
            "assets/colourSounds/correctSound.mp3")

        # load incorrect sound
        self.incorrect_sound = pygame.mixer.Sound(
            "assets/colourSounds/incorrectSound.mp3")

        # button images
        self.button_img = pygame.image.load(
            "assets/colourEasyImgs/mc_button.png").convert_alpha()
        self.button_hover_img = pygame.image.load(
            "assets/colourEasyImgs/mc_hover_button.png").convert_alpha()

        # import congrats images/buttons
        self.congrats = pygame.image.load(
            "assets/colourEasyImgs/congrats.png").convert_alpha()
        # load extra buttons on congrats image
        self.levels_button = pygame.image.load(
            "assets/colourEasyImgs/levels.png").convert_alpha()
        self.next_level_button = pygame.image.load(
            "assets/colourEasyImgs/nextLevel.png").convert_alpha()
        self.save_game_button = pygame.image.load(
            "assets/colourEasyImgs/saveGame.png").convert_alpha()

        # load backbutton
        self.back_button = pygame.image.load(
            "assets/colourEasyImgs/backButton.png").convert_alpha()

        self.questions_answered = 0
        self.answered = False  # if question is answered
        self.new_question()
        self.active = True
        self.score = 0  # set score
        self.saved = False

    def new_question(self):
        '''
        Generate a new question.
        :return:
        '''
        self.choice = random.choice(list(self.colours.values()))
        self.choice_key = None
        for key, value in self.colours.items():
            if value == self.choice:
                self.choice_key = key
                break
        self.choices = [self.choice_key]

        # Randomly select three incorrect answers
        while len(self.choices) < 4:
            random_color = random.choice(list(self.colours.keys()))
            if random_color not in self.choices:
                self.choices.append(random_color)

        # Shuffle the choices
        random.shuffle(self.choices)

        self.correct_answer = False
        self.incorrect_answer = False
        self.play_sound = False
        self.hovered = None  # check if hovered or not
        self.questions_answered += 1

    def run(self):
        ''' 
        Creates UI for the game
        :return:
        '''
        pygame.display.set_caption('Rainbow Rumble')
        self.screen.fill("beige")
        font1 = pygame.font.SysFont("arialblack", 45)
        title = font1.render("What colour is this?", True, "black")
        self.screen.blit(title, (140, 20))

        # display colour
        colour_border = (203, 236, 164)
        colour_rect = pygame.Rect((160, 120, 410, 510))
        pygame.draw.rect(self.screen, colour_border, (140, 100, 450, 550))
        pygame.draw.rect(self.screen, self.choice, colour_rect)

        # display back button
        self.screen.blit(self.back_button, (40, 15))

        # display score
        font1 = pygame.font.SysFont("arialblack", 40)
        score_text = font1.render("Score: " + str(self.score), True, "black")
        self.screen.blit(score_text, (1010, 15))

        # multiple choice questions
        col_value = 2
        row_value = 2
        button_width = 220
        button_height = 250
        horizontal_space = 25
        vertical_space = 25

        for i, item in enumerate(self.choices):
            column = i % col_value
            row = i // row_value
            x = 695 + column * (button_width + horizontal_space)
            y = 100 + row * (button_height + vertical_space)

            button_img = self.button_hover_img if self.hovered == item else self.button_img

            self.screen.blit(button_img, (x, y))
            option_surface = self.font.render(item, True, "black")
            option_rect = option_surface.get_rect(
                center=(x + button_width // 2, y + button_height // 2))
            self.screen.blit(option_surface, option_rect)
        self.message()

        # game finished
        if self.questions_answered == 11:
            self.active = False
            self.screen.blit(self.congrats, (315, 160))
            # show buttons
            self.screen.blit(self.levels_button, (368, 450))
            self.screen.blit(self.save_game_button, (561, 450))
            self.screen.blit(self.next_level_button, (753, 450))

        pygame.display.update()
        self.clock.tick(60)

    def user_input(self, event, save):
        '''
        Handle user input including button pressing
        :param event:
        :param save:
        :return:
        '''
        # multiple choice question buttons parameters
        button_width = 220
        button_height = 250
        horizontal_space = 25
        vertical_space = 25

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # back button
            back_button = pygame.Rect(40, 15, 70, 70)
            if back_button.collidepoint(pos):
                self.__init__(self.screen, self.game_state)
                self.game_state.set_state('colourLevels')
            # game finished
            if self.questions_answered == 11:
                self.active = False
                levels_rect = pygame.Rect(368, 450, 159, 65)
                saveGame_rect = pygame.Rect(561, 450, 159, 65)
                nextLevel_rect = pygame.Rect(753, 450, 159, 65)
                if saveGame_rect.collidepoint(pos):
                    self.saved = True
                    saveGame(save, 1, 1)
                if levels_rect.collidepoint(pos):
                    if self.saved == False:
                        self.__init__(self.screen, self.game_state)
                    self.game_state.set_state('colourLevels')
                if nextLevel_rect.collidepoint(pos):
                    if self.saved == False:
                        self.__init__(self.screen, self.game_state)
                    self.game_state.set_state('colourMed')
            # multiple choice questions
            if self.active:
                for i, option in enumerate(self.choices):
                    column = i % 2
                    row = i // 2
                    x = 695 + column * (button_width + horizontal_space)
                    y = 100 + row * (button_height + vertical_space)
                    option_rectangle = pygame.Rect(
                        x, y, button_width, button_height)
                    if option_rectangle.collidepoint(pos):
                        clicked_color = option
                        self.answered = True
                        # check answer
                        if clicked_color == self.choice_key:
                            self.correct_answer = True
                        else:
                            self.incorrect_answer = True
                if self.answered:  # user presses button, go to next question
                    next_rect = pygame.Rect(1075, 650, 175, 50)
                    if next_rect.collidepoint(pos):
                        if self.correct_answer:
                            self.update_score()
                            self.new_question()
                        else:
                            self.new_question()
        # next question
        if event.type == pygame.K_SPACE and self.answered:
            self.new_question()
        # mouse hover event
        if event.type == pygame.MOUSEMOTION:
            self.mouseover()

    # score
    def update_score(self):
        '''
        Update player's score
        :return:
        '''
        self.score += 10

    def mouseover(self):
        '''
        Handle mouse hover events
        :return:
        '''
        # button parameters
        button_width = 220
        button_height = 250
        horizontal_space = 25
        vertical_space = 25

        # check if mouse is hovering over button
        pos = pygame.mouse.get_pos()
        for i, item in enumerate(self.choices):
            column = i % 2
            row = i // 2
            x = 695 + column * (button_width + horizontal_space)
            y = 100 + row * (button_height + vertical_space)
            option_rectangle = pygame.Rect(x, y, button_width, button_height)
            if option_rectangle.collidepoint(pos):
                self.hovered = item
                return
        self.hovered = None

    def message(self):
        '''
        Display if answer is correct or incorrect.
        :return:
        '''
        font1 = pygame.font.SysFont("secularoneregular", 20)
        font2 = pygame.font.SysFont("secularoneregular", 35)
        display = False
        text1 = None
        text2 = None
        message = "The colour is " + self.choice_key
        # correct answer message
        if self.correct_answer:
            text1 = font2.render(
                " CORRECT ANSWER ", True, "#7dba6a")
            text2 = font1.render(
                message, True, "#8d9dc7")
            display = True
        # incorrect answer message
        elif self.incorrect_answer:
            text1 = font2.render(
                " INCORRECT ANSWER ", True, "#ba3232")
            text2 = font1.render(
                message, True, "#8d9dc7")
            display = True
        rect = pygame.Rect(450, 280, 400, 250)

        if display:
            pygame.draw.rect(
                self.screen, "beige", rect, 0, 20)
            pygame.draw.rect(
                self.screen, "#c1d7d9", rect, 8, 20)

            self.screen.blit(text1, (480, 320))
            self.screen.blit(text2, text2.get_rect(
                center=rect.center))
            self.screen.blit(self.next_button, (1075, 650))  # next button
            # correct answer sound
            if not self.play_sound and self.correct_answer:
                self.correct_sound.play(loops=0)
                self.play_sound = True
            # incorrect answer sound
            elif not self.play_sound and self.incorrect_answer:
                self.incorrect_sound.play(loops=0)
                self.play_sound = True
