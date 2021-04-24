import sys

import pygame

from settings import Settings


class AlienInvasion:
    """ A game that strongly resembles the old Aliens arcade game """
    def __init__(self):
        """ All of the game settings """
        self.settings = Settings()

        """ Setup the game screen """
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.screen.fill(self.settings.bgcolor)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ Game main loop """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
