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