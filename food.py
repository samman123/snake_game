import pygame
import random
import config

class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = config.orange
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (
            random.randint(0, int(config.Grid_Width) - 1) * config.Grid_Size, 
            random.randint(0, int(config.Grid_Height) - 1) * config.Grid_Size
        )

    def draw(self, surface):
            rect= pygame.Rect((self.position[0], self.position[1]), (config.Grid_Size, config.Grid_Size))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, config.black, rect, 1)