from pygame.locals import *
import pygame
import os


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, pos, name):
        self.game = game

        pygame.sprite.Sprite.__init__(self)
        img_n = "%s.png" %name

        self.image = pygame.image.load(os.path.join('images', 'enemies', img_n))
        self.image.convert()

        self.rect = self.image.get_rect(topleft=pos)
        self.true_location = list(self.rect.topleft)
        self.alive = True

        self.direction = 'left'
        self.stats = {}
        self.stats['hp'] = 10
        self.speed = 180

    def update(self,dt):

        if self.alive:
            if self.direction == 'right':
                self.true_location[0] += self.speed*dt
            elif self.direction == 'left':
                self.true_location[0] -= self.speed*dt
            self.rect.topleft = self.true_location

            for block in self.game.pass_blocks:
                if self.rect.colliderect(block.rect) and block.block_type == 'switcher':
                    if self.direction == 'left':
                        self.direction = 'right'
                        self.rect.left = block.rect.right

                    elif self.direction == 'right':
                        self.direction = 'left'
                        self.rect.right = block.rect.left
                    self.true_location = list(self.rect.topleft)

            for bullet in self.game.bullet_list:
                if self.rect.colliderect(bullet.rect):
                    self.stats['hp'] -= 2

            if self.stats['hp'] <= 0:
                self.alive = False
        else:
            self.rect.y += 800*dt
            if self.rect.y >= 550:
                self.kill()



