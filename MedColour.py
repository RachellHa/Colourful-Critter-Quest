import pydoc
import pygame
import random
from saveGame import saveGame


class MedColour:
    '''
        Author: Ethne Au
        Purpose: Class for medium level of the Rainbow Rumble game, runs 10 questions
    '''

    def __init__(self, screen, game_state):
        '''
        Initialize MedColour class.
        Loads images and sounds from files. 
        Create colour dictionary containing possible options/questions.
        Randomize question.

        :param screen: The game screen surface:
        :param game_state: The game state manager:
        '''
        # default font
        self.font = pygame.font.SysFont("secularoneregular", 40)

        # window dimensions
        self.width = 1280
        self.height = 720
        # initialize window
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.game_state = game_state

        self.answer_box = pygame.Rect(930, 160, 200, 200)  # box to put answer
        self.next_button = pygame.image.load(
            "assets/colourEasyImgs/next_button.png").convert_alpha()  # next button to the next question
        self.hint_button = pygame.image.load(
            "assets/colourEasyImgs/hint_button_colour.png").convert_alpha()

        self.orange = pygame.image.load(
            "assets/colourEasyImgs/orange.png").convert_alpha()

        self.green = pygame.image.load(
            "assets/colourEasyImgs/green.png").convert_alpha()

        self.purple = pygame.image.load(
            "assets/colourEasyImgs/purple.png").convert_alpha()

        self.pink = pygame.image.load(
            "assets/colourEasyImgs/pink.png").convert_alpha()

        self.gray = pygame.image.load(
            "assets/colourEasyImgs/gray.png").convert_alpha()

        self.brown = pygame.image.load(
            "assets/colourEasyImgs/brown.png").convert_alpha()

        # load correct sound
        self.correct_sound = pygame.mixer.Sound(
            "assets/colourSounds/correctSound.mp3")

        # load incorrect sound
        self.incorrect_sound = pygame.mixer.Sound(
            "assets/colourSounds/incorrectSound.mp3")

        # load backbutton
        self.back_button = pygame.image.load(
            "assets/colourEasyImgs/backButton.png").convert_alpha()

        # import congrats images/buttons
        self.congrats = pygame.image.load(
            "assets/colourEasyImgs/congrats.png").convert_alpha()

        # load extra buttons on congrats image
        self.levels_button = pygame.image.load(
            "assets/animalQuestionAssets/levels.png").convert_alpha()
        self.next_level_button = pygame.image.load(
            "assets/animalQuestionAssets/nextLevel.png").convert_alpha()
        self.save_game_button = pygame.image.load(
            "assets/animalQuestionAssets/saveGame.png").convert_alpha()

        # dictionary containing colours and their hex codes
        self.colours = {
            "Red": {
                "base": "#db5448",
                "border": "red4",
                "text": "#730b02"},
            "Orange": {
                "base": "#ff8c3f",
                "border": "#d45500",
                "text": "#b54900"},
            "Yellow": {
                "base": "#f5e14e",
                "border": "#e3b842",
                "text": "goldenrod4"},
            "Green": {
                "base": "#65b567",
                "border": "#4e9655",
                "text": "#245e2e"},
            "Blue": {
                "base": "#55ade0",
                "border": "#295bab",
                "text": "#113163"},
            "Purple": {
                "base": "mediumpurple",
                "border": "mediumpurple4",
                "text": "#412c66"},
            "Pink": {
                "base": "lightpink2",
                "border": "#c76b87",
                "text": "#a65069"},
            "Black": {
                "base": "gray15",
                "border": "gray2",
                "text": "#b5b5b5"},
            "White": {
                "base": "#ffffff",
                "border": "gray",
                "text": "#808080"},
            "Brown": {
                "base": "#70513d",
                "border": "#543a29",
                "text": "#291c14"},
            "Gray": {
                "base": "gray50",
                "border": "gray20",
                "text": "black"}
        }

        # list containing colour combinations
        self.combinations = [
            ["Red", "Yellow", "Orange"],
            ["Yellow", "Blue", "Green"],
            ["Blue", "Red", "Purple"],
            ["Red", "White", "Pink"],
            ["Black", "White", "Gray"],
            ["Red", "Green", "Brown"],
            ["Yellow", "Red", "Orange"],
            ["Blue", "Yellow", "Green"],
            ["Red", "Blue", "Purple"],
            ["White", "Red", "Pink"],
            ["White", "Black", "Gray"],
            ["Green", "Red", "Brown"]
        ]

        # list containing xy coordinates of the options
        self.optionsXY = [
            [170, 500],
            [430, 500],
            [690, 500],
            [940, 500]
        ]

        # list of the original positions of the options
        self.originalX = [170, 430, 690, 940]

        # randomize next question and remove it from the list
        self.question = random.choice(self.combinations)
        self.combinations.remove(self.question)

        # randomize options
        self.options = self.randomize_choices()
        self.dragging = False
        self.correct_answer = False
        self.incorrect_answer = False
        self.select_hint = False
        self.play_sound = False
        self.newgame = True
        self.selected_box = None
        self.j = 0
        self.questions_answered = 0
        self.choices = []
        self.score = 0
        self.saved = False

    def user_input(self, event, save):
        '''
        Handle user input including button pressing and drag and drop
        :param event:
        :param save:
        :return:
        '''
        self.screen.fill("beige")
        pos = pygame.mouse.get_pos()  # mouse position
        # if the user selected a colour option
        if event.type == pygame.MOUSEBUTTONDOWN and not (self.correct_answer or self.incorrect_answer):
            # check which option they chose
            self.j = 0
            for i in range(len(self.choices)):
                if self.choices[i].collidepoint(pos):
                    self.dragging = True
                    self.selected_box = self.choices[i]
                    self.j = i
                    break
        # if user is dragging the option
        if event.type == pygame.MOUSEMOTION and self.dragging:
            if self.selected_box:
                # move option with mouse
                self.optionsXY[self.j][0] += event.rel[0]
                self.optionsXY[self.j][1] += event.rel[1]

        # if user dropped of the option
        if event.type == pygame.MOUSEBUTTONUP and not (self.correct_answer or self.incorrect_answer):
            self.dragging = False
            # change option coordinates to the answer box
            if self.answer_box.colliderect(self.choices[self.j]):
                for i in range(len(self.optionsXY)):
                    if self.optionsXY[i][0] > 900 and self.optionsXY[i][1] < 300:
                        self.optionsXY[i][0] = self.originalX[i]
                        self.optionsXY[i][1] = 500
                self.optionsXY[self.j][0] = 955
                self.optionsXY[self.j][1] = 190
                if self.j == answer:
                    self.correct_answer = True
                    self.play_sound = False
                else:
                    self.incorrect_answer = True
                    self.play_sound = False
            else:  # change option coordinates to original position
                self.optionsXY[self.j][0] = self.originalX[self.j]
                self.optionsXY[self.j][1] = 500
                self.correct_answer = False
                self.incorrect_answer = False

        # if user pressed the next button to the next question
        if event.type == pygame.MOUSEBUTTONDOWN and (self.correct_answer or self.incorrect_answer):
            next_rect = pygame.Rect(640, 450, 175, 50)
            if next_rect.collidepoint(pos):
                if self.correct_answer:
                    self.update_score()
                    self.next_question()
                else:
                    self.next_question()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # hint button
            hint_rect = pygame.Rect(900, 15, 175, 50)
            if hint_rect.collidepoint(pos):
                self.select_hint = True
            else:
                self.select_hint = False

            # back button
            back_button = pygame.Rect(40, 15, 70, 70)
            if back_button.collidepoint(pos):
                self.__init__(self.screen, self.game_state)
                self.game_state.set_state('colourLevels')
            # 10 questions finished
            if self.questions_answered == 10:
                self.active = False
                levels_rect = pygame.Rect(368, 450, 159, 65)
                saveGame_rect = pygame.Rect(561, 450, 159, 65)
                nextLevel_rect = pygame.Rect(753, 450, 159, 65)
                if saveGame_rect.collidepoint(pos):
                    self.saved = True
                    saveGame(save, 1, 2)
                if levels_rect.collidepoint(pos):
                    if self.saved == False:
                        self.__init__(self.screen, self.game_state)
                    self.game_state.set_state('colourLevels')
                if nextLevel_rect.collidepoint(pos):
                    if self.saved == False:
                        self.__init__(self.screen, self.game_state)
                    self.game_state.set_state('colourHard')

    def update_score(self):
        '''
        Update player's score
        :return:
        '''
        self.score += 20

    def run(self):
        ''' 
        Creates UI for the game
        :return:
        '''
        pygame.display.set_caption('Rainbow Rumble')
        # title
        font1 = pygame.font.SysFont("arialblack", 45)
        title = font1.render("What Colour does this make?", True, "#313538")
        self.screen.blit(title, (140, 15))

        # display back button
        self.screen.blit(self.back_button, (40, 15))

        # display score
        font1 = pygame.font.SysFont("arialblack", 40)
        score_text = font1.render("Score: " + str(self.score), True, "black")
        self.screen.blit(score_text, (1010, 15))

        # box background
        colour_border = "#a0d184"
        pygame.draw.rect(self.screen, (203, 236, 164),
                         (70, 110, self.width-140, 300), 0, 30)
        pygame.draw.rect(self.screen, colour_border,
                         (70, 110, self.width-140, 300), 8, 30)

        # equation colours
        equation_rect1 = pygame.Rect((130, 170, 180, 180))
        equation_rect2 = pygame.Rect((530, 170, 180, 180))
        # borders for the colours
        pygame.draw.rect(
            self.screen, self.colours[self.question[0]]["border"], equation_rect1.inflate(10, 10), 0, 75)
        pygame.draw.rect(
            self.screen, self.colours[self.question[1]]["border"], equation_rect2.inflate(10, 10), 0, 75)
        # base for the colours
        pygame.draw.rect(
            self.screen, self.colours[self.question[0]]["base"], equation_rect1, 0, 70)
        pygame.draw.rect(
            self.screen, self.colours[self.question[1]]["base"], equation_rect2, 0, 70)
        # text on the colours
        equation_text1 = self.font.render(
            self.question[0], True, self.colours[self.question[0]]["text"])
        self.screen.blit(equation_text1, equation_text1.get_rect(
            center=equation_rect1.center))
        equation_text2 = self.font.render(
            self.question[1], True, self.colours[self.question[1]]["text"])
        self.screen.blit(equation_text2, equation_text2.get_rect(
            center=equation_rect2.center))

        # addition symbol
        font2 = pygame.font.SysFont("arialblack", 100)
        add_sign = font2.render("+", True, "#313538")
        self.screen.blit(add_sign, (390, 170))

        # equal sign
        equal_sign = font2.render("=", True, "#313538")
        self.screen.blit(equal_sign, (780, 170))

        # drop colour area
        font3 = pygame.font.SysFont("arialblack", 150)
        drop_line = font3.render("___", True, "#313538")
        self.screen.blit(drop_line, (920, 180))

        # border around choices
        colour_border = (203, 236, 164)
        pygame.draw.rect(self.screen, colour_border,
                         (70, 450, self.width-140, 230), 8, 30)
        text_rect = pygame.Rect((100, 435, 400, 50))
        pygame.draw.rect(self.screen, "#dbebeb", text_rect, 0, 10)
        pygame.draw.rect(self.screen, "#c1d7d9", text_rect, 6, 10)
        font4 = pygame.font.SysFont("secularoneregular", 32)
        text1 = font4.render("Drag and Drop a Colour", True, "#7dba6a")
        self.screen.blit(text1, (128, 450))

        # choices to choose from
        self.choices = []

        self.choices.append(pygame.Rect(
            (self.optionsXY[0][0], self.optionsXY[0][1], 150, 150)))
        pygame.draw.rect(
            self.screen, self.colours[self.options[0]]["border"], self.choices[0].inflate(10, 10), 0, 57)
        pygame.draw.rect(
            self.screen, self.colours[self.options[0]]["base"], self.choices[0], 0, 55)
        choice_text1 = self.font.render(
            self.options[0], True, self.colours[self.options[0]]["text"])
        self.screen.blit(choice_text1, choice_text1.get_rect(
            center=self.choices[0].center))

        self.choices.append(pygame.Rect(
            (self.optionsXY[1][0], self.optionsXY[1][1], 150, 150)))
        pygame.draw.rect(
            self.screen, self.colours[self.options[1]]["border"], self.choices[1].inflate(10, 10), 0, 57)
        pygame.draw.rect(
            self.screen, self.colours[self.options[1]]["base"], self.choices[1], 0, 55)
        choice_text2 = self.font.render(
            self.options[1], True, self.colours[self.options[1]]["text"])
        self.screen.blit(choice_text2, choice_text2.get_rect(
            center=self.choices[1].center))

        self.choices.append(pygame.Rect(
            (self.optionsXY[2][0], self.optionsXY[2][1], 150, 150)))
        pygame.draw.rect(
            self.screen, self.colours[self.options[2]]["border"], self.choices[2].inflate(10, 10), 0, 57)
        pygame.draw.rect(
            self.screen, self.colours[self.options[2]]["base"], self.choices[2], 0, 55)
        choice_text3 = self.font.render(
            self.options[2], True, self.colours[self.options[2]]["text"])
        self.screen.blit(choice_text3, choice_text3.get_rect(
            center=self.choices[2].center))

        self.choices.append(pygame.Rect(
            (self.optionsXY[3][0], self.optionsXY[3][1], 150, 150)))
        pygame.draw.rect(
            self.screen, self.colours[self.options[3]]["border"], self.choices[3].inflate(10, 10), 0, 57)
        pygame.draw.rect(
            self.screen, self.colours[self.options[3]]["base"], self.choices[3], 0, 55)
        choice_text4 = self.font.render(
            self.options[3], True, self.colours[self.options[3]]["text"])
        self.screen.blit(choice_text4, choice_text4.get_rect(
            center=self.choices[3].center))

        self.screen.blit(self.hint_button, (900, 15))
        self.message()
        if self.select_hint:
            self.hint()

        # game finished
        if self.questions_answered == 10:
            self.screen.blit(self.congrats, (315, 160))
            # show buttons
            self.screen.blit(self.levels_button, (368, 450))
            self.screen.blit(self.save_game_button, (561, 450))
            self.screen.blit(self.next_level_button, (753, 450))

        pygame.display.update()  # update display
        self.clock.tick(60)

    def randomize_choices(self):
        '''
        Randomize list of options for the user to choose from
        :return options:
        '''
        # choose 3 options out of all the colours
        # Takes 3 color keys out of self.colours, red, yellow, green etc.
        options = random.sample(list(self.colours.keys()), 3)
        # redraw if answer is in the sample (duplicate)
        while self.question[2] in options:
            # random.sample(list(self.colours.keys()), 3)
            options = random.sample(list(self.colours.keys()), 3)
        # add answer to guarantee
        options.append(self.question[2])

        # shuffle order
        random.shuffle(options)

        # keep answer
        global answer
        answer = options.index(self.question[2])

        return options

    def message(self):
        '''
        Display if answer is correct or incorrect to screen.
        :return:
        '''
        font1 = pygame.font.SysFont("secularoneregular", 20)
        font2 = pygame.font.SysFont("secularoneregular", 35)
        display = False
        text1 = None
        text2 = None
        # correct answer message
        if self.correct_answer:
            message = self.question[0] + " and " + self.question[1] + \
                " makes " + self.question[2]
            text1 = self.font.render(
                " CORRECT ANSWER ", True, "#7dba6a")
            text2 = font1.render(
                message, True, "#8d9dc7")
            display = True
        # incorrect answer message
        elif self.incorrect_answer:
            message = message = self.question[0] + " and " + self.question[1] + \
                " makes " + self.question[2]
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

            self.screen.blit(text1, (470, 320))
            self.screen.blit(text2, text2.get_rect(
                center=rect.center))
            self.screen.blit(self.next_button, (640, 450))  # next button
            # correct answer sound
            if not self.play_sound and self.correct_answer:
                self.correct_sound.play(loops=0)
                self.play_sound = True
            # incorrect answer sound
            elif not self.play_sound and self.incorrect_answer:
                self.incorrect_sound.play(loops=0)
                self.play_sound = True

    def hint(self):
        '''
        Display hint image to the user
        :return:
        '''
        hint_rect = pygame.Rect(450, 280, 400, 200)

        pygame.draw.rect(
            self.screen, "beige", hint_rect, 0, 20)
        pygame.draw.rect(
            self.screen, "#c1d7d9", hint_rect, 8, 20)
        if self.question[2] == "Orange":
            colour = self.orange
        elif self.question[2] == "Green":
            colour = self.green
        elif self.question[2] == "Purple":
            colour = self.purple
        elif self.question[2] == "Pink":
            colour = self.pink
        elif self.question[2] == "Gray":
            colour = self.gray
        else:
            colour = self.brown
        self.screen.blit(colour, colour.get_rect(center=hint_rect.center))

    def next_question(self):
        '''
        Generate a new question.
        :return:
        '''
        # change back to original coordinates
        for i in range(4):
            self.optionsXY[i][0] = self.originalX[i]
            self.optionsXY[i][1] = 500

        self.questions_answered += 1

        # randomize question and options
        self.question = random.choice(self.combinations)
        self.combinations.remove(self.question)
        self.options = self.randomize_choices()

        self.correct_answer = False
        self.incorrect_answer = False
