import pygame
import pydoc

class Levels:
    """
    Author: Lily So
    This class is used to display the levels page. It contains the animal, math and colour level buttons.
    """
    def __init__(self, screen, game_state):
        """
        This method initializes the levels page of all the levels.
        :param screen: the screen to display the levels page
        :param game_state: the current state of the game
        """
        self.screen = screen
        self.game_state = game_state

        #load images buttons/images for this page
        self.level_title = pygame.image.load("assets/levelPage/levels.png").convert_alpha()
        self.animalLevel = pygame.image.load("assets/levelPage/animalLevel.png").convert_alpha()
        self.mathLevel = pygame.image.load("assets/levelPage/mathLevel.png").convert_alpha()
        self.colourLevel = pygame.image.load("assets/levelPage/colourLevel.png").convert_alpha()
        self.backButton = pygame.image.load("assets/levelPage/backButton.png").convert_alpha()

        #create button rectangles
        self.levelAnimalRect = pygame.Rect(200, 155, 880, 145)
        self.levelMathRect = pygame.Rect(200, 333, 880, 145)
        self.levelColourRect = pygame.Rect(200, 511, 880, 145)
        self.backButtonRect = pygame.Rect(106, 45, 70, 70)

    def run(self):
        """
        This method runs the levels page.
        """
        self.screen.fill('beige')
        pygame.display.set_caption("Levels") 
        #display level buttons
        self.screen.blit(self.level_title, (290, 40))
        self.screen.blit(self.animalLevel, (200, 155))
        self.screen.blit(self.mathLevel, (200, 333))
        self.screen.blit(self.colourLevel, (200, 511))

        #display back button
        self.screen.blit(self.backButton, (106, 45))

    def user_input(self, event):
        """
        This method handles the user input for the levels page.
        :param event: the event that the user inputs
        """
        pos = pygame.mouse.get_pos()
        #changes the state based on the button clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.levelAnimalRect.collidepoint(pos):
                self.game_state.set_state('animalLevels')
            if self.levelMathRect.collidepoint(pos):
                self.game_state.set_state('mathLevels')
            if self.levelColourRect.collidepoint(pos):
                self.game_state.set_state('colourLevels')
            if self.backButtonRect.collidepoint(pos):
                self.game_state.set_state('menu')
        
