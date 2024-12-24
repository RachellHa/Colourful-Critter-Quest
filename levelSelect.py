import pygame
import pydoc

class createButton:
    '''
            Author: Ethan Lui
            Purpose: This class was created to condense code to make it more readable and less repetitive. A helper function.
    '''
    def __init__(self, x, y, distx, disty, font, string):
        '''
            This method is run on object generation/initialization.
            :param x: How big the button is, horizontally.
            :param y: How big the button is, vertically.
            :param distx: How far the button is, from the left side of the display window.
            :param disty: How far the button is, from the top side of the display window.
            :param font: The Font.
            :param string: The text that will be displayed on the button.
        '''
        self.surface = pygame.Surface((x, y))
        self.surface.fill((219,235,235))
        self.text = font.render(string, True, (0,0,0))
        self.textRect = self.text.get_rect(center = (self.surface.get_width()/2, self.surface.get_height()/2))
        self.theRect = pygame.Rect(distx, disty, x, y)

class createText:
    '''
            Author: Ethan Lui
            Purpose: This class was created to condense code to make it more readable and less repetitive.
        '''
    def __init__(self, font, text, color1, color2, xcenter, yTop):
        '''
            This method is run on object generation/initialization.
            :param font: The font.
            :param text: The text displayed.
            :param color1: The color of the actually letters.
            :param color2: The color of the background of the text rectangle.
            :param xcenter: The center of the title.
            :param yTop: How far from the top the rectangle will be rendered.
        '''
        self.text = font.render(text, True, color1, color2)
        self.text_Rect = self.text.get_rect()
        self.text_Rect.center = (xcenter, yTop)

class levelSelection:
    '''
            Author: Ethan Lui
            Purpose: To Display the level selection screen so the user can choose which game to play.
        '''
    def __init__ (self, screen, game_state, save, exist):
        '''
            This method is run on object generation/initialization.
            This checks the save files emptiness, and fills it if it is.
            This method also generates all of the buttons/text needed for rendering.
            :param screen: The Display screen that is maintained across all modules.
            :param save: The save that is being used.
            :param empty: Whether or not the save is empty, a new save.
        '''
        self.screen = screen
        self.font = pygame.font.SysFont("arial", 24)
        self.back_button = pygame.image.load("assets/levelPage/backButton.png").convert_alpha()
        self.game_state = game_state

        if exist == False:
            self.colorLevel = 1
            self.mathLevel = 1
            self.animalLevel = 1
            f = open(save, "w")
            f.write("1\n")
            f.write("1\n")
            f.write("1\n")
            f.close()
            # Writes to the file and stores level 1 in every game, a new game.
        else:
            fileOpener = open(save, 'r')
            self.colorLevel = int(fileOpener.readline().strip())
            self.mathLevel = int(fileOpener.readline().strip())
            self.animalLevel = int(fileOpener.readline().strip())
            if (self.colorLevel == 4):
                self.colorLevel = 3
            elif (self.mathLevel == 4):
                self.mathLevel = 3
            elif (self.animalLevel == 4):
                self.animalLevel = 3

        # We now have every the levels that are required.

        #Okay, now we have to make 9 buttons, a title, and 3 game titles, and a back button.
        self.colorContinue = createButton(400, 75, 200, 160, self.font, "Continue Level " + str(self.colorLevel)) #260
        self.colorView = createButton(400, 75, 200, 220, self.font, "View All Levels")
        self.animalContinue = createButton(400, 75, 440, 490, self.font, "Continue Level " + str(self.animalLevel))
        self.animalView = createButton(400, 75, 440, 550, self.font, "View All Levels")
        self.mathContinue = createButton(400, 75, 720, 160, self.font, "Continue Level " + str(self.mathLevel)) #260
        self.mathView = createButton(400, 75, 720, 220, self.font, "View All Levels")
        self.back_buttonRect = pygame.Rect(40, 15, 70, 70)
                

        self.mathTitle = createText(self.font, "Math Mania", (0,0,0), (203,236,164), 920, 110) #210
        self.animalTitle = createText(self.font, "Animal Typing Safari", (0,0,0), (203,236,164), 640, 455)
        self.colorTitle = createText(self.font, "Rainbow Rumble", (0,0,0), (203,236,164), 400, 110) #210
        self.mainTitle = createText(pygame.font.SysFont("arial", 40), "SAVED GAMES", (0,0,0), (255,255,255), 1280/2, 50)

        # All buttons and text boxes created.

    def run(self):
        '''
           This function is run when the levelSelect module needs to be displayed.
           This function is the function that renders the buttons created during initialization.
            :return: Void, no return.
       '''
        self.screen.fill("beige")
        pygame.display.set_caption('Level Selection')

        self.colorContinue.surface.blit(self.colorContinue.text, self.colorContinue.textRect)
        self.mathContinue.surface.blit(self.mathContinue.text, self.mathContinue.textRect)
        self.animalContinue.surface.blit(self.animalContinue.text, self.animalContinue.textRect)
        self.colorView.surface.blit(self.colorView.text, self.colorView.textRect)
        self.mathView.surface.blit(self.mathView.text, self.mathView.textRect)
        self.animalView.surface.blit(self.animalView.text, self.animalView.textRect)
        
        self.screen.blit(self.colorContinue.surface, (self.colorContinue.theRect.x, self.colorContinue.theRect.y))
        self.screen.blit(self.mathContinue.surface, (self.mathContinue.theRect.x, self.mathContinue.theRect.y))
        self.screen.blit(self.animalContinue.surface, (self.animalContinue.theRect.x, self.animalContinue.theRect.y))
        self.screen.blit(self.colorView.surface, (self.colorView.theRect.x, self.colorView.theRect.y))
        self.screen.blit(self.mathView.surface, (self.mathView.theRect.x, self.mathView.theRect.y))
        self.screen.blit(self.animalView.surface, (self.animalView.theRect.x, self.animalView.theRect.y))
        self.screen.blit(self.back_button, (40, 15))

        # Display Titles
        self.screen.blit(self.mathTitle.text, self.mathTitle.text_Rect)
        self.screen.blit(self.colorTitle.text, self.colorTitle.text_Rect)
        self.screen.blit(self.animalTitle.text, self.animalTitle.text_Rect)
        self.screen.blit(self.mainTitle.text, self.mainTitle.text_Rect)

        pygame.display.update()

    def user_input(self, event):
        '''
        The Event Handler for the levelSelect module.
        :param event:
        :return:
        '''

        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Remove the print statements when adding module navigation.
            # They exist to stop Python from throwing a fit.
            if self.colorContinue.theRect.collidepoint(pos):
                # Open up the appropriate color level depending on the value
                # stored in self.colorLevel
                if self.colorLevel == 1:
                    self.game_state.set_state('colourEasy')
                elif self.colorLevel == 2:
                    self.game_state.set_state('colourMed')
                elif self.colorLevel == 3:
                    self.game_state.set_state('colourHard')
            elif self.colorView.theRect.collidepoint(pos):
                # View the different color levels available.
                self.game_state.set_state('colourLevels')
            elif self.mathContinue.theRect.collidepoint(pos):
                # Open up the appropriate math level depending on the value
                # stored in self.mathLevel
                if self.mathLevel == 1:
                    self.game_state.set_state('mathEasy')
                elif self.mathLevel == 2:
                    self.game_state.set_state('mathMed')
                elif self.mathLevel == 3:
                    self.game_state.set_state('mathHard')
            elif self.mathView.theRect.collidepoint(pos):
                self.game_state.set_state('mathLevels')
            elif self.animalContinue.theRect.collidepoint(pos):
                # Open up the appropriate animal level depending on the value
                # stored in self.animal level.
                if self.animalLevel == 1:
                    self.game_state.set_state('animalEasy')
                elif self.animalLevel == 2:
                    self.game_state.set_state('animalMed')
                elif self.animalLevel == 3:
                    self.game_state.set_state('animalHard')
            elif self.animalView.theRect.collidepoint(pos):
                self.game_state.set_state('animalLevels')
            elif self.back_buttonRect.collidepoint(pos):
                # Returns to the saves/loads game screen.
                self.game_state.set_state('loadGame')
