import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """ A game that strongly resembles the old Aliens arcade game """
    def __init__(self):
        """ All of the game settings """
        self.settings = Settings()

        """ Setup the game screen """
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.rect = self.screen.get_rect()
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self.rect)

    def run_game(self):
        """ Game main loop """
        while True:
            self.__check_events()
            self.__update_screen()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def __update_screen(self):
        self.screen.fill(self.settings.bgcolor)
        self.ship.blitme(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
