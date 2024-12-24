import pygame
from loadGame import loadsGame
import pydoc
import sys

class MainMenu:
    """
    Author: Lily So
    This class is used to display the main menu page. It contains the new game, load game, tutorial, highscores and exit buttons.
    """
    def __init__(self, screen, game_state, game):
        """
        This method initializes the main menu page.
        :param screen: the screen to display the main menu page
        :param game_state: the current state of the game
        :param game: the game object
        """
        self.game = game
        self.screen = screen
        self.game_state = game_state

        #load title
        self.bigTitle = pygame.image.load('assets/mainMenuButtons/bigTitle.png').convert_alpha()

        #load menu buttons
        self.new_game_img = pygame.image.load('assets/mainMenuButtons/new_game.png').convert_alpha()
        self.load_game_img = pygame.image.load('assets/mainMenuButtons/load_game.png').convert_alpha()
        self.tutorial_img = pygame.image.load('assets/mainMenuButtons/tutorial.png').convert_alpha()
        self.highscores_img = pygame.image.load('assets/mainMenuButtons/highscores.png').convert_alpha()
        self.exit_img = pygame.image.load('assets/mainMenuButtons/exit.png').convert_alpha()

        #create button rectangles
        self.new_game_button = pygame.Rect(485, 259, 310, 58)
        self.load_game_button = pygame.Rect(485, 333, 310, 58)
        self.tutorial_button = pygame.Rect(485, 406, 310, 58)
        self.highscores_button = pygame.Rect(485, 480, 310, 58)
        self.exit_button = pygame.Rect(485, 554, 310, 58)

        #main menu images
        self.duck_img = pygame.image.load('assets/mainMenu/duck.png').convert_alpha()
        self.math_img = pygame.image.load('assets/mainMenu/mathImg.png').convert_alpha()
        self.rgb_img = pygame.image.load('assets/mainMenu/rgb.png').convert_alpha()
        self.cat_img = pygame.image.load('assets/mainMenu/cat.png').convert_alpha()

    def run(self):
        """
        This method runs the main menu page.
        """
        self.screen.fill('beige')
        self.screen.blit(self.bigTitle, (67, 35))

        #display credits
        font = pygame.font.SysFont("arial", 20)
        text_surface1 = font.render("Created by: Team 77 - Lily So, Ethan Lui, Ethne Au, Rachel Ha, Michelle Ko", True, "black")
        text_surface2 = font.render("Created as part of CS2212 @ Western Universtiy | Winter 2024", True, "black")
        self.screen.blit(text_surface1, (30, 660))
        self.screen.blit(text_surface2, (30, 680))

        #display main menu images
        self.screen.blit(self.duck_img, (74, 218))
        self.screen.blit(self.math_img, (962, 264))
        self.screen.blit(self.rgb_img, (946, 457))
        self.screen.blit(self.cat_img, (198, 396))


        #display menu buttons
        self.screen.blit(self.new_game_img, (485, 259))
        self.screen.blit(self.load_game_img, (485, 333))
        self.screen.blit(self.tutorial_img, (485, 406))
        self.screen.blit(self.highscores_img, (485, 480))
        self.screen.blit(self.exit_img, (485, 554))

    def user_input(self, event):
        """
        This method handles the user input for the main menu page.
        :param event: the event that the user inputs
        """
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #change state based on button clicked
            if self.new_game_button.collidepoint(pos):
                self.game_state.set_state('loadGame')
            elif self.load_game_button.collidepoint(pos):
                self.game.load_game = loadsGame(self.screen, self.game_state, self.game)
                self.game.states.update({'loadGame':self.game.load_game})
                self.game_state.set_state('loadGame')
            elif self.tutorial_button.collidepoint(pos):
                self.game_state.set_state('tutorial')
            elif self.highscores_button.collidepoint(pos):
                self.game_state.set_state('highscores')
            elif self.exit_button.collidepoint(pos):
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


        
