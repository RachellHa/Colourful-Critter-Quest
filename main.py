import pygame
from gameState import GameState
from menu import MainMenu
from animalLevelPage import AnimalLevelPage
from levels import Levels
from mathLevelPage import MathLevelPage
from colourLevelPage import ColourLevelPage
from tutorial import Tutorial
from highscores import Highscores
from loadGame import loadsGame
import pydoc
import sys

class Game:
    """
    Author: Lily So
    This class is used to run the game, preloads the games and handle the game state and user events.
    """

    def __init__(self):
        """
        This method initializes the game.
        """
        self.saveFile = None
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720)) #set screen
        self.clock = pygame.time.Clock()

        self.game_state = GameState('menu') #set initial state to menu
        #initialize all the pages
        self.menu = MainMenu(self.screen, self.game_state, self)
        self.levels = Levels(self.screen, self.game_state)
        self.tutorial = Tutorial(self.screen, self.game_state)
        self.highscores = Highscores(self.screen, self.game_state)
        self.animalLevels = AnimalLevelPage(self.screen, self.game_state)
        self.mathLevels = MathLevelPage(self.screen, self.game_state)
        self.colourLevels = ColourLevelPage(self.screen, self.game_state)
        self.load_game = loadsGame(self.screen, self.game_state, self)

        self.level_select = None
        
        #animal levels
        self.easy_game = AnimalLevelPage(self.screen, self.game_state).easy_game
        self.med_game = AnimalLevelPage(self.screen, self.game_state).med_game
        self.hard_game = AnimalLevelPage(self.screen, self.game_state).hard_game
    
        #math levels
        self.easy_math = MathLevelPage(self.screen, self.game_state).easy_math
        self.med_math = MathLevelPage(self.screen, self.game_state).med_math
        self.hard_math = MathLevelPage(self.screen, self.game_state).hard_math

        #colour levels
        self.easy_colour = ColourLevelPage(self.screen, self.game_state).easy_colour
        self.med_colour = ColourLevelPage(self.screen, self.game_state).med_colour
        self.hard_colour = ColourLevelPage(self.screen, self.game_state).hard_colour

        #store all the states in dictionary
        self.states = {'menu': self.menu,
                       'levels': self.levels,
                       'loadGame': self.load_game,
                       'tutorial': self.tutorial,
                       'highscores': self.highscores,
                       'mathLevels': self.mathLevels,
                       'mathEasy': self.easy_math,
                       'mathMed': self.med_math,
                       'mathHard': self.hard_math,
                       'animalLevels': self.animalLevels,
                       'animalEasy': self.easy_game,
                       'animalMed': self.med_game,
                       'animalHard': self.hard_game,
                       'colourLevels': self.colourLevels,
                       'colourEasy': self.easy_colour,
                       'colourMed': self.med_colour,
                       'colourHard': self.hard_colour
                       }

    def run(self):
        """
        This method runs the game and handles all the events.
        """
        pygame.display.set_caption("Colourful Critter Quest")
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                #pass user input to the current state
                if self.game_state.get_state() == 'menu':
                    self.menu.user_input(event)
                elif self.game_state.get_state() == 'levels':
                    self.levels.user_input(event)
                elif self.game_state.get_state() == 'loadGame':
                    self.load_game.user_input(event)
                elif self.game_state.get_state() == 'levelSelect':
                    self.level_select.user_input(event)
                elif self.game_state.get_state() == 'tutorial':
                    self.tutorial.user_input(event)
                elif self.game_state.get_state() == 'highscores':
                    self.highscores = Highscores(self.screen, self.game_state)
                    self.states.update({'highscores':self.highscores})
                    self.highscores.user_input(event)
                elif self.game_state.get_state() == 'animalLevels':
                    self.animalLevels.user_input(event, self.saveFile)
                elif self.game_state.get_state() == 'animalEasy':
                    self.easy_game.user_input(event, self.saveFile)
                elif self.game_state.get_state() == 'animalMed':
                    self.med_game.user_input(event, self.saveFile)
                elif self.game_state.get_state() == 'animalHard':
                    self.hard_game.user_input(event, self.saveFile)
                elif self.game_state.get_state() == 'mathLevels':
                    self.mathLevels.user_input(event, self.saveFile)
                elif self.game_state.get_state() == 'mathEasy':
                    self.easy_math.user_input(event, self.saveFile)
                elif self.game_state.get_state() == 'mathMed':
                    self.med_math.user_input(event, self.saveFile)
                elif self.game_state.get_state() == 'mathHard':
                    self.hard_math.user_input(event, self.saveFile)
                elif self.game_state.get_state() == 'colourLevels':
                    self.colourLevels.user_input(event, self.saveFile)
                elif self.game_state.get_state() == 'colourEasy':
                    self.easy_colour.user_input(event, self.saveFile)
                elif self.game_state.get_state() == 'colourMed':
                    self.med_colour.user_input(event, self.saveFile)
                elif self.game_state.get_state() == 'colourHard':
                    self.hard_colour.user_input(event, self.saveFile)
                
            self.states[self.game_state.get_state()].run() #run the current state

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()

