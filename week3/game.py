import numpy as np
from capture import capture_territory


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

        size = 5

        r1 = max(0, row - size // 2)
        r2 = min(self.rows, row + size // 2 + 1)

        c1 = max(0, col - size // 2)
        c2 = min(self.cols, col + size // 2 + 1)

        self.grid[r1:r2, c1:c2] = player.player_id

    def update(self):

        if self.game_over:
            return

        next_positions = {}

        # -------------------------
        # Collision checks
        # -------------------------

        for player in self.players:

            if not player.is_alive:
                continue

            row, col = player.position
            dr, dc = player.direction

            next_pos = (row + dr, col + dc)

            row, col = next_pos

            # Wall = blocked
            if (
                row < 0
                or row >= self.rows
                or col < 0
                or col >= self.cols
            ):
                continue

            cell = self.grid[row, col]

            # Own trail = death
            if cell == -player.player_id:
                player.is_alive = False
                continue

            # Enemy trail = kill enemy
            if cell < 0 and cell != -player.player_id:

                for enemy in self.players:

                    if enemy.player_id == -cell:
                        enemy.is_alive = False

            # Enemy territory = blocked
            if cell > 0 and cell != player.player_id:
                continue

            next_positions[player] = next_pos

        # -------------------------
        # Head-on collisions
        # -------------------------

        positions = list(next_positions.values())

        for player, next_pos in next_positions.items():

            if not player.is_alive:
                continue

            if positions.count(next_pos) > 1:
                player.is_alive = False
                continue

            old_row, old_col = player.position

            player.position = next_pos

            new_row, new_col = player.position

            cell = self.grid[new_row, new_col]

            if cell == 0:

                player.outside = True

                self.grid[old_row, old_col] = -player.player_id

                player.trail.append((old_row, old_col))

            elif cell == player.player_id and player.outside:

                 print("CAPTURE CALLED")

                 capture_territory(self.grid, player.player_id)

                 player.trail.clear()

                 player.outside = False


        # -------------------------
        # Win condition
        # -------------------------

        alive_players = [
            player
            for player in self.players
            if player.is_alive
        ]

        if len(alive_players) == 1:

            winner = alive_players[0]

            winner.score += 1

            self.game_over = True

            self.winner_text = (
                f"Player {winner.player_id} Wins!"
            )

        elif len(alive_players) == 0:

            self.game_over = True

            self.winner_text = "Draw!"

    def reset(self):

        self.grid = np.zeros(
            (self.rows, self.cols),
            dtype=int
        )

        for player in self.players:

            player.reset()

            row, col = player.position

            size = 5

            r1 = max(0, row - size // 2)
            r2 = min(
                self.rows,
                row + size // 2 + 1
            )

            c1 = max(0, col - size // 2)
            c2 = min(
                self.cols,
                col + size // 2 + 1
            )

            self.grid[
                r1:r2,
                c1:c2
            ] = player.player_id

        self.game_over = False
        self.winner_text = ""