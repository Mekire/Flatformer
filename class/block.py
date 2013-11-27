from pygame.locals import *
import pygame
import os


class Block(pygame.sprite.Sprite):
    def __init__(self, game, pos, name):
        self.game = game
        
        pygame.sprite.Sprite.__init__(self)
        img_n = "block%s.png" %name

        self.image = pygame.image.load(os.path.join('images', 'blocks', img_n))
        

        self.rect = self.image.get_rect()
        self.rect.topleft = (pos[0], pos[1])
        
        
