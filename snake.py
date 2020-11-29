# Imports
import pygame, random as rd

class Snake:

    def __init__(self: object) -> None:
        self.__speed: int = 5
        self.__location: list = [rd.randint(0, 750), rd.randint(0, 490), 25, 25]
        self.__control_location: list = [self.__speed, 0]
        self.__body: list = []
        self.__head: list = [self.__location[0], self.__location[1]]
        self.__length: int = 5

    @property
    def location(self: object) -> list:
        return self.__location

    @property
    def body(self: object) -> list:
        return self.__body

    def move_right(self: object) -> None:
        if self.__control_location[0] == -self.__speed:
            pass
        else:
            self.__control_location[0] = self.__speed
            self.__control_location[1] = 0

    def move_left(self: object) -> None:
        if self.__control_location[0] == self.__speed:
            pass
        else:
            self.__control_location[0] = -self.__speed
            self.__control_location[1] = 0

    def move_up(self: object) -> None:
        if self.__control_location[1] == self.__speed:
            pass
        else:
            self.__control_location[0] = 0
            self.__control_location[1] = -self.__speed

    def move_down(self: object) -> None:
        if self.__control_location[1] == -self.__speed:
            pass
        else:
            self.__control_location[0] = 0
            self.__control_location[1] = self.__speed

    def collision(self: object) -> bool:
        if self.__body.count(self.__head) > 1:
            return True
        else:
            return False

    def update_location(self: object) -> None:
        self.__location[0] += self.__control_location[0]
        self.__location[1] += self.__control_location[1]

    def update_length(self: object) -> None:
        self.__length += 5

    def update_body_head(self: object) -> None:
        self.__head = [self.__location[0], self.__location[1]]
        self.__body.append(self.__head)

    def update(self: object, window_size: tuple, game_screen: pygame.Surface) -> None:
        if self.__location[0] > window_size[0]:
            self.__location[0] = 0
        if self.__location[0] < 0:
            self.__location[0] = window_size[0]

        if self.__location[1] < 0:
            self.__location[1] = window_size[1]
        if self.__location[1] > window_size[1]:
            self.__location[1] = 0

        if len(self.__body) > self.__length:
            del self.__body[0]

        for position in self.__body:
            pygame.draw.rect(game_screen, (0, 0, 255), (position[0], position[1], 30, 30))