class Player:

    def __init__(self, start_pos, start_dir, color, player_id):

        self.position = start_pos
        self.direction = start_dir
        self.color = color
        self.start_position = start_pos
        self.start_direction = start_dir

        self.player_id = player_id
        self.score = 0
        self.is_alive = True
        self.trail = []
        self.outside = False

    def reset(self):

        self.position = self.start_position
        self.direction = self.start_direction

        self.is_alive = True
        self.outside = False
        self.trail = []