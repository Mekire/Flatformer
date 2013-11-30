from pygame.locals import *
import pygame
import sys

sys.path.append('class')

from player import Player
from block import Block
from maploader import MapLoader
from bullet import Bullet
pygame.init()

class Game():
    def __init__(self):
        #window setup
        pygame.display.set_caption('Game!')
        
        # Spite lists
        self.player_list = pygame.sprite.Group()
        self.enemies_list = pygame.sprite.Group()
        self.solid_blocks = pygame.sprite.Group()
        self.pass_blocks = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
    
        # initiate the clock and screen
        
        self.clock = pygame.time.Clock()
        self.last_tick = pygame.time.get_ticks()
        self.screen_res = [750, 550]
        self.center_point = [470., 350.]
        self.screen = pygame.display.set_mode(self.screen_res, pygame.HWSURFACE, 32)

        self.current_map = 1

        self.maploader = MapLoader(self)
        self.maploader.load(1)

        self.player = self.maploader.player

        #start loop
        while 1:
            self.Loop()

    def Loop(self):
        # main game loop
        self.eventLoop()
        
        self.Tick()
        self.Draw()
        pygame.display.update()

    def eventLoop(self):
        # the main event loop, detects keypresses
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                bullet = Bullet(self, pygame.mouse.get_pos())
                self.bullet_list.add(bullet)

    def Tick(self):
        
        self.ttime = self.clock.tick(45)
        self.keys_pressed = pygame.key.get_pressed()
        self.screen.blit(self.maploader.bg, (0,0))
        self.solid_blocks.draw(self.screen)
        self.pass_blocks.draw(self.screen)
        self.last_tick = pygame.time.get_ticks()

    def Draw(self):
        #update sprites
        self.bullet_list.update(self.ttime / 1000.)
        self.enemies_list.update()
        self.player_list.update(self.ttime / 1000.)
        #draw sprites
        self.bullet_list.draw(self.screen)
        self.enemies_list.draw(self.screen)
        self.player_list.draw(self.screen)

    def Reset(self):
        self.bullet_list.empty()
        self.enemies_list.empty()
        self.player_list.empty()
        self.solid_blocks.empty()
        self.pass_blocks.empty()
        self.maploader.load(self.current_map)
        self.player = self.maploader.player
        
Game()
