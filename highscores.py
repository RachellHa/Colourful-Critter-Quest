import pygame
import pydoc

class createText:
    '''
        Author: Ethan Lui
        Purpose: Simplify the create of text objects to display in pygame.
    '''
    def __init__(self, font, text, color1, color2, xcenter, yTop):
        self.text = font.render(text, True, color1, color2)
        self.text_Rect = self.text.get_rect()
        self.text_Rect.center = (xcenter, yTop)


class Highscores:
    '''
        Authors: Ethan Lui, Lily So
        Purpose: To create and display the highscores screen.
    '''
    def __init__(self, screen, game_state):
        '''
            The Method/Function that is run on object generation.
            Creates and initializes objects.
        :param screen: The screen that is being used/updated.
        :param game_state: The state of the game.
        '''
        self.screen = screen
        self.game_state = game_state
        self.font = pygame.font.SysFont("arial", 30)
        #load title
        self.scores_title = pygame.image.load("assets/titles/highscores.png").convert_alpha()
        self.backButton = pygame.image.load("assets/levelPage/backButton.png").convert_alpha()
    
        #create button rect
        self.backButtonRect = pygame.Rect(106, 45, 70, 70)

        self.save1Empty = False
        self.save2Empty = False
        self.save3Empty = False
        self.save4Empty = False
        self.save1Score = 0
        self.save2Score = 0
        self.save3Score = 0
        self.save4Score = 0


        try:
            save1 = open("save1.txt", 'r')
            for i in range(3):
                temp = int(save1.readline().strip())
                if temp == 2:
                    self.save1Score = self.save1Score + 100
                elif temp == 3:
                    self.save1Score = self.save1Score + 300
                elif temp == 4:
                    self.save1Score = self.save1Score + 600
            save1.close()

        except FileNotFoundError:
            self.save1Empty = True
        try:
            save2 = open("save2.txt", 'r')
            for i in range(3):
                temp = int(save2.readline().strip())
                if temp == 2:
                    self.save2Score = self.save2Score + 100
                elif temp == 3:
                    self.save2Score = self.save2Score + 300
                elif temp == 4:
                    self.save2Score = self.save2Score + 600
            save2.close()
        except FileNotFoundError:
            self.save2Empty = True

        try:
            save3 = open("save3.txt", 'r')
            for i in range(3):
                temp = int(save3.readline().strip())
                if temp == 2:
                    self.save3Score = self.save3Score + 100
                elif temp == 3:
                    self.save3Score = self.save3Score + 300
                elif temp == 4:
                    self.save3Score = self.save3Score + 600
            save3.close()
        except FileNotFoundError:
            self.save3Empty = True

        try:
            save4 = open("save4.txt", 'r')
            for i in range(3):
                temp = int(save4.readline().strip())
                if temp == 2:
                    self.save4Score = self.save4Score + 100
                elif temp == 3:
                    self.save4Score = self.save4Score + 300
                elif temp == 4:
                    self.save4Score = self.save4Score + 600
            save4.close()
        except FileNotFoundError:
            self.save4Empty = True

        # Now we have all the scores, or lack thereof with save1Empty or not.
        # createText(font, text, color1, color2, xcenter, yTop)
        #self.title = createText(self.font, "High Scores", (0, 0, 0), (203, 236, 164), 1280 / 2, 100)
        empty = "Empty"

        if (self.save1Empty):
            self.slot1 = createText(self.font, empty, (0, 0, 0), (203, 236, 164), 1280 / 2, 200)
        else:
            self.slot1 = createText(self.font, "Save 1: " + str(self.save1Score), (0, 0, 0), (203, 236, 164), 1280 / 2,
                                    200)

        if (self.save2Empty):
            self.slot2 = createText(self.font, empty, (0, 0, 0), (203, 236, 164), 1280 / 2, 300)
        else:
            self.slot2 = createText(self.font, "Save 2: " + str(self.save2Score), (0, 0, 0), (203, 236, 164), 1280 / 2,
                                    300)

        if (self.save3Empty):
            self.slot3 = createText(self.font, empty, (0, 0, 0), (203, 236, 164), 1280 / 2, 400)
        else:
            self.slot3 = createText(self.font, "Save 3: " + str(self.save3Score), (0, 0, 0), (203, 236, 164), 1280 / 2,
                                    400)

        if (self.save4Empty):
            self.slot4 = createText(self.font, empty, (0, 0, 0), (203, 236, 164), 1280 / 2, 500)
        else:
            self.slot4 = createText(self.font, "Save 4: " + str(self.save4Score), (0, 0, 0), (203, 236, 164), 1280 / 2,
                                    500)

    def run(self):
        '''
            This function is used for displaying all of the highscores objects that were created
            during object generation.
        :return:
        '''
        self.screen.fill('beige')
        pygame.display.set_caption('High Scores')

        self.screen.blit(self.scores_title, (290, 40))

        #display back button
        self.screen.blit(self.backButton, (106, 45))

        #Displaying highscores.

        self.screen.blit(self.slot1.text, self.slot1.text_Rect)
        self.screen.blit(self.slot2.text, self.slot2.text_Rect)
        self.screen.blit(self.slot3.text, self.slot3.text_Rect)
        self.screen.blit(self.slot4.text, self.slot4.text_Rect)

        pygame.display.update()





    def user_input(self, event):
        '''
            This function is used to handle user input.
        :param event: The event that is being passed and that will be handled.
        :return: None, Void.
        '''
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.backButtonRect.collidepoint(pos):
                self.game_state.set_state('menu')

#Testing
#pydoc.writedoc('highscores')
'''
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))
hs = Highscores(screen, 'Highscore')
while True:
    clock.tick(60)
    hs.run()
'''
