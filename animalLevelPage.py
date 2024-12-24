import pygame
from animalEasy import AnimalEasy
from animalMed import AnimalMed
from easyAnimalDict import AnimalDictEasy
from medAnimalDict import AnimalDictMed
from animalHard import AnimalHard
import pydoc

class AnimalLevelPage:
    """
    Author: Lily So
    This class is used to display the animal level page. It contains the easy, medium and hard level buttons.
    """
    def __init__(self, screen, game_state):
        """
        This method initializes the animal level page.
        :param screen: the screen to display the animal level page
        :param game_state: the current state of the game
        """
        self.screen = screen
        self.game_state = game_state

        #load images buttons/images for this page
        self.animalTitle = pygame.image.load("assets/animalLevel/animalTypingSafari.png").convert_alpha()
        self.easyLevel = pygame.image.load("assets/animalLevel/easyLevel.png").convert_alpha()
        self.medLevel = pygame.image.load("assets/animalLevel/medLevel.png").convert_alpha()
        self.hardLevel = pygame.image.load("assets/animalLevel/hardLevel.png").convert_alpha()
        self.backButton = pygame.image.load("assets/animalLevel/backButton.png").convert_alpha()

        #create button rectangles
        self.levelEasyRect = pygame.Rect(200, 155, 880, 145)
        self.levelMedRect = pygame.Rect(200, 333, 880, 145)
        self.levelHardRect = pygame.Rect(200, 511, 880, 145)
        self.backButtonRect = pygame.Rect(106, 45, 70, 70)

        #initialize animal levels
        self.easy_animals = AnimalDictEasy().easy_animals #get easy animals dict
        self.easy_game = AnimalEasy(self.screen, self.easy_animals, self.game_state)

        self.med_animals = AnimalDictMed().med_animals # get med animals dict
        self.med_game = AnimalMed(self.screen, self.med_animals, self.game_state)
        
        #combine easy and med animal dicts
        self.combined_dict = self.easy_animals.copy()
        self.combined_dict.update(self.med_animals)

        self.hard_game = AnimalHard(self.screen, self.combined_dict, self.game_state)

    def run(self):
        """
        This method runs the animal level page.
        """
        self.screen.fill('beige')
        pygame.display.set_caption("Animal Typing Safari Levels") 
        self.screen.blit(self.animalTitle, (290, 40))
        self.screen.blit(self.easyLevel, (200, 155))
        self.screen.blit(self.medLevel, (200, 333))
        self.screen.blit(self.hardLevel, (200, 511))

        #display back button
        self.screen.blit(self.backButton, (106, 45))


    def user_input(self, event, save):
        """
        This method handles the user input for the animal level page.
        :param event: the event that the user inputs
        """
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #change state based on button clicked
            if self.levelEasyRect.collidepoint(pos):
                self.game_state.set_state('animalEasy')
            if self.levelMedRect.collidepoint(pos):
                self.game_state.set_state('animalMed')
            if self.levelHardRect.collidepoint(pos):
                self.game_state.set_state('animalHard')
            if self.backButtonRect.collidepoint(pos):
                self.game_state.set_state('levels')
        #pass user input to the coressponding level
        if self.game_state.get_state() == 'animalEasy':
            self.easy_game.user_input(event, save)
        elif self.game_state.get_state() == 'animalMed':
            self.med_game.user_input(event, save)
        elif self.game_state.get_state() == 'animalHard':
            self.hard_game.user_input(event, save)

