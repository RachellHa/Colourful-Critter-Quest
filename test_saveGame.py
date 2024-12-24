import pydoc
import unittest
from saveGame import saveGame

class testSaveGame(unittest.TestCase):
    '''
        Author: Ethan Lui
        Purpose: To test the saveGame function
    '''
    def test_save1(self):
        '''
            Tests opening a save file, altering the 1st line, and updates the level completion.
        :return:
        '''
        saveGame("testSave.txt", 1, 2)
        saveFile = open("testSave.txt", 'r')
        temp = saveFile.readline().strip()
        self.assertEqual(temp, "3")
        self.assertEqual(saveFile.readline().strip(), "1")
        self.assertEqual(saveFile.readline().strip(), "1")
        saveFile.close()
        saveFile = open("testSave.txt", "w")
        saveFile.write("1\n")
        saveFile.write("1\n")
        saveFile.write("1\n")
        saveFile.close()

    def test_save2(self):
        '''
            Tests opening a save file, altering the 2nd line, and updates the level completion.
        :return:
        '''
        saveGame("testSave.txt", 2, 3)
        saveFile = open("testSave.txt", 'r')
        self.assertEqual(saveFile.readline().strip(), "1")
        self.assertEqual(saveFile.readline().strip(), "4")
        self.assertEqual(saveFile.readline().strip(), "1")
        saveFile.close()
        saveFile = open("testSave.txt", "w")
        saveFile.write("1\n")
        saveFile.write("1\n")
        saveFile.write("1\n")
        saveFile.close()

    def test_save3(self):
        '''
            Tests opening a save file, altering the 3rd line, and updates the level completion.
        :return:
        '''
        saveGame("testSave.txt", 3, 1)
        saveFile = open("testSave.txt", 'r')
        self.assertEqual(saveFile.readline().strip(), "1")
        self.assertEqual(saveFile.readline().strip(), "1")
        self.assertEqual(saveFile.readline().strip(), "2")
        saveFile.close()
        saveFile = open("testSave.txt", "w")
        saveFile.write("1\n")
        saveFile.write("1\n")
        saveFile.write("1\n")
        saveFile.close()

'''
if __name__ == '__main__':
    unittest.main()
'''
pydoc.writedoc('test_saveGame')