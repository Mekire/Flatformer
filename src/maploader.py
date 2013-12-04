from pygame.locals import *
import pygame
import os

from block import Block
from enemy import Enemy
from player import Player

class MapLoader():
    def __init__(self, game):
        self.game = game

    def load(self, map_num):
        path = os.path.join("src","Maps","{}.map".format(map_num))
        with open(path) as f:
            map_txt =  f.read()

        self.bg =  pygame.image.load(os.path.join('images', 'bg','bg1.png'))
        self.bg.convert_alpha()


        col = 0
        row = 0
        for line in map_txt.split('\n'):
            for char in line:
                if char == 'P':
                    self.player = Player(self.game)
                    self.game.player_list.add(self.player)

                elif char == '1':
                    block = Block(self, [col, row], "1", 'solid')
                    self.game.solid_blocks.add(block)

                elif char == '2':
                    block = Block(self, [col, row], "2", 'solid')
                    self.game.solid_blocks.add(block)

                elif char == '3':
                    block = Block(self, [col, row], "3", 'switcher')
                    self.game.pass_blocks.add(block)

                elif char == '4':
                    block = Block(self, [col, row], "1", 'switcher')
                    self.game.pass_blocks.add(block)

                elif char == 'E':
                    enemy = Enemy(self.game, [col, row], "blockman")
                    self.game.enemies_list.add(enemy)

                elif char == '_': pass

                col += 25
            row += 25
            col = 0
        self.game.all_sprites.add(self.game.player_list,
                                  self.game.enemies_list,
                                  self.game.bullet_list)
        self.game.all_blocks.add(self.game.solid_blocks,self.game.pass_blocks)










