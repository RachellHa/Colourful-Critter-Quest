import pygame
import pydoc

class AnimalDictMed:
    """
    Author: Lily So
    This class is used to store the medium level animals and their corresponding images and sounds.
    """
    def __init__(self):
        """
        This method initializes the medium level animals dictionary.
        """
        self.med_animals = {
            "Alpaca": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/alpaca.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/alpaca.mp3")
            },
            "Buffalo": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/buffalo.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/buffalo.mp3")
            },
            "Chameleon": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/chameleon.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/chameleon.mp3")
            },
            "Cheetah": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/cheetah.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/cheetah.mp3")
            },
            "Chipmunk": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/chipmunk.jpeg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/chipmunk.mp3")
            },
            "Coyote": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/coyote.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/coyote.mp3")
            },
            "Donkey": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/donkey.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/donkey.mp3")
            },
            "Ferret": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/ferret.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/ferret.mp3")
            },
            "Flamingo": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/flamingo.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/flamingo.mp3")
            },
            "Hedgehog": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/hedgehog.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/hedgehog.mp3")
            },
            "Kangaroo": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/kangaroo.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/kangaroo.mp3")
            },
            "Leopard": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/leopard.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/leopard.mp3")
            },
            "Lynx": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/lynx.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/lynx.mp3")
            },
            "Otter": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/otter.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/otter.mp3")
            },
            "Woodpecker": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/woodpecker.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/woodpecker.mp3")
            },
            "Yak": {
                "image": pygame.transform.scale(pygame.image.load("assets/medAnimals/yak.jpg").convert(), (465,522)),
                "sound": pygame.mixer.Sound("assets/medSounds/yak.mp3")
            }

        }
