import pygame
import pydoc

class AnimalDictEasy:
    """
    Author: Lily So
    This class is used to store the dictionary of easy animals and their corresponding images and sounds.
    """
    def __init__(self):
        """
        This method initializes the easy animals dictionary.
        """
        self.easy_animals = {
            "Cat": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/cat.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/catMeow.mp3")
            },
            "Dog": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/dog.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/dogBark.mp3")
            },
            "Bear": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/bear.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/bearSound.mp3")
            },
            "Horse": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/horse.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/horseSound.mp3")
            },
            "Chicken": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/chicken.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/chickenSound.mp3")
            },
            "Cow": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/cow.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/cowSound.mp3")
            },
            "Duck": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/duck.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/duckSound.mp3")
            },
            "Elephant": { 
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/elephant.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/elephantSound.mp3")
            },
            "Goat": { 
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/goat.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/goatSound.mp3") 
            },
            "Goose": { 
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/goose.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/gooseSound.mp3")
            },
            "Lion": { 
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/lion.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/lionSound.mp3")
            },
            "Monkey": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/monkey.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/monkeySound.mp3")
            },
            "Owl": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/owl.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/owlSound.mp3")
            },
            "Pig": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/pig.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/pigSound.mp3")
            },
            "Snake": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/snake.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/snakeSound.mp3")
            },
            "Mouse": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/mouse.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/mouseSound.mp3")
            },
            "Frog": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/frog.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/frogSound.mp3")
            },
            "Wolf": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/wolf.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/wolfSound.mp3")
            },
            "Turkey": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/turkey.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/turkeySound.mp3")
            },
            "Bat": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/bat.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/batSound.mp3")
            },
            "Tiger": {
                "image": pygame.transform.scale(pygame.image.load("assets/easyAnimals/tiger.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/easySounds/tigerSound.mp3")
            }

        }
