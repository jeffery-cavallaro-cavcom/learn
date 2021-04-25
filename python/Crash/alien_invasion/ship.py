import pygame


class Ship:
    """ Out hero, the alien-zapping ship """
    def __init__(self, screen_rect):
        """ Initialize the ship in the mid bottom of the screen """
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = screen_rect.midbottom

    def blitme(self, screen):
        screen.blit(self.image, self.rect)
