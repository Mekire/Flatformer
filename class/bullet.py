from pygame.locals import *
import pygame
import os
import math
from pygame.transform import rotate


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, mpos):
        self.game = game
        self.mpos = mpos
        
        pygame.sprite.Sprite.__init__(self)
        

        self.image = pygame.image.load(os.path.join('images', 'bullet.png'))

        
        
        self.mouse_x, self.mouse_y = mpos
        self.player = self.game.player.rect.x, self.game.player.rect.y

        
        
        self.rect = self.image.get_rect()
    
        self.rect.topleft = (self.player)
 
        

        self.dy = 0
        self.dx = 0
        
    def getDegrees(self):
        
        ppos = self.player
        mpos = self.mpos
        try:
            degrees = math.degrees(math.atan((mpos[0] - ppos[0]) / (mpos[1] - ppos[1])))
        except ZeroDivisionError:
            degrees = 0
        if not degrees:
            if mpos[1] == ppos[1] or mpos[0] == ppos[0]:
                if mpos[0] > ppos[0]:
                    degrees = 90
                elif mpos[0] < ppos[0]:
                    degrees = 270
                elif mpos[1] > ppos[1]:
                    degrees = 180
                elif mpos[1] > ppos[1]:
                    degrees = 0

        elif mpos[0] > ppos[0] and mpos[1] < ppos[1]:
            degrees = abs(degrees)
        elif mpos[0] > ppos[0] and mpos[1] > ppos[1]:
            degrees = 90 - degrees + 90
        elif mpos[0] < ppos[0] and mpos[1] > ppos[1]:
            degrees = abs(degrees) + 180
        elif mpos[0] < ppos[0] and mpos[1] < ppos[1]:
            degrees = 90 - degrees + 270
        else:
            raise Exception('Incalculable degrees %s' % degrees)
        return int(360 - degrees)
    
    def update(self, dt):

        
        
        speed = -10.
        range = 200
        distance = [self.mouse_x - self.player[0], self.mouse_y - self.player[1]]
        norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / norm, distance[1 ] / norm]
        bullet_vector = [direction[0] * speed, direction[1] * speed]

        self.dx = bullet_vector[0]
        self.dy = bullet_vector[1]
        
        for block in self.game.block_list:
            if self.rect.colliderect(block):
                self.kill()
                
        for enemy in self.game.enemies_list:
            if self.rect.colliderect(enemy):
                self.kill()

        self.rect.x -= self.dx
        self.rect.y -= self.dy
