from pygame.locals import *
import pygame

from block import Block

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
                
                if char == '1':
                    block = Block(self, [col, row], "1")
                    self.game.block_list.add(block)
                elif char == '2':
                    block = Block(self, [col, row], "2")
                    self.game.block_list.add(block)
                    
                elif char == '_': pass

                col += 25
            row += 25
            col = 0


        
                
            
                    


        
        
