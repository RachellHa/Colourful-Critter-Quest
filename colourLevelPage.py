import pygame
from EasyColour import EasyColour
from MedColour import MedColour
from HardColour import HardColour
import pydoc

class ColourLevelPage:
    """
    Author: Lily So
    This class is used to display the colour level page. It contains the easy, medium and hard level buttons.
    """
    def __init__(self, screen, game_state):
        """
        This method initializes the colour level page.
        :param screen: the screen to display the colour level page
        :param game_state: the current state of the game
        """
        self.screen = screen
        self.game_state = game_state

        #load images/buttons for this page
        self.colourTitle = pygame.image.load("assets/colourLevel/rainbowRumble.png").convert_alpha()
        self.easyLevel = pygame.image.load("assets/colourLevel/easyLevel.png").convert_alpha()
        self.medLevel = pygame.image.load("assets/colourLevel/medLevel.png").convert_alpha()
        self.hardLevel = pygame.image.load("assets/colourLevel/hardLevel.png").convert_alpha()
        self.backButton = pygame.image.load("assets/colourLevel/backButton.png").convert_alpha()

        #create button rectangles
        self.levelEasyRect = pygame.Rect(200, 155, 880, 145)
        self.levelMedRect = pygame.Rect(200, 333, 880, 145)
        self.levelHardRect = pygame.Rect(200, 511, 880, 145)
        self.backButtonRect = pygame.Rect(106, 45, 70, 70)

        #initialize colour levels
        self.easy_colour = EasyColour(self.screen, self.game_state)
        self.med_colour = MedColour(self.screen, self.game_state)
        self.hard_colour = HardColour(self.screen, self.game_state)

    def run(self):
        """
        This method runs the colour level page.
        """
        self.screen.fill('beige')
        pygame.display.set_caption("Rainbow Rumble Levels")
        self.screen.blit(self.colourTitle, (290, 40))
        self.screen.blit(self.easyLevel, (200, 155))
        self.screen.blit(self.medLevel, (200, 333))
        self.screen.blit(self.hardLevel, (200, 511))

        #display back button
        self.screen.blit(self.backButton, (106, 45))

    def user_input(self, event, save):
        """
        This method handles the user input for the colour level page.
        :param event: the event that the user inputs
        """
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #change state based on button clicked
            if self.levelEasyRect.collidepoint(pos):
                self.game_state.set_state('colourEasy')
            if self.levelMedRect.collidepoint(pos):
                self.game_state.set_state('colourMed')
            if self.levelHardRect.collidepoint(pos):
                self.game_state.set_state('colourHard')
            if self.backButtonRect.collidepoint(pos):
                self.game_state.set_state('levels')
        #pass user input to the coressponding level
        if self.game_state.get_state() == 'colourEasy':
            self.easy_colour.user_input(event, save)
        elif self.game_state.get_state() == 'colourMed':
            self.med_colour.user_input(event, save)
        elif self.game_state.get_state() == 'colourHard':
            self.hard_colour.user_input(event, save)
