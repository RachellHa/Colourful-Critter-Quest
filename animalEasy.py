import pygame
import random
import pydoc
from saveGame import saveGame

class AnimalEasy:
    """
    Author: Lily So
    This class was created to display the easy level of the animal typing safari game.
    """
    def __init__(self, screen, animals, game_state):
        """
        This method initializes the AnimalEasy class.
        :param screen: the screen to display the game on
        :param animals: the dictionary of animals and their data
        :param game_state: the current state of the game
        """
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.game_state = game_state
        self.animals = animals
        screen = pygame.display.set_mode((1280, 720)) 
        self.font = pygame.font.SysFont("arial", 40)

        #load background buttons
        self.button_img = pygame.image.load("assets/animalQuestionAssets/mc_button.png").convert_alpha()
        self.button_hover_img = pygame.image.load("assets/animalQuestionAssets/mc_hover_button.png").convert_alpha()

        #load hint button
        self.hint_button = pygame.image.load("assets/animalQuestionAssets/hint_button.png").convert_alpha()

        #load next button
        self.next_button = pygame.image.load("assets/animalQuestionAssets/next_button.png").convert_alpha()

        #load correct sound
        self.correct_sound = pygame.mixer.Sound("assets/animalQuestionAssets/correctSound.mp3")

        #load incorrect sound
        self.incorrect_sound = pygame.mixer.Sound("assets/animalQuestionAssets/incorrectSound.mp3")

        #load congrats image
        self.congrats = pygame.image.load("assets/animalQuestionAssets/congrats.png").convert_alpha()

        #load extra buttons on congrats image
        self.levels_button = pygame.image.load("assets/animalQuestionAssets/levels.png").convert_alpha()
        self.next_level_button = pygame.image.load("assets/animalQuestionAssets/nextLevel.png").convert_alpha()
        self.save_game_button = pygame.image.load("assets/animalQuestionAssets/saveGame.png").convert_alpha()

        #load back button
        self.back_button = pygame.image.load("assets/animalLevel/backButton.png").convert_alpha()
        
        self.selected_animal = None #selected animal from the list
        self.animal_index = 0 #index of the selected animal
        self.iter = 0 #the iterations of the animal keys in list
        self.animal_keys = list(animals.keys()) #convert animal dict into list of keys
        random.shuffle(self.animal_keys)#gets a new list every game start
        self.options = self.multiple_choice(self.animal_keys)#list of animal options
        self.selected_option = None #user selected option
        self.correct_answer = False
        self.hovered = None #check if hovered or not
        self.score = 0 # set score
        self.answered = False
        self.questions_answered = 0 #tracking number of questions answered
        self.save_game = False #user clicked save game button

    def multiple_choice(self, animal_keys):
        """
        This method creates a multiple choice options for the user.
        :param animal_keys: list of animal keys
        """
        self.selected_animal = animal_keys[self.iter] #select animal from list from every iteration
        other_options = []
        #append all other options except the selected animal
        for key in animal_keys:
            if key != self.selected_animal:
                other_options.append(key)

        options = random.sample(other_options, 3) #get 3 other options
        multiple_choice_options = [] #list for all 4 values
        multiple_choice_options = [self.selected_animal]
        multiple_choice_options.extend(options) #extend the rest of the values into end of list
        random.shuffle(multiple_choice_options) #shuffle list
        self.animal_index = multiple_choice_options.index(self.selected_animal) #index of the answer
        
        return multiple_choice_options
    
    def run(self):
        """
        This method runs the game and displays the interface of the easy game.
        """
        self.screen.fill("beige")
        pygame.display.set_caption("Animal Typing Safari")
        font = pygame.font.SysFont("arialblack", 45)
        img = font.render("What animal is this?", True, "black")
        self.screen.blit(img, (150, 15))

        animal_answer = self.options[self.animal_index] 
        animal_data = self.animals[animal_answer]
        animal_img = animal_data["image"]
        self.screen.blit(animal_img, (140, 100))

        #create green boarder for image
        img_boarder = (203, 236, 164)
        img_rect = animal_img.get_rect(topleft=(140,100)) 
        pygame.draw.rect(self.screen, img_boarder, img_rect, 10)

        #display hint button
        self.screen.blit(self.hint_button, (735, 15))

        #display back button
        self.screen.blit(self.back_button, (40, 15))

        #display score 
        score_text = font.render("Score: " + str(self.score), True, "black")
        self.screen.blit(score_text, (900, 15))

        #define multiple choice button values
        col_value = 2
        row_value = 2
        button_width = 220
        button_height = 250
        horizontal_space = 25
        vertical_space = 25
        #create and display the rectangles for the options
        for i, item in enumerate(self.options):
            column = i % col_value
            row = i // row_value
            x = 695 + column * (button_width + horizontal_space)
            y = 100 + row * (button_height + vertical_space)

            button_img = self.button_hover_img if self.hovered == item else self.button_img #hover effect

            self.screen.blit(button_img, (x, y))
            option_surface = self.font.render(item, True, "black")
            option_rect = option_surface.get_rect(center=(x + button_width // 2, y + button_height // 2))
            self.screen.blit(option_surface, option_rect)

        #if user selects an answer output if correct or incorrect then display next button
        if not self.answered and self.selected_option is not None:
            self.check_answer()
            if self.correct_answer:
                self.display_answer("Correct! This is a %s." % (animal_answer.lower()), "green")
                self.screen.blit(self.next_button, (1075, 650))
            else:
                self.display_answer("Incorrect. The correct answer is %s." % (animal_answer.lower()), "red")
                self.screen.blit(self.next_button, (1075, 650))

        #level complete if 10 questions are answered
        if self.questions_answered == 10:
            self.screen.blit(self.congrats, (315, 160))
            #show buttons on congrats screen
            self.screen.blit(self.levels_button, (368, 450))
            self.screen.blit(self.save_game_button, (561, 450))
            self.screen.blit(self.next_level_button, (753, 450))
            self.answered = True
            
        pygame.display.update()
        self.clock.tick(60)

    def user_input(self, event, save):
        """
        This method handles user input for the game.
        :param event: the event that the user inputs
        :param save: the save file to save the game
        """
        #define multiple choice button values
        button_width = 220
        button_height = 250
        horizontal_space = 25
        vertical_space = 25
        
        pos = pygame.mouse.get_pos()#get mouse position
    
        if event.type == pygame.MOUSEBUTTONDOWN and self.selected_option is None:
            #if user answered 10 questions, display congrats screen with buttons
            if self.questions_answered == 10:
                levels_rect = pygame.Rect(368, 450, 159, 65)
                saveGame_rect = pygame.Rect(561, 450, 159, 65)
                nextLevel_rect = pygame.Rect(753, 450, 159, 65)
                #if user clicked on buttons
                if saveGame_rect.collidepoint(pos):
                    self.save_game = True #if user clicked save game
                    saveGame(save, 3, 1) #save game into file
                if levels_rect.collidepoint(pos):
                    if self.save_game == False:
                        self.__init__(self.screen, self.animals, self.game_state)#reset game
                    self.game_state.set_state('animalLevels')
                if nextLevel_rect.collidepoint(pos):
                    if self.save_game == False:
                        self.__init__(self.screen, self.animals, self.game_state)#reset game
                    self.game_state.set_state('animalMed')
            #if user has not answered the question
            if not self.answered:
                for i, option in enumerate(self.options):
                    column = i % 2
                    row = i // 2
                    x = 695 + column * (button_width + horizontal_space)
                    y = 100 + row * (button_height + vertical_space)
                    option_rectangle = pygame.Rect(x, y, button_width, button_height)
                    #if user clicked on option
                    if option_rectangle.collidepoint(pos):
                        self.selected_option = option
                        #check if answer is correct and play sound depending on answer
                        self.check_answer()
                        if self.correct_answer:
                            self.correct_sound.play(loops=0)
                        else:
                            self.incorrect_sound.play(loops=0)

                #play animal sound if hint buttton is clicked
                hint_rect = pygame.Rect(735, 15, 130, 70)
                if hint_rect.collidepoint(pos):
                    animal_choice = self.options[self.animal_index]
                    animal_data = self.animals[animal_choice]
                    animal_sound = animal_data["sound"]
                    animal_sound.play()
                #if back button is clicked, go back to animal levels
                back_button = pygame.Rect(40, 15, 70, 70)
                if back_button.collidepoint(pos):
                    self.__init__(self.screen, self.animals, self.game_state)#reset game
                    self.game_state.set_state('animalLevels')
 
        #if user clicks on next button, on correct answer increase score and go to next question
        elif event.type == pygame.MOUSEBUTTONDOWN and self.selected_option is not None:
            next_rect = pygame.Rect(1075, 650, 175, 50)
            if next_rect.collidepoint(pos):
                self.check_answer()
                if self.correct_answer:
                    self.update_score()
                    self.next_question()
                else:
                    self.next_question()
        
        elif event.type == pygame.KEYDOWN:
            #if user presses spacebar, go to next question
            if self.selected_option is not None and event.key == pygame.K_SPACE:
                self.next_question()
            else:
                self.selected_option = None
            #if user presses h, play animal sound
            if event.key == pygame.K_h:
                animal_choice = self.options[self.animal_index]
                animal_data = self.animals[animal_choice]
                animal_sound = animal_data["sound"]
                animal_sound.play()
        #if user hovers over option, change to the hover image
        elif event.type == pygame.MOUSEMOTION:
            self.mouseover()

    def update_score(self):
        """
        This method updates the score of the user.
        """
        self.score += 10

    def check_answer(self):
        """
        This method checks if the user's answer is correct or not.
        """
        correct_ans = self.options[self.animal_index]
        if self.selected_option == correct_ans:
            self.correct_answer = True
        else:
            self.correct_answer = False

    def mouseover(self):
        """
        This method checks if the user hovers over an option.
        """
        button_width = 220
        button_height = 250
        horizontal_space = 25
        vertical_space = 25
        
        pos = pygame.mouse.get_pos()
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

    def display_answer(self, message, colour):
        """
        This method displays the answer of the user.
        :param message: the message to display
        :param colour: the colour of the message
        """
        text = self.font.render(message, True, colour)
        text_rect = text.get_rect(center=(1280 // 2, 675))
        self.screen.blit(text, text_rect)

    def next_question(self):
        """
        This method changes the question to the next question by incrementing the list index.
        """
        self.iter += 1 #increment list, index of dict keys
        self.options = self.multiple_choice(self.animal_keys) #shuffle options
        self.selected_option = None #reset option
        self.correct_answer = False #reset correct answer
        self.questions_answered += 1
