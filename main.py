import pygame
import sys
import random
import food.py
import score.py

pygame.init()

class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [(Width/2), (Height/2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = green

    def get_head_positions(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1)  == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        current  self.get_head_position()
        x, y = self.direction
        new = (((cureent[0] + (x * Grid_Size)) % Width), (current[1] + (y * Grid_Size)) % Height)
        if len(self.positions) > 2 and new in self.position[2:]
        self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(Width/2), (Height/2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw (self, surface):
        for pos in self.positions:
            rect= pygame.Rect((pos[0], pos[1]), (Grid_Size, Grid_Size))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, black, rect, 3)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.Quit:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                if event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                if event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
                if event.key == pygame.K_LEFT:
                    self.turn(LEFT)

def drawGrid(surface):
    for y in range(0, int(Grid_Height)):
        for x in range(0, int(Grid_Width)):
            if ((x +y) % 2) == 0:
                rect = pygame.Rect((x * Grid_Size, y * Grid_Size), (Grid_Size, Grid_Size))
                pygame.draw.rect(surface, blue1, rect)
            else:
                rect = pygame.Rect((x * Grid_Size, y * Grid_Size), (Grid_Size, Grid_Size))
                pygame.draw.rect(surface, red2, rect)


#Game library variables
Width = 580
Height = 480
Grid_Size = 20
Grid_Width = Width / Grid_Size
Grid_Height = Height / Grid_Size
blue1 = (0, 0, 255)
red2 = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
orange = (255, 165, 0)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
font = pygame.font.Font('consola.ttf', 30)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Width, Height), 0, 32)

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
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))

        pygame.display.update()

main()