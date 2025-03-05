import pygame
import sys
import random
from food import Food
import score
import config

pygame.init()

class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [(config.Width // 2, config.Height // 2)]
        self.direction = random.choice([config.UP, config.DOWN, config.LEFT, config.RIGHT])
        self.color = config.green

    def get_head_positions(self):
        if isinstance(self.positions[0], tuple):
            return self.positions[0]
        else:
            raise TypeError("Error: Expected a tuple but got an integer. Check positions list.")

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1)  == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        current = self.get_head_positions()
        x, y = self.direction
        new = (((current[0] + (x * config.Grid_Size)) % config.Width), (current[1] + (y * config.Grid_Size)) % config.Height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(config.Width/2), (config.Height/2)]
        self.direction = random.choice([config.UP, config.DOWN, config.LEFT, config.RIGHT])

    def draw (self, surface):
        for pos in self.positions:
            rect= pygame.Rect((pos[0], pos[1]), (config.Grid_Size, config.Grid_Size))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, config.black, rect, 3)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(config.UP)
                if event.key == pygame.K_DOWN:
                    self.turn(config.DOWN)
                if event.key == pygame.K_RIGHT:
                    self.turn(config.RIGHT)
                if event.key == pygame.K_LEFT:
                    self.turn(config.LEFT)

def drawGrid(surface):
    for y in range(0, int(config.Grid_Height)):
        for x in range(0, int(config.Grid_Width)):
            if ((x +y) % 2) == 0:
                rect = pygame.Rect((x * config.Grid_Size, y * config.Grid_Size), (config.Grid_Size, config.Grid_Size))
                pygame.draw.rect(surface, config.blue1, rect)
            else:
                rect = pygame.Rect((x * config.Grid_Size, y * config.Grid_Size), (config.Grid_Size, config.Grid_Size))
                pygame.draw.rect(surface, config.red2, rect)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((config.Width, config.Height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    drawGrid(surface)

    snake = Snake()
    food = Food()

    score = 0
    while True:
        clock.tick(5)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_positions() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))

        pygame.display.update()

main()