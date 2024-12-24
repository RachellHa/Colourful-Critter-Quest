import pygame
import pydoc

class Tutorial:
    """
    Author: Lily So and Ethne Au
    This class is used to display the tutorial page. It contains the instructions for each game.
    """
    def __init__(self, screen, game_state):
        """
        This method initializes the tutorial page.
        :param screen: the screen to display the tutorial page
        :param game_state: the current state of the game
        """
        self.screen = screen
        self.game_state = game_state

        # load title
        self.tutorial_title = pygame.image.load(
            "assets/titles/tutorial.png").convert_alpha()
        self.backButton = pygame.image.load(
            "assets/levelPage/backButton.png").convert_alpha()

        # create button rect
        self.backButtonRect = pygame.Rect(106, 45, 70, 70)

    def run(self):
        """
        This method runs the tutorial page.
        """
        self.screen.fill('beige')
        pygame.display.set_caption('Tutorial')

        self.screen.blit(self.tutorial_title, (290, 40))

        # display back button
        self.screen.blit(self.backButton, (106, 45))

        font1 = pygame.font.SysFont("arialblack", 30)
        font2 = pygame.font.SysFont("arialblack", 20)

        # display instructions
        heading1 = "Animal Typing Safari"
        h1 = font1.render(heading1, True, "#313538")
        self.screen.blit(h1, (140, 150))
        animaleasymedium = "Easy/Medium: Pick and choose the name of the animal shown"
        a1 = font2.render(animaleasymedium, True, "#313538")
        self.screen.blit(a1, (140, 200))
        animalhard = "Hard: Type the name of the animal shown"
        a2 = font2.render(animalhard, True, "#313538")
        self.screen.blit(a2, (140, 230))

        heading2 = "Math Mania"
        h2 = font1.render(heading2, True, "#313538")
        self.screen.blit(h2, (140, 280))
        math = "Easy/Medium/Hard: Pick and choose the result of the given equation"
        m1 = font2.render(math, True, "#313538")
        self.screen.blit(m1, (140, 330))

        heading3 = "Rainbow Rumble"
        h3 = font1.render(heading3, True, "#313538")
        self.screen.blit(h3, (140, 380))
        coloureasy = "Easy: Pick and choose the name of the colour shown"
        c1 = font2.render(coloureasy, True, "#313538")
        self.screen.blit(c1, (140, 430))
        colourmed = "Medium: Drag and drop the resulting colour of mixing the two given colours"
        c2 = font2.render(colourmed, True, "#313538")
        self.screen.blit(c2, (140, 460))
        colourhard = "Hard: Type the name of the colour resulting from mixing the two given colours"
        c3 = font2.render(colourhard, True, "#313538")
        self.screen.blit(c3, (140, 490))

    def user_input(self, event):
        """
        This method handles the user input for the tutorial page.
        :param event: the event that the user inputs
        """
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.backButtonRect.collidepoint(pos):
                self.game_state.set_state('menu')
