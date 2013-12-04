from pygame.locals import *
import pygame
import os
import sys

from src.player import Player
from src.block import Block
from src.maploader import MapLoader
from src.bullet import Bullet
pygame.init()

CAPTION = "Game!"

class Game():
    def __init__(self):
        #window setup
        pygame.display.set_caption(CAPTION)
        os.environ["SDL_VIDEO_CENTERED"] = "True"
        self.fps = 60.0

        # Spite lists
        self.player_list = pygame.sprite.Group()
        self.enemies_list = pygame.sprite.Group()
        self.solid_blocks = pygame.sprite.Group()
        self.pass_blocks = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.OrderedUpdates()
        self.all_blocks = pygame.sprite.OrderedUpdates()

        # initiate the clock and screen

        self.clock = pygame.time.Clock()
        self.last_tick = pygame.time.get_ticks()
        self.screen_res = [750, 550]
        self.center_point = [470., 350.]
        self.screen = pygame.display.set_mode(self.screen_res,pygame.HWSURFACE)

        self.current_map = 1

        self.maploader = MapLoader(self)
        self.maploader.load(1)

        self.player = self.maploader.player

        #start loop
        self.clock.tick(self.fps)
        while 1:
            self.Loop()

    def Loop(self):
        # main game loop
        self.eventLoop()

        self.Tick()
        self.Draw()
        pygame.display.update()
        caption = "{} - FPS: {:.2f}".format(CAPTION,self.clock.get_fps())
        pygame.display.set_caption(caption)

    def eventLoop(self):
        # the main event loop, detects keypresses
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                bullet = Bullet(self, pygame.mouse.get_pos())
                self.bullet_list.add(bullet)
                self.all_sprites.add(bullet)
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    self.player.jump()

    def Tick(self):
        self.ttime = self.clock.tick(self.fps)
        self.keys_pressed = pygame.key.get_pressed()
        self.screen.blit(self.maploader.bg, (0,0))
        self.all_blocks.draw(self.screen)
        self.last_tick = pygame.time.get_ticks()

    def Draw(self):
        #update sprites
        delta = self.ttime / 1000.
        self.all_sprites.update(delta)
        self.all_sprites.draw(self.screen)

    def Reset(self):
        for sprite in self.all_sprites:
            sprite.kill()
        for sprite in self.all_blocks:
            sprite.kill()
        self.maploader.load(self.current_map)
        self.player = self.maploader.player

Game()
