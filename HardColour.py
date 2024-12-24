import pydoc
import pygame
import random
from saveGame import saveGame


class HardColour:
    '''
            Author: Ethne Au, Lily So
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
        self.font = pygame.font.SysFont("arial", 40)
        self.width = 1280
        self.height = 720
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.game_state = game_state

        # load keyboard buttons
        self.key_a = pygame.image.load(
            "assets/keyboardKeys/a.png").convert_alpha()
        self.key_b = pygame.image.load(
            "assets/keyboardKeys/b.png").convert_alpha()
        self.key_c = pygame.image.load(
            "assets/keyboardKeys/c.png").convert_alpha()
        self.key_d = pygame.image.load(
            "assets/keyboardKeys/d.png").convert_alpha()
        self.key_e = pygame.image.load(
            "assets/keyboardKeys/e.png").convert_alpha()
        self.key_f = pygame.image.load(
            "assets/keyboardKeys/f.png").convert_alpha()
        self.key_g = pygame.image.load(
            "assets/keyboardKeys/g.png").convert_alpha()
        self.key_h = pygame.image.load(
            "assets/keyboardKeys/h.png").convert_alpha()
        self.key_i = pygame.image.load(
            "assets/keyboardKeys/i.png").convert_alpha()
        self.key_j = pygame.image.load(
            "assets/keyboardKeys/j.png").convert_alpha()
        self.key_k = pygame.image.load(
            "assets/keyboardKeys/k.png").convert_alpha()
        self.key_l = pygame.image.load(
            "assets/keyboardKeys/l.png").convert_alpha()
        self.key_m = pygame.image.load(
            "assets/keyboardKeys/m.png").convert_alpha()
        self.key_n = pygame.image.load(
            "assets/keyboardKeys/n.png").convert_alpha()
        self.key_o = pygame.image.load(
            "assets/keyboardKeys/o.png").convert_alpha()
        self.key_p = pygame.image.load(
            "assets/keyboardKeys/p.png").convert_alpha()
        self.key_q = pygame.image.load(
            "assets/keyboardKeys/q.png").convert_alpha()
        self.key_r = pygame.image.load(
            "assets/keyboardKeys/r.png").convert_alpha()
        self.key_s = pygame.image.load(
            "assets/keyboardKeys/s.png").convert_alpha()
        self.key_t = pygame.image.load(
            "assets/keyboardKeys/t.png").convert_alpha()
        self.key_u = pygame.image.load(
            "assets/keyboardKeys/u.png").convert_alpha()
        self.key_v = pygame.image.load(
            "assets/keyboardKeys/v.png").convert_alpha()
        self.key_w = pygame.image.load(
            "assets/keyboardKeys/w.png").convert_alpha()
        self.key_x = pygame.image.load(
            "assets/keyboardKeys/x.png").convert_alpha()
        self.key_y = pygame.image.load(
            "assets/keyboardKeys/y.png").convert_alpha()
        self.key_z = pygame.image.load(
            "assets/keyboardKeys/z.png").convert_alpha()

        self.key_back = pygame.image.load(
            "assets/keyboardKeys/backspace.png").convert_alpha()

        self.next_button = pygame.image.load(
            "assets/colourEasyImgs/next_button.png").convert_alpha()  # next button to the next question
        self.hint_button = pygame.image.load(
            "assets/colourEasyImgs/hint_button_colour.png").convert_alpha()
        self.submit_button = pygame.image.load(
            "assets/colourEasyImgs/submit_button.png").convert_alpha()  # load submit button

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
            "Red": "#db5448",
            "Orange": "#ff8c3f",
            "Yellow": "#f5e14e",
            "Green": "#65b567",
            "Blue": "#55ade0",
            "Purple": "mediumpurple",
            "Pink": "lightpink2",
            "Black": "gray15",
            "White": "#ffffff",
            "Brown": "#70513d",
            "Gray": "gray50"
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
        # randomize next question and remove it from the list
        self.question = random.choice(self.combinations)
        self.combinations.remove(self.question)

        self.user_text = ''
        self.active = False
        self.colour_textbox_click = pygame.Color("lightblue")
        self.colour_textbox_passive = pygame.Color(203, 236, 164)
        self.colour = self.colour_textbox_passive
        self.input_rect = pygame.Rect(735, 227, 450, 80)

        self.questions_answered = 0  # tracking number of questions answered
        self.correct_answer = False

        self.submit_clicked = False
        self.answered = False
        self.select_hint = False
        self.score = 0
        self.saved = False

    def run(self):
        ''' 
            Creates UI for the game
            :return:
        '''
        pygame.display.set_caption('Rainbow Rumble')
        font1 = pygame.font.SysFont("arialblack", 45)
        title = font1.render("What Colour does this make?", True, "black")
        self.screen.blit(title, (140, 15))

        # display back button
        self.screen.blit(self.back_button, (40, 15))

        # display score
        font1 = pygame.font.SysFont("arialblack", 40)
        score_text = font1.render("Score: " + str(self.score), True, "black")
        self.screen.blit(score_text, (1010, 15))

        # display colour
        colour_border = (203, 236, 164)
        pygame.draw.rect(self.screen, colour_border, (140, 100, 450, 550))
        pygame.draw.rect(
            self.screen, self.colours[self.question[0]], (160, 115, 410, 220), 120, 30)
        pygame.draw.rect(
            self.screen, self.colours[self.question[1]], (160, 415, 410, 220), 120, 30)

        # addition symbol
        font2 = pygame.font.SysFont("arialblack", 100)
        add_sign = font2.render("+", True, "black")
        self.screen.blit(add_sign, (330, 300))

        font2 = pygame.font.SysFont("arialblack", 22)
        title = font2.render(
            "Click the box to type your answer.", True, "black")
        self.screen.blit(title, (750, 170))

        # display hint button
        self.screen.blit(self.hint_button, (900, 15))

        # display submit button
        self.screen.blit(self.submit_button, (735, 325))

        # display user input box
        pygame.draw.rect(self.screen, self.colour, self.input_rect)
        font1 = pygame.font.SysFont("arialblack", 40)
        text = font1.render(self.user_text, True, "black")
        self.screen.blit(text, (self.input_rect.x +
                         10, self.input_rect.y + 10))

        # only allow letters within the box
        text_width = text.get_width()
        if text_width > self.input_rect.width - 5:
            self.user_text = self.user_text[:-1]

        # display keys for keyboard - first row
        self.screen.blit(self.key_q, (735, 400))
        self.screen.blit(self.key_w, (780, 400))
        self.screen.blit(self.key_e, (825, 400))
        self.screen.blit(self.key_r, (870, 400))
        self.screen.blit(self.key_t, (915, 400))
        self.screen.blit(self.key_y, (960, 400))
        self.screen.blit(self.key_u, (1005, 400))
        self.screen.blit(self.key_i, (1050, 400))
        self.screen.blit(self.key_o, (1095, 400))
        self.screen.blit(self.key_p, (1140, 400))

        # second row
        self.screen.blit(self.key_a, (758, 445))
        self.screen.blit(self.key_s, (803, 445))
        self.screen.blit(self.key_d, (848, 445))
        self.screen.blit(self.key_f, (893, 445))
        self.screen.blit(self.key_g, (938, 445))
        self.screen.blit(self.key_h, (983, 445))
        self.screen.blit(self.key_j, (1028, 445))
        self.screen.blit(self.key_k, (1073, 445))
        self.screen.blit(self.key_l, (1118, 445))

        # third row
        self.screen.blit(self.key_z, (781, 490))
        self.screen.blit(self.key_x, (826, 490))
        self.screen.blit(self.key_c, (871, 490))
        self.screen.blit(self.key_v, (916, 490))
        self.screen.blit(self.key_b, (961, 490))
        self.screen.blit(self.key_n, (1006, 490))
        self.screen.blit(self.key_m, (1051, 490))

        # backspace
        self.screen.blit(self.key_back, (1096, 490))

        # level complete if 10 questions are answered
        if self.questions_answered == 10:
            self.screen.blit(self.congrats, (315, 160))
            # show buttons
            self.screen.blit(self.levels_button, (368, 450))
            self.screen.blit(self.save_game_button, (561, 450))
            self.active = False
            self.answered = True

        # when user submits an answer, check answer
        if self.answered and self.questions_answered != 10:
            self.check_answer(self.user_text)
            if self.correct_answer:
                self.correct()
                self.screen.blit(self.next_button, (1075, 650))
            else:
                self.incorrect()
                self.screen.blit(self.next_button, (1075, 650))
        if self.select_hint:
            self.hint()

        pygame.display.update()  # update display
        self.clock.tick(60)

    def user_input(self, event, save):
        '''
            Handle user input including button pressing and drag and drop
            :param event:
            :param save:
            :return:
        '''
        self.screen.fill("beige")
        # quit game on escape
        pos = pygame.mouse.get_pos()  # mouse position

        if event.type == pygame.MOUSEBUTTONDOWN:
            # back button
            back_button = pygame.Rect(40, 15, 70, 70)
            if back_button.collidepoint(pos):
                self.__init__(self.screen, self.game_state)
                self.game_state.set_state('colourLevels')
            if not self.answered:
                if self.input_rect.collidepoint(event.pos):
                    self.active = True
                # screen keyboard
                if self.active:
                    q_rect = pygame.Rect((735, 400, 40, 40))
                    if q_rect.collidepoint(pos):
                        self.user_text += 'q'
                    w_rect = pygame.Rect((780, 400, 40, 40))
                    if w_rect.collidepoint(pos):
                        self.user_text += 'w'
                    e_rect = pygame.Rect((825, 400, 40, 40))
                    if e_rect.collidepoint(pos):
                        self.user_text += 'e'
                    r_rect = pygame.Rect((870, 400, 40, 40))
                    if r_rect.collidepoint(pos):
                        self.user_text += 'r'
                    t_rect = pygame.Rect((915, 400, 40, 40))
                    if t_rect.collidepoint(pos):
                        self.user_text += 't'
                    y_rect = pygame.Rect((960, 400, 40, 40))
                    if y_rect.collidepoint(pos):
                        self.user_text += 'y'
                    u_rect = pygame.Rect((1005, 400, 40, 40))
                    if u_rect.collidepoint(pos):
                        self.user_text += 'u'
                    i_rect = pygame.Rect((1050, 400, 40, 40))
                    if i_rect.collidepoint(pos):
                        self.user_text += 'i'
                    o_rect = pygame.Rect((1085, 400, 40, 40))
                    if o_rect.collidepoint(pos):
                        self.user_text += 'o'
                    p_rect = pygame.Rect((1140, 400, 40, 40))
                    if p_rect.collidepoint(pos):
                        self.user_text += 'p'
                    a_rect = pygame.Rect((758, 445, 40, 40))
                    if a_rect.collidepoint(pos):
                        self.user_text += 'a'
                    s_rect = pygame.Rect((803, 445, 40, 40))
                    if s_rect.collidepoint(pos):
                        self.user_text += 's'
                    d_rect = pygame.Rect((848, 445, 40, 40))
                    if d_rect.collidepoint(pos):
                        self.user_text += 'd'
                    f_rect = pygame.Rect((893, 445, 40, 40))
                    if f_rect.collidepoint(pos):
                        self.user_text += 'f'
                    g_rect = pygame.Rect((938, 445, 40, 40))
                    if g_rect.collidepoint(pos):
                        self.user_text += 'g'
                    h_rect = pygame.Rect((983, 445, 40, 40))
                    if h_rect.collidepoint(pos):
                        self.user_text += 'h'
                    j_rect = pygame.Rect((1028, 445, 40, 40))
                    if j_rect.collidepoint(pos):
                        self.user_text += 'j'
                    k_rect = pygame.Rect((1073, 445, 40, 40))
                    if k_rect.collidepoint(pos):
                        self.user_text += 'k'
                    l_rect = pygame.Rect((1118, 445, 40, 40))
                    if l_rect.collidepoint(pos):
                        self.user_text += 'l'
                    z_rect = pygame.Rect((781, 490, 40, 40))
                    if z_rect.collidepoint(pos):
                        self.user_text += 'z'
                    x_rect = pygame.Rect((826, 490, 40, 40))
                    if x_rect.collidepoint(pos):
                        self.user_text += 'x'
                    c_rect = pygame.Rect((871, 490, 40, 40))
                    if c_rect.collidepoint(pos):
                        self.user_text += 'c'
                    v_rect = pygame.Rect((916, 490, 40, 40))
                    if v_rect.collidepoint(pos):
                        self.user_text += 'v'
                    b_rect = pygame.Rect((961, 490, 40, 40))
                    if b_rect.collidepoint(pos):
                        self.user_text += 'b'
                    n_rect = pygame.Rect((1006, 490, 40, 40))
                    if n_rect.collidepoint(pos):
                        self.user_text += 'n'
                    m_rect = pygame.Rect((1051, 490, 40, 40))
                    if m_rect.collidepoint(pos):
                        self.user_text += 'm'
                    back_rect = pygame.Rect((1094, 490, 80, 40))
                    if back_rect.collidepoint(pos):
                        self.user_text = self.user_text[:-1]
                else:
                    self.active = False
                # submit button
                submit_rect = pygame.Rect(735, 325, 450, 50)
                if submit_rect.collidepoint(pos):
                    self.submit_clicked = True

                if self.submit_clicked and self.questions_answered != 10:
                    self.check_answer(self.user_text)
                    self.answered = True
                    if self.correct_answer:
                        self.correct_sound.play(loops=0)
                        self.submit_clicked = False
                    else:
                        self.incorrect_sound.play(loops=0)
                        self.submit_clicked = False
                # hint button
                hint_rect = pygame.Rect(900, 15, 175, 50)
                if hint_rect.collidepoint(pos):
                    self.select_hint = True
                else:
                    self.select_hint = False

            if self.answered and self.questions_answered != 10:
                next_rect = pygame.Rect(1075, 650, 175, 50)
                if next_rect.collidepoint(pos):
                    if self.correct_answer:
                        self.update_score()
                        self.next_question()
                    else:
                        self.next_question()
            # game finished
            if self.questions_answered == 10:
                self.active = False
                levels_rect = pygame.Rect(368, 450, 159, 65)
                saveGame_rect = pygame.Rect(561, 450, 159, 65)
                if saveGame_rect.collidepoint(pos):
                    self.saved = True
                    saveGame(save, 1, 3)
                if levels_rect.collidepoint(pos):
                    if self.saved == False:
                        self.__init__(self.screen, self.game_state)
                    self.game_state.set_state('colourLevels')

        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            else:
                key_name = pygame.key.name(event.key)
                if len(key_name) == 1:
                    self.user_text += key_name

        if self.active:
            self.colour = self.colour_textbox_click
        else:
            self.colour = self.colour_textbox_passive

    # score
    def update_score(self):
        '''
            Update player's score
            :return:
        '''
        self.score += 30

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

    # check answer
    def check_answer(self, user_input):
        '''
            Check typed answer is correct or incorrect
            :param user_input: User-typed answer
            :return: True if correct, false otherwise
        '''
        correct_ans = self.question[2]

        if user_input.lower() == correct_ans.lower():
            self.correct_answer = True
        else:
            self.correct_answer = False

    def display_answer(self, message, colour):
        '''
            Display answer on screen
            :param message:
            :param colour: Colour of text
        '''
        text = self.font.render(message, True, colour)
        text_rect = text.get_rect(center=(1280 // 2, 675))
        self.screen.blit(text, text_rect)

    def next_question(self):
        '''
            Generate a new question.
            :return:
        '''
        # randomize question and options
        self.question = random.choice(self.combinations)
        self.combinations.remove(self.question)

        self.correct_answer = False
        self.answered = False
        self.correct_answer = False  # reset correct answer
        self.user_text = ''  # reset user text
        self.submit_clicked = False
        self.answered = False
        self.questions_answered += 1
        self.active = False

    def correct(self):
        '''
            Display if answer is correct to screen.
            :return:
        '''
        font1 = pygame.font.SysFont("secularoneregular", 35)
        font2 = pygame.font.SysFont("secularoneregular", 20)
        if self.correct_answer:
            message = self.question[0] + " and " + self.question[1] + \
                " makes " + self.question[2]
            correct1 = font1.render(
                " CORRECT ANSWER ", True, "#7dba6a")
            correct2 = font2.render(
                message, True, "#8d9dc7")
            correct_rect = pygame.Rect(450, 280, 400, 250)

            pygame.draw.rect(
                self.screen, "beige", correct_rect, 0, 20)
            pygame.draw.rect(
                self.screen, "#c1d7d9", correct_rect, 8, 20)

            self.screen.blit(correct1, (500, 320))
            self.screen.blit(correct2, correct2.get_rect(
                center=correct_rect.center))

    def incorrect(self):
        '''
            Display if answer is incorrect to screen.
            :return:
        '''
        if not self.correct_answer:
            font1 = pygame.font.SysFont("secularoneregular", 35)
            font2 = pygame.font.SysFont("secularoneregular", 20)
            message = self.question[0] + " and " + self.question[1] + \
                " makes " + self.question[2]
            incorrect1 = font1.render(
                " INCORRECT ANSWER ", True, "#ba3232")
            incorrect2 = font2.render(
                message, True, "#8d9dc7")
            incorrect_rect = pygame.Rect(450, 280, 400, 250)

            pygame.draw.rect(
                self.screen, "beige", incorrect_rect, 0, 20)
            pygame.draw.rect(
                self.screen, "#c1d7d9", incorrect_rect, 8, 20)

            self.screen.blit(incorrect1, (475, 320))
            self.screen.blit(incorrect2, incorrect2.get_rect(
                center=incorrect_rect.center))
