import pydoc
import unittest
# Save game is just a function that is run at the end of a level's completion.
# It must specify which game's level it just completed, as well as which level.
# It must also be passed the current save. Save is a string "save1.txt" or something.
# The Game is represented by a 1, 2, or 3, which are code for Color, Math, Animal.
# In the save file, the first line is color, second line math, 3rd line Animal.

def saveGame(save, game, levelCompleted):

    """
        Author: Ethan Lui
        Purpose: Save game function that is to be run at the end of a level, saving the user's progress without input from the user.

        Params:
            save(String), game(int), levelCompleted(int).
        Returns: Void, Writes to file save.
    """

    saveFile = open(save, "r")
    colorLevel = saveFile.readline().strip()
    mathLevel = saveFile.readline().strip()
    animalLevel = saveFile.readline().strip()
    saveFile.close()

    saveFile = open(save, "w")
    if (game == 1):
        if (levelCompleted < 3):
            saveFile.write(str(levelCompleted + 1) + "\n")
        else:
            saveFile.write(str(levelCompleted + 1) + "\n")
        saveFile.write(mathLevel+ "\n")
        saveFile.write(animalLevel+ "\n")

    elif(game == 2):
        saveFile.write(colorLevel + "\n")
        if (levelCompleted < 3):
            saveFile.write(str(levelCompleted + 1) + "\n")
        else:
            saveFile.write(str(levelCompleted + 1) + "\n")
        saveFile.write(animalLevel + "\n")

    elif (game == 3):
        saveFile.write(colorLevel + "\n")
        saveFile.write(mathLevel + "\n")
        if (levelCompleted < 3):
            saveFile.write(str(levelCompleted + 1) + "\n")
        else:
            saveFile.write(str(levelCompleted+ 1) + "\n")

    saveFile.close()


#pydoc.writedoc('saveGame')


