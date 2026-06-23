import numpy as np


class Game:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.players = []
        self.grid = np.zeros((rows, cols), dtype=int)

        self.game_over = False
        self.winner_text = ""

    def add_player(self, player):
        self.players.append(player)

        row, col = player.position
        self.grid[row, col] = player.player_id

    def update(self):

        if self.game_over:
            return

        next_positions = {}


        for player in self.players:

            if not player.is_alive:
                continue

            row, col = player.position
            dr, dc = player.direction

            next_pos = (row + dr, col + dc)

            next_positions[player] = next_pos

        for player, next_pos in next_positions.items():

            row, col = next_pos

            if (row < 0 or row >= self.rows or col < 0 or col >= self.cols):
                player.is_alive = False
                continue

            if self.grid[row, col] != 0:
                player.is_alive = False
                continue

        
        positions = list(next_positions.values())

        for player, next_pos in next_positions.items():

            if not player.is_alive:
                continue

            if positions.count(next_pos) > 1:
                player.is_alive = False
                continue

            
            player.position = next_pos

         
            player.trail.append(next_pos)

          
            row, col = next_pos
            self.grid[row, col] = player.player_id

      
        alive_players = [player for player in self.players if player.is_alive]

        if len(alive_players) == 1:

            winner = alive_players[0]
            winner.score += 1

            self.game_over = True
            self.winner_text = (f"Player {winner.player_id} Wins!")

        elif len(alive_players) == 0:

            self.game_over = True
            self.winner_text = "Draw!"

    def reset(self):

        self.grid = np.zeros((self.rows, self.cols),dtype=int)

        for player in self.players:

            player.reset()

            row, col = player.position

            self.grid[row, col] = player.player_id

        self.game_over = False
        self.winner_text = ""