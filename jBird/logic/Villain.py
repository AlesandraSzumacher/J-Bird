import random


class Villain:
    def __init__(self, board):
        random_pos = random.randint(0, 2) % 2
        if random_pos == 0:
            tile_number = 1
        else:
            tile_number = 22

        self.position = list(board.listOfTiles[tile_number].center)

        self.level = 1

    def get_position(self):
        p = [self.position[0] - 30, self.position[1] - 45]
        return p

    def move_down(self, board):
        """Find move to down, rand left or right, check if possible and move"""
        possible_move_down = board.countTwoDownTiles(self.position)
        random_pos = random.randint(0, 2) % 2

        if board.if_tile_is_in_board(possible_move_down[random_pos]):
            self.set_position(possible_move_down[random_pos])
        elif board.if_tile_is_in_board(possible_move_down[(random_pos +1) % 2]):
            self.set_position(possible_move_down[(random_pos + 1) % 2])
        else:
            return True
        return False

    def set_position(self, pos):
        self.position[0] = pos[0]
        self.position[1] = pos[1]
