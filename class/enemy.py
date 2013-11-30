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

        self.alive = True

        self.direction = 'left'
        self.stats = {}
        self.stats['hp'] = 10

    def update(self):
        
        if self.alive:
            if self.direction == 'left':
                self.rect.x += 4
            elif self.direction == 'right':
                self.rect.x -= 4 

            for block in self.game.pass_blocks:
                if self.rect.colliderect(block.rect) and block.block_type == 'switcher':
                    if self.direction == 'left':
                        self.direction = 'right'

                    elif self.direction == 'right':
                        self.direction = 'left'
                        
            for bullet in self.game.bullet_list:
                if self.rect.colliderect(bullet.rect):
                    self.stats['hp'] -= 2
                    
            if self.stats['hp'] <= 0:
                self.alive = False
        else:
            self.rect.y +=30
            if self.rect.y <= 550:
                self.kill()
                    
        

