from pygame import color
import pygame

from constants import (cell_size,screen_width,screen_height,gray)


def draw_grid(screen):

    for x in range(0, screen_width, cell_size):
        pygame.draw.line(screen,gray,(x, 0),(x, screen_height))

    for y in range(0, screen_height, cell_size):
        pygame.draw.line(screen,gray,(0, y),(screen_width, y))


def draw_player(screen, player):
    row, col = player.position

    x = col * cell_size
    y = row * cell_size

    screen.blit(player.image, (x, y))


def draw_trail(screen, player):

    r, g, b = player.color

    trail_color = (r // 2,g // 2,b // 2)

    for trail_pos in player.trail:

        row, col = trail_pos

        x = col * cell_size
        y = row * cell_size

        pygame.draw.rect(screen,trail_color,(x, y, cell_size, cell_size))

def draw_board(screen , grid):
    rows , cols = grid.shape
    for row in range(rows):
        for col in range(cols):
            cell = grid[row , col]
            if cell == 0:
                continue
            if cell == 1:
                color = (255,0,0)
            elif cell == 2:
                color = (0,0,255)
            elif cell == -1:
                color = (120 ,0,0)
            elif cell == -2:
                color = (0,0,120)
            else:
                continue
            x = col * cell_size
            y = row * cell_size

            pygame.draw.rect(screen,color,(x, y, cell_size, cell_size))

