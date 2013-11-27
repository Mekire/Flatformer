from pygame.locals import *
import pygame
import os




class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('images', 'player', 'left.png'))

        self.rect = self.image.get_rect()

        self.jumping = False

        self.rect.x = 200
        self.rect.y = 75

        self.dx = 0
        self.dy = 0
        
        self.gravity = 3
        self.moving = False
        self.jumping = False

        self.player_face = 'left'

        self.player_frames = {}
        for fi in os.listdir(os.path.join('images', 'player')):
            if fi.endswith('.png'):
                self.player_frames[fi] = pygame.image.load(os.path.join('images', 'player', fi)).convert_alpha()

    def checkCollision(self):
    
        if pygame.sprite.spritecollideany(self, self.game.block_list):
            
            return True

        else:
            return False

    def update(self, dt):
        last = self.rect.copy()
        if 1 in self.game.keys_pressed:
            
            if self.game.keys_pressed[K_d]:
                
                self.player_face = 'right'
                self.rect.x += 15 
                
            if self.game.keys_pressed[K_a]:
                
                self.player_face = 'left'
                self.rect.x += -15
                
            if not self.jumping and self.game.keys_pressed[K_w] and self.checkCollision():
                self.dy = -3
                self.jumping = True
                
        if self.jumping:
            self.dy -= 75
            print self.dy 
            self.rect.y += self.dy * dt
                
            if self.dy < -600:
                
                self.jumping = False

        if not self.checkCollision() and not self.jumping:
            if self.dy < 540:
                self.dy += 75
            else:
                self.dy += 0
            
            self.rect.y += self.dy * dt

        # detect if the player touches any of the blocks
        for block in self.game.block_list:
            if self.rect.colliderect(block):
            
                if self.rect.top <= block.rect.bottom and self.rect.top >= block.rect.top and self.checkCollision():
                    self.jumping = False
                    self.rect = last
                    
                if self.rect.bottom <= block.rect.top and self.rect.bottom >= block.rect.bottom and self.checkCollision():
                    self.jumping = False
                    self.rect = last

                if self.rect.right >= block.rect.left and self.rect.right <= block.rect.right and self.rect.bottom >= block.rect.bottom and self.rect.top <= block.rect.top and self.checkCollision():
                    self.rect.x -= 0
                    self.rect = last
                    

                if self.rect.left <= block.rect.right and self.rect.right >= block.rect.right and self.rect.bottom >= block.rect.bottom and self.rect.top <= block.rect.top and self.checkCollision():
                    self.rect.x += 0
                    self.rect = last
                    
                    
                


            
        
                
            
            
                

                     
            
                

           
        self.image = self.player_frames['%s.png' % (self.player_face)]
            
   
        
        
            
    
        
    
        
            
    
        
        
        
