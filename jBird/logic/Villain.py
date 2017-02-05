import random


class Villain:
    def __init__(self, board):
        random_pos = random.randint(0, 2) % 2
        if random_pos == 0:
            tile_number = 1
        else:
            tile_number = 22

        self.position = []
        self.position.append(board.listOfTiles[tile_number].center[0])
        self.position.append(board.listOfTiles[tile_number].center[1])

        self.position[0] -= 30
        self.position[1] -= 45
        self.level = 1

    def get_position(self):
        return self.position

    def move_down(self, board):
        """Allows to move the chicken down - left or right."""
        possible_move_down = board.countTwoDownTiles(self.position)
        random_pos = random.randint(0, 2) % 2
        choose_move = possible_move_down[random_pos]

        if board.if_tile_is_in_board(choose_move):
            self.set_position(choose_move)
        else:
            self.position = [0, 0]

        return choose_move

    def set_position(self, pos):
        self.position[0] = pos[0] - 30
        self.position[1] = pos[1] - 45

