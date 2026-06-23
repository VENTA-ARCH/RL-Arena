from renderer import draw_board
import pygame

from renderer import draw_grid, draw_player, draw_board
from game import Game
from player import Player
from constants import (screen_width,screen_height,grid_width,grid_height,red,blue,fps,white,cell_size)

pygame.init()

background = pygame.image.load("melody.jpg")
background = pygame.transform.scale(background,(screen_width, screen_height))
player1_image = pygame.image.load("images.jpeg")
player2_image = pygame.image.load("Unknown.jpg")

player1_image = pygame.transform.scale(player1_image,(cell_size*2,cell_size*2))

player2_image = pygame.transform.scale(player2_image,(cell_size*2, cell_size*2))



font = pygame.font.Font(None, 72)
score_font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake Game")

game = Game(grid_width, grid_height)

player1 = Player((5, 5), (1, 0), red, 1)
player2 = Player((74, 74), (-1, 0), blue, 2)
player1.image = player1_image
player2.image = player2_image
game.add_player(player1)
game.add_player(player2)

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if game.game_over and event.key == pygame.K_r:
                game.reset()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player1.direction != (1, 0):
        player1.direction = (-1, 0)

    elif keys[pygame.K_DOWN] and player1.direction != (-1, 0):
        player1.direction = (1, 0)

    elif keys[pygame.K_LEFT] and player1.direction != (0, 1):
        player1.direction = (0, -1)

    elif keys[pygame.K_RIGHT] and player1.direction != (0, -1):
        player1.direction = (0, 1)



    if keys[pygame.K_w] and player2.direction != (1, 0):
        player2.direction = (-1, 0)

    elif keys[pygame.K_s] and player2.direction != (-1, 0):
        player2.direction = (1, 0)

    elif keys[pygame.K_a] and player2.direction != (0, 1):
        player2.direction = (0, -1)

    elif keys[pygame.K_d] and player2.direction != (0, -1):
       player2.direction = (0, 1)

    if not game.game_over:
        game.update()
        
    screen.blit(background, (0, 0))

    draw_grid(screen)

    score_text = score_font.render(f"P1: {player1.score}   P2: {player2.score}",True,white)

    screen.blit(score_text, (10, 10))
    draw_board(screen , game.grid)
    for player in game.players:
        
        draw_player(screen, player)

   

    if game.game_over:

        text = font.render(game.winner_text,True,white)

        text_rect = text.get_rect(center=(screen_width // 2,screen_height // 2))

        screen.blit(text, text_rect)

        restart_text = score_font.render("Press R to play again",True,white)

        restart_rect = restart_text.get_rect(center=(screen_width // 2,screen_height // 2 + 50))

        screen.blit(restart_text,restart_rect)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()