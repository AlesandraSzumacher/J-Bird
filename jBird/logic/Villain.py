import random


class Villain:
    def __init__(self, board):
        random_pos = random.randint(0, 2) % 2
        if random_pos == 0:
            tile_number = 1
        else:
            tile_number = 22

        self.position = board.listOfTiles[tile_number].center

        self.position[0] -= 30
        self.position[1] -= 45
        self.level = 1

    def get_position(self):
        return self.position
