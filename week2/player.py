class Player:

    def __init__(self, start_pos, start_dir, color, player_id):

        self.position = start_pos
        self.direction = start_dir
        self.color = color
        self.start_position = start_pos
        self.start_direction = start_dir

        self.is_alive = True
        self.player_id = player_id
        self.score = 0

        self.trail = [start_pos]

    def reset(self):

        self.position = self.start_position
        self.direction = self.start_direction

        self.is_alive = True

        self.trail = [self.start_position]