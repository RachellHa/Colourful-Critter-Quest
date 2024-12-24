Colourful Critter Quest is an educational children's game that teaches kids targeted towards ages 2-10 to recognize
 and spell animals, basic colour theory, and do simple mathematical calculations. Through a combination of
 entertainment and education. Each of the three topic modules includes at least three different levels: the lowest
 levels contain multiple choice questions, while the higher level questions require users to spell and type out the
 answers. fter each game session, users can save the levels they have already completed. Allowing users to progress 
 throughout the game, reviewing words, calculations, and colour theories they have already learned while learning new 
 concepts.

This game is built in Python on Visual Studio Code 1.87.2 with the pygame extension, managed and sotred in a Bitbucket repository. 
Built in functions imported into this game include random, saveGame, sys, pydoc and unittest.

To download Python, visit https://www.python.org/downloads and download the latest version available in your operatng system 
(Windows 10 or 11)
Next, download an IDE to code on that supports Python. In this case, download VSCode by visiting https://code.visualstudio.com/download
and downloading the version for Windows 10, 11.
After VSCode has been downloaded, open up the app. Visit the extensions page and install Python with the Microsoft verified domain, as 
as Pygame Snippets v0.0.1 published by Taiwo Kareem.

Getting started to develope the game, create a page for each class of the game: this includes menu, savegame, highscore, and the three 
modules (math, colour and animal), including the three different levels of each module (easy, medium and hard). Starting with the 
development of the modules, draw out the screen with size (1280, 720), colour 'beige' and caption with the module names 
Math module = "Math Mania"
Colour module = "Rainbow Rumble"
Animal module = "Animal Typing Safari"

Following that, draw rectangles and import images to where items belong. We have all the images and buttons stored under assets. For guideline, the rectangle colour question found in rainbow rumble 
is (left right x-axis 160, top down y-axis 120, width 410, height 510). And render words for the questions in the level class. For guideline, 
the question asked in easy level of Rainbow Rumble is "What colour is this?" in black, placed (140, 20).
After setting up all the page screens, create functions that collect user input as well as mouse button recognition. As well as the functionality
of the game: items of questions and answers, correct and wrong answers, and have the computer detect what a mouse button wants to do. Did it select
or type in a wrong answer? Then set up a scoring data structure that saves all the scores users have collected in level of the games, which should be 
saved for the next time a user visits the game. Once all this is set up, import the pages together to work as a whole game. Allowing users to start 
from the main menu, to visiting other pages such as saved games, high score, and playing the game levels.

To run this software, clone the system using ssh://git@repo.csd.uwo.ca:7999/compsci2212_w2024/group77.git repository into a working IDE with a Pygame extension.
After, you may run to visit the menu page of the game.

To start a game, visit load games. You may then choose one of the three modules and start with level one. Everytime you play, scores will change and 
be saved in your saved. Next time you want to visit the saved game, visit "Load game" and to start a new game visit "New Game".