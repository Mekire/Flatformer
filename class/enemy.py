from pygame.locals import *
import pygame
import os


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, pos, name):
        self.game = game
        
        pygame.sprite.Sprite.__init__(self)
        img_n = "%s.png" %name

        self.image = pygame.image.load(os.path.join('images', 'enemies', img_n))
        

        self.rect = self.image.get_rect()
        self.rect.topleft = (pos[0], pos[1])

        self.direction = 'left'

    def update(self):
        if self.direction == 'left':
            self.rect.x += 4
        elif self.direction == 'right':
            self.rect.x -= 4 

        for block in self.game.block_list:
            if self.rect.colliderect(block.rect) and block.block_type == 'switcher':
                if self.direction == 'left':
                    self.direction = 'right'

                elif self.direction == 'right':
                    self.direction = 'left'
                    
        

