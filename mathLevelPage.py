import pygame
from easyMath import EasyMath
from medMath import MedMath
from hardMath import HardMath
import pydoc

class MathLevelPage:
    """
    Author: Lily So
    This class is used to display the math level page. It contains the easy, medium and hard level buttons.
    """
    def __init__(self, screen, game_state):
        """
        This method initializes the math level page.
        :param screen: the screen to display the math level page
        :param game_state: the current state of the game
        """
        self.screen = screen
        self.game_state = game_state

        #load images/buttons for this page
        self.mathTitle = pygame.image.load("assets/mathLevel/mathMania.png").convert_alpha()
        self.easyLevel = pygame.image.load("assets/mathLevel/easyLevel.png").convert_alpha()
        self.medLevel = pygame.image.load("assets/mathLevel/medLevel.png").convert_alpha()
        self.hardLevel = pygame.image.load("assets/mathLevel/hardLevel.png").convert_alpha()
        self.backButton = pygame.image.load("assets/animalLevel/backButton.png").convert_alpha()

        #create button rectangles
        self.levelEasyRect = pygame.Rect(200, 155, 880, 145)
        self.levelMedRect = pygame.Rect(200, 333, 880, 145)
        self.levelHardRect = pygame.Rect(200, 511, 880, 145)
        self.backButtonRect = pygame.Rect(106, 45, 70, 70)

        #initialize math levels
        self.easy_math = EasyMath(self.screen, self.game_state)
        self.med_math = MedMath(self.screen, self.game_state)
        self.hard_math = HardMath(self.screen, self.game_state)

    def run(self):
        """
        This method runs the math level page.
        """
        self.screen.fill('beige')
        pygame.display.set_caption("Math Mania Levels")
        self.screen.blit(self.mathTitle, (290, 40))
        self.screen.blit(self.easyLevel, (200, 155))
        self.screen.blit(self.medLevel, (200, 333))
        self.screen.blit(self.hardLevel, (200, 511))

        #display back button
        self.screen.blit(self.backButton, (106, 45))

    def user_input(self, event, save):
        """
        This method handles the user input for the math level page.
        :param event: the event that the user inputs
        """
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #change state based on button clicked
            if self.levelEasyRect.collidepoint(pos):
                self.game_state.set_state('mathEasy')
            if self.levelMedRect.collidepoint(pos):
                self.game_state.set_state('mathMed')
            if self.levelHardRect.collidepoint(pos):
                self.game_state.set_state('mathHard')
            if self.backButtonRect.collidepoint(pos):
                self.game_state.set_state('levels')
        #pass user input to the coressponding level
        if self.game_state.get_state() == 'mathEasy':
            self.easy_math.user_input(event, save)
        elif self.game_state.get_state() == 'mathMed':
            self.med_math.user_input(event, save)
        elif self.game_state.get_state() == 'mathHard':
            self.hard_math.user_input(event, save)

