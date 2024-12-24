import pygame
import random
import pydoc
from saveGame import saveGame

class AnimalHard:
    """
    Author: Lily So
    This class was created to display the hard level of the animal typing safari game.
    """
    def __init__(self, screen, animals, game_state):
        """
        This method initializes the AnimalHard class.
        :param screen: the screen to display the game
        :param animals: the dictionary of animals and their data
        :param game_state: the current state of the game
        """
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.game_state = game_state
        self.animals = animals
        screen = pygame.display.set_mode((1280, 720))
        self.font = pygame.font.SysFont("arial", 40)

        #load keyboard buttons
        self.key_a = pygame.image.load("assets/keyboardKeys/a.png").convert_alpha()
        self.key_b = pygame.image.load("assets/keyboardKeys/b.png").convert_alpha()
        self.key_c = pygame.image.load("assets/keyboardKeys/c.png").convert_alpha()
        self.key_d = pygame.image.load("assets/keyboardKeys/d.png").convert_alpha()
        self.key_e = pygame.image.load("assets/keyboardKeys/e.png").convert_alpha()
        self.key_f = pygame.image.load("assets/keyboardKeys/f.png").convert_alpha()
        self.key_g = pygame.image.load("assets/keyboardKeys/g.png").convert_alpha()
        self.key_h = pygame.image.load("assets/keyboardKeys/h.png").convert_alpha()
        self.key_i = pygame.image.load("assets/keyboardKeys/i.png").convert_alpha()
        self.key_j = pygame.image.load("assets/keyboardKeys/j.png").convert_alpha()
        self.key_k = pygame.image.load("assets/keyboardKeys/k.png").convert_alpha()
        self.key_l = pygame.image.load("assets/keyboardKeys/l.png").convert_alpha()
        self.key_m = pygame.image.load("assets/keyboardKeys/m.png").convert_alpha()
        self.key_n = pygame.image.load("assets/keyboardKeys/n.png").convert_alpha()
        self.key_o = pygame.image.load("assets/keyboardKeys/o.png").convert_alpha()
        self.key_p = pygame.image.load("assets/keyboardKeys/p.png").convert_alpha()
        self.key_q = pygame.image.load("assets/keyboardKeys/q.png").convert_alpha()
        self.key_r = pygame.image.load("assets/keyboardKeys/r.png").convert_alpha()
        self.key_s = pygame.image.load("assets/keyboardKeys/s.png").convert_alpha()
        self.key_t = pygame.image.load("assets/keyboardKeys/t.png").convert_alpha()
        self.key_u = pygame.image.load("assets/keyboardKeys/u.png").convert_alpha()
        self.key_v = pygame.image.load("assets/keyboardKeys/v.png").convert_alpha()
        self.key_w = pygame.image.load("assets/keyboardKeys/w.png").convert_alpha()
        self.key_x = pygame.image.load("assets/keyboardKeys/x.png").convert_alpha()
        self.key_y = pygame.image.load("assets/keyboardKeys/y.png").convert_alpha()
        self.key_z = pygame.image.load("assets/keyboardKeys/z.png").convert_alpha()
        self.key_back = pygame.image.load("assets/keyboardKeys/backspace.png").convert_alpha()

        #load background buttons
        self.button_img = pygame.image.load("assets/animalQuestionAssets/mc_button.png").convert_alpha()
        self.button_hover_img = pygame.image.load("assets/animalQuestionAssets/mc_hover_button.png").convert_alpha()

        #load hint button
        self.hint_button = pygame.image.load("assets/animalQuestionAssets/hint_button.png").convert_alpha()

        #load next button
        self.next_button = pygame.image.load("assets/animalQuestionAssets/next_button.png").convert_alpha()

        #load submit button
        self.submit_button = pygame.image.load("assets/animalQuestionAssets/submit_button.png").convert_alpha()
        #load correct sound
        self.correct_sound = pygame.mixer.Sound("assets/animalQuestionAssets/correctSound.mp3")
        #load extra buttons on congrats image
        self.levels_button = pygame.image.load("assets/animalQuestionAssets/levels.png").convert_alpha()
        self.next_level_button = pygame.image.load("assets/animalQuestionAssets/nextLevel.png").convert_alpha()
        self.save_game_button = pygame.image.load("assets/animalQuestionAssets/saveGame.png").convert_alpha()
        #load incorrect sound
        self.incorrect_sound = pygame.mixer.Sound("assets/animalQuestionAssets/incorrectSound.mp3")

        #load congrats image
        self.congrats = pygame.image.load("assets/animalQuestionAssets/congrats.png").convert_alpha()
        #load back button
        self.back_button = pygame.image.load("assets/animalLevel/backButton.png").convert_alpha()

        self.correct_answer = False
        self.user_text = '' #track user text input
        self.active = False #track if user clicked the box
        self.colour_textbox_click = pygame.Color("lightblue")
        self.colour_textbox_passive = pygame.Color(203, 236, 164)
        self.colour = self.colour_textbox_passive
        self.input_rect = pygame.Rect(735, 227, 450, 80)
        self.selected_animal = None #track selected animal
        self.animal_index = 0 #index of selected animal
        self.animal_list = self.shuffle_options(animals)#list of animal options
        self.questions_answered = 0 #tracking number of questions answered
        self.correct_answer = False
        self.submit_clicked = False
        self.answered = False
        self.score = 0 #set score
        self.hardLevel_complete = False
        self.save_game = False #track if user clicked save_game

    def update_score(self):
        """
        This method updates the score of the user.
        """
        self.score += 30

    def shuffle_options(self, animals):
        """
        This method shuffles the list of animals.
        :param animals: the dictionary of animals and their data
        :return: the shuffled list of animals keys
        """
        animal_keys = list(animals.keys())
        random.shuffle(animal_keys)
        return animal_keys
    
    def run(self):
        """
        This method runs the hard level of the animal typing safari game.
        """
        self.screen.fill("beige")
        pygame.display.set_caption("Animal Typing Safari")
        #prompt user for question
        font = pygame.font.SysFont("arialblack", 45)
        img = font.render("What animal is this?", True, "black")
        self.screen.blit(img, (140, 15))
        
        #instructions for user 
        font1 = pygame.font.SysFont("arialblack", 20)
        img1 = font1.render("Click the box to type your answer.", True, "black")
        self.screen.blit(img1, (775, 175))

        #display selected animal image
        selected_animal = self.animal_list[self.animal_index]
        animal_data = self.animals[selected_animal]
        animal_img = animal_data["image"]
        self.screen.blit(animal_img, (140, 100))

        #create green boarder for image
        img_boarder = (203, 236, 164)
        img_rect = animal_img.get_rect(topleft=(140,100)) 
        pygame.draw.rect(self.screen, img_boarder, img_rect, 10)

        #display hint button
        self.screen.blit(self.hint_button, (735, 15))

        #display submit button
        self.screen.blit(self.submit_button, (735, 325))

        #display back button
        self.screen.blit(self.back_button, (40, 15))

        #display score 
        score_text = font.render("Score: " + str(self.score), True, "black")
        self.screen.blit(score_text, (900, 15))

        #display user input box
        pygame.draw.rect(self.screen, self.colour, self.input_rect)
        font1 = pygame.font.SysFont("arialblack", 40)
        text = font1.render(self.user_text, True, "black")
        self.screen.blit(text, (self.input_rect.x + 10, self.input_rect.y + 10))

        #only allow letters within the box
        text_width = text.get_width()
        if text_width > self.input_rect.width - 5:
            self.user_text = self.user_text[:-1]

        #when user submits an answer, check answer
        if self.answered and self.questions_answered != 10:
            self.check_answer(self.user_text)
            if self.correct_answer:
                self.display_answer("Correct! This is a %s." % (selected_animal.lower()), "green")
                self.screen.blit(self.next_button, (1075, 650))
            else:
                self.display_answer("Incorrect. The correct answer is %s." % (selected_animal.lower()), "red")
                self.screen.blit(self.next_button, (1075, 650))

        #display keys for keyboard - first row
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
        #second row
        self.screen.blit(self.key_a, (758, 445))
        self.screen.blit(self.key_s, (803, 445))
        self.screen.blit(self.key_d, (848, 445))
        self.screen.blit(self.key_f, (893, 445))
        self.screen.blit(self.key_g, (938, 445))
        self.screen.blit(self.key_h, (983, 445))
        self.screen.blit(self.key_j, (1028, 445))
        self.screen.blit(self.key_k, (1073, 445))
        self.screen.blit(self.key_l, (1118, 445))
        #third row
        self.screen.blit(self.key_z, (781, 490))
        self.screen.blit(self.key_x, (826, 490))
        self.screen.blit(self.key_c, (871, 490))
        self.screen.blit(self.key_v, (916, 490))
        self.screen.blit(self.key_b, (961, 490))
        self.screen.blit(self.key_n, (1006, 490))
        self.screen.blit(self.key_m, (1051, 490))
        #backspace
        self.screen.blit(self.key_back, (1096, 490))

        #level complete and congrats image is displayed if user answers 10 questions
        if self.questions_answered == 10:
            self.screen.blit(self.congrats, (315, 160))
            #show buttons on congrats image
            self.screen.blit(self.levels_button, (368, 450))
            self.screen.blit(self.save_game_button, (561, 450))
            self.active = False
            self.answered = True
            self.hardLevel_complete = True

        pygame.display.update()
        self.clock.tick(60)

    def user_input(self, event, save):
        """
        This method handles user input for the game.
        :param event: the event to handle
        :param save: the save file to save the game
        """
        pos = pygame.mouse.get_pos()#get mouse position

        if event.type == pygame.MOUSEBUTTONDOWN:
            #back button
            back_button = pygame.Rect(40, 15, 70, 70)
            if back_button.collidepoint(pos):
                self.__init__(self.screen, self.animals, self.game_state)#reset game
                self.game_state.set_state('animalLevels')
            #check if user answered the question, otherwise allow them to click the keyboard buttons
            if not self.answered: 
                if self.input_rect.collidepoint(event.pos):
                    self.active = True
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

                #play sound on hint button click
                hint_rect = pygame.Rect(735, 15, 130, 70)
                if hint_rect.collidepoint(pos):
                    selected_animal = self.animal_list[self.animal_index]
                    animal_data = self.animals[selected_animal]
                    animal_sound = animal_data["sound"]
                    animal_sound.play()

                #submit answer
                submit_rect = pygame.Rect(735, 325, 450, 50)
                if submit_rect.collidepoint(pos):
                    self.submit_clicked = True

                #check user answer and play corresponding sound
                if self.submit_clicked and self.questions_answered != 10:
                    self.check_answer(self.user_text)
                    self.answered = True
                    if self.correct_answer:
                        self.correct_sound.play(loops=0)
                        self.submit_clicked = False
                    else:
                        self.incorrect_sound.play(loops=0)
                        self.submit_clicked = False

            #display next button and update score if user answers correctly
            if self.answered and self.questions_answered != 10:
                next_rect = pygame.Rect(1075, 650, 175, 50)
                if next_rect.collidepoint(pos):
                    if self.correct_answer:
                        self.update_score()
                        self.next_question()
                    else:
                        self.next_question()
            #display next level button and save game button
            if self.questions_answered == 10:
                self.active = False
                levels_rect = pygame.Rect(368, 450, 159, 65)
                saveGame_rect = pygame.Rect(561, 450, 159, 65)
                if saveGame_rect.collidepoint(pos):
                    self.save_game = True
                    saveGame(save, 3, 3) #save game
                if levels_rect.collidepoint(pos):
                    if self.save_game == False:
                        self.__init__(self.screen, self.animals, self.game_state) #reset game
                    self.game_state.set_state('animalLevels')

        elif event.type == pygame.KEYDOWN and self.active:
            #allow user to type in the box with physical keyboard
            if event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            else:
                key_name = pygame.key.name(event.key)
                if len(key_name) == 1:
                    self.user_text += key_name
    
        #change colour of box when clicked
        if self.active:
            self.colour = self.colour_textbox_click
        else:
            self.colour = self.colour_textbox_passive

    def check_answer(self, user_input):
        """
        This method checks the user's answer.
        :param user_input: the String of the user's input
        """
        correct_ans = self.animal_list[self.animal_index]

        if user_input.lower() == correct_ans.lower():
            self.correct_answer = True
        else:
            self.correct_answer = False

    def display_answer(self, message, colour):
        """
        This method displays the answer to the user.
        :param message: the message to display to the user
        :param colour: the colour of the message
        """
        text = self.font.render(message, True, colour)
        text_rect = text.get_rect(center=(1280 // 2, 675))
        self.screen.blit(text, text_rect)

    def next_question(self):
        """
        This method moves on to the next question.
        """
        self.answered = False
        self.correct_answer = False #reset correct answer
        self.user_text = '' #reset user text
        self.animal_index += 1 #increment to iterate values in dict
        self.submit_clicked = False
        self.answered = False
        self.questions_answered += 1
        self.active = False
