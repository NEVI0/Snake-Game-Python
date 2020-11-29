import pygame, random as rd

class Fruit:

    def __init__(self: object):

        self.__image = pygame.image.load('assets/fruit.png')
        self.__image.set_colorkey((255, 255, 255))
        self.__image = pygame.transform.scale(self.__image, (35, 35))

        self.__location: list = [rd.randint(0, 890), rd.randint(0, 490)]
        self.__sound = pygame.mixer.Sound('assets/sound.wav')

        self.__rect = pygame.Rect(
            self.__location[0],
            self.__location[1],
            self.__image.get_width(),
            self.__image.get_height()
        )

    @property
    def image(self: object) -> pygame.Surface:
        return self.__image

    @property
    def rect(self: object) -> pygame.Surface:
        return self.__rect

    @property
    def location(self: object) -> list:
        return self.__location

    def collision(self: object) -> None:
        self.__sound.play()
        self.__location = [rd.randint(0, 890), rd.randint(0, 490)]
        self.__rect = pygame.Rect(
            self.__location[0],
            self.__location[1],
            self.__image.get_width(),
            self.__image.get_height()
        )
