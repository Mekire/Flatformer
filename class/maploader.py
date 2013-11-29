from pygame.locals import *
import pygame

from block import Block
from enemy import Enemy
from player import Player

class MapLoader():
    def __init__(self, game):
        self.game = game
        
    def load(self, map_num):
        with open("class\Maps\%s.map" %str(map_num), 'r') as f:
            map_txt =  f.read()

            
        col = 0
        row = 0
        for line in map_txt.split('\n'):
            for char in line:
                if char == 'P':
                    self.player = Player(self.game)
                    self.game.player_list.add(self.player)
                    
                elif char == '1':
                    block = Block(self, [col, row], "1", 'solid')
                    self.game.block_list.add(block)
                    
                elif char == '2':
                    block = Block(self, [col, row], "2", 'solid')
                    self.game.block_list.add(block)
                    
                elif char == '3':
                    block = Block(self, [col, row], "3", 'switcher')
                    self.game.block_list.add(block)
                    
                elif char == '4':
                    block = Block(self, [col, row], "1", 'switcher')
                    self.game.block_list.add(block)
                    
                elif char == 'E':
                    enemy = Enemy(self.game, [col, row], "blockman")
                    self.game.enemies_list.add(enemy)
                    
                elif char == '_': pass

                col += 25
            row += 25
            col = 0


        
                
            
                    


        
        
