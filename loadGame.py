import pygame
import pydoc
from levelSelect import levelSelection
'''
Updates the screen for load game with 4 slots. Each slot is a separate player.
Clicking on one of the saved games will load that game state, and will then show the
3 different games, each with the saved levels of that save file.
Save files are to be stored locally.
'''

# Initializes the load game module.
class loadsGame:
    '''
            Author: Ethan Lui
            Purpose: Loads a specified save file.
    '''
    def __init__(self, screen, game_state, game):
        '''
            This function is run on generation of the loadsGame object.
            This function checks the directory for the 4 save files, if they exist.
            If they do, then the screen will display as such.
            It also creates the buttons required for interactivity.


            :param screen:
        '''
        self.game = game
        # Initializes the loadsGame object
        self.screen = screen
        self.clock = pygame.time.Clock
        self.game_state = game_state
        # screen = pygame.display.set_mode((1280, 720))
        font = pygame.font.SysFont("arial", 30)

        #load title
        self.load_title = pygame.image.load("assets/titles/loadSave.png").convert_alpha()
        self.backButton = pygame.image.load("assets/levelPage/backButton.png").convert_alpha()

    # Searches for the save files, save1.txt, save2.txt, save3.txt, save4.txt.
        # Check if the save files exist. If they do not, simply put "EMPTY" in the save spot.
        try:
            self.save1 = open("save1.txt", "r")
            self.save1 = True
        except FileNotFoundError:
            print("Yes")
            self.save1 = False

        try:
            self.save2 = open("save2.txt", "r")
            self.save2 = True
        except FileNotFoundError:
            self.save2 = False

        try:
            self.save3 = open("save3.txt", "r")
            self.save3 = True
        except FileNotFoundError:
            self.save3 = False

        try:
            self.save4 = open("save4.txt", "r")
            self.save4 = True
        except FileNotFoundError:
            self.save4 = False

        # If a given save does not except(Threw a FileNotFoundError), the given save does not exist.
        # Now we have whether or not to display empty.
        # Creating the buttons and their respective fields require for interactability.
        self.save1Button = pygame.Surface((250, 100))
        self.save1Text = font.render("Empty", True, (255,255,255))
        if (self.save1):
            self.save1Text = font.render("Save 1", True, (255,255,255))
        self.text_rect1 = self.save1Text.get_rect(center = (self.save1Button.get_width()/2, self.save1Button.get_height()/2))
        self.button1 = pygame.Rect(320,180,250,100)


        self.save2Button = pygame.Surface((250,100))
        self.save2Text = font.render("Empty", True, (255,255,255))
        if (self.save2):
            self.save2Text = font.render("Save 2", True, (255,255,255))

        self.text_rect2 = self.save2Text.get_rect(center=(self.save2Button.get_width() / 2, self.save2Button.get_height()/2))
        self.button2 = pygame.Rect(710,180,250,100)


        self.save3Button = pygame.Surface((250,100))
        self.save3Text = font.render("Empty", True, (255,255,255))
        if (self.save3):
            self.save3Text = font.render("Save 3", True, (255,255,255))

        self.text_rect3 = self.save3Text.get_rect(center=(self.save3Button.get_width() / 2, self.save3Button.get_height()/2))
        self.button3 = pygame.Rect(320,540,250,100)


        self.save4Button = pygame.Surface((250,100))
        self.save4Text = font.render("Empty", True, (255,255,255))
        if (self.save4):
            self.save4Text = font.render("Save 4", True, (255,255,255))

        self.text_rect4 = self.save4Text.get_rect(center=(self.save4Button.get_width() / 2, self.save4Button.get_height()/2))
        self.button4 = pygame.Rect(710,540,250,100)

        #create button rect
        self.backButtonRect = pygame.Rect(106, 45, 70, 70)

    '''
    #UI has a back button that lets you return to the main menu,
        self.backButton = pygame.Surface((100,50))
        self.backText = font.render("Back", True, (255,255,255))
        self.backRect = self.backText.get_rect(center = (self.backButton.get_width()/2, self.backButton.get_height()/2))
        self.button5 = pygame.Rect(20,20,100,50)


    # Also create a title surface.

        self.title_text = font.render("Load Save", True, (0,128,255))
        self.title_textRect = self.title_text.get_rect()
        self.title_textRect.center = (1280/2, 90)
    '''

    # Parses the save files. The save files have the format:
    # First line game1, second line game1 levels completed,
    # Third line game2, fourth line game2 levels completed,
    # Fifth line game3, fourth line game3 levels completed.
    # Once these save files are parsed, they can be used to update the load game display.




    def run(self):
        '''
            This function is called when the loadsGame module needs to be run/displayed.
            It is the function that displays all of the buttons and text.
            :return:
        '''
        #screen = pygame.display.set_mode((1280, 720))
        self.screen.fill(("beige"))
        pygame.display.set_caption('Load Game')

        self.save1Button.blit(self.save1Text, self.text_rect1)
        self.save2Button.blit(self.save2Text, self.text_rect2)
        self.save3Button.blit(self.save3Text, self.text_rect3)
        self.save4Button.blit(self.save4Text, self.text_rect4)
        #self.backButton.blit(self.backText, self.backRect)

        self.screen.blit(self.save1Button, (self.button1.x, self.button1.y))
        self.screen.blit(self.save2Button, (self.button2.x, self.button2.y))
        self.screen.blit(self.save3Button, (self.button3.x, self.button3.y))
        self.screen.blit(self.save4Button, (self.button4.x, self.button4.y))

        #self.screen.blit(self.backButton, (self.button5.x, self.button5.y))

        # Display Title
        self.screen.blit(self.load_title, (290, 40))
        #self.screen.blit(self.title_text, self.title_textRect)

        #disp backbutton
        self.screen.blit(self.backButton, (106, 45))

        # Draw Borders around buttons cause why not.
        pygame.draw.rect(self.screen, (96,96,96), self.button1, 10, 15)
        pygame.draw.rect(self.screen, (96,96,96), self.button2, 10, 15)
        pygame.draw.rect(self.screen, (96,96,96), self.button3, 10, 15)
        pygame.draw.rect(self.screen, (96,96,96), self.button4, 10, 15)

        pygame.display.update()

    def user_input(self, event):
        '''
            This is the event handler for the module.
            It receives events and responds to them accordingly.
        :param event: The Event that occurs.
        :return:
        '''
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # I'm sorry, there's no switch() function in python );
            if self.button1.collidepoint(pos):
                print("Save 1 Clicked")
                if (self.save1 == False): # Save 1 is empty/doesn't exist.
                    f = open("save1.txt", "x") # Create the file.
                    f.close()
                self.game.level_select = levelSelection(self.screen, self.game_state, "save1.txt", self.save1)
                self.game.states.update({'levelSelect':self.game.level_select})
                self.game.saveFile = "save1.txt"

                self.game_state.set_state('levelSelect')
                # Call on level select with the parameters from save 1.
                # levelSelection(self.screen, "save1.txt", self.save1)
            elif (self.button2.collidepoint(pos)):
                print("Save 2 Clicked")
                if (self.save2 == False): # Save 2 is empty/doesn't exist.
                    f = open("save2.txt", "x")
                    f.close()
                self.game.level_select = levelSelection(self.screen, self.game_state, "save2.txt", self.save2)
                self.game.states.update({'levelSelect': self.game.level_select})
                self.game.saveFile = "save2.txt"
                self.game_state.set_state('levelSelect')
                # Call on level select with the parameters from save 2.
            elif (self.button3.collidepoint(pos)):
                print("Save 3 Clicked")
                if (self.save3 == False): # Save 3 is empty/doesn't exist.
                    f = open("save3.txt", "x")
                    f.close()
                self.game.level_select = levelSelection(self.screen, self.game_state, "save3.txt", self.save3)
                self.game.states.update({'levelSelect': self.game.level_select})
                self.game.saveFile = "save3.txt"

                self.game_state.set_state('levelSelect')
                # Call on level select with the parameters from save 3.
            elif (self.button4.collidepoint(pos)):
                print("Save 4 Clicked")
                if (self.save4 == False): # Save 4 is empty/doesn't exist.
                    f = open("save4.txt", "x")
                    f.close()
                self.game.level_select = levelSelection(self.screen, self.game_state, "save4.txt", self.save4)
                self.game.states.update({'levelSelect': self.game.level_select})
                self.game.saveFile = "save4.txt"

                self.game_state.set_state('levelSelect')
                # Call on level select with the parameters from save 4.
            elif self.backButtonRect.collidepoint(pos):
                self.game_state.set_state('menu')
                # Call on main menu to return.



