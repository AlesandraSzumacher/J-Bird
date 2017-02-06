import random


class Snake(object):
    """This class makes and moves snake"""
    def __init__(self, board):
        """Initializes new snake"""
        random_pos = random.randint(0, 2) % 2
        if random_pos == 0:
            tile_number = 1
        else:
            tile_number = 22

        self.position = list(board.list_of_tiles[tile_number].center)

        self.level = 1
        self.if_ball = True

    def get_position(self):
        """Count correct position of image"""
        p = [self.position[0] - 35, self.position[1] - 55]
        return p

    def move(self, board, chicken):
        """Moves snake, diffrent way when snake is in ball or not"""
        if_need_to_change_in_snake = False
        if self.if_ball:
            if_need_to_change_in_snake = self.move_down(board)

            if if_need_to_change_in_snake:
                self.if_ball = False
        else:
            self.move_in_chicken_side(chicken, board)

    def move_down(self, board):
        """Find move to down, rand left or right, check if possible and move."""
        possible_move_down = board.count_two_down_tiles(self.position)
        random_pos = random.randint(0, 2) % 2

        if board.if_tile_is_in_board(possible_move_down[random_pos]):
            self.set_position(possible_move_down[random_pos])
        elif board.if_tile_is_in_board(possible_move_down[(random_pos +1) % 2]):
            self.set_position(possible_move_down[(random_pos + 1) % 2])
        else:
            return True
        return False

    def set_position(self, pos):
        """Sets position of left down angle"""
        self.position[0] = pos[0]
        self.position[1] = pos[1]

    def move_in_chicken_side(self, chicken, board):
        """Snake follows chicken."""
        possible_move_down = board.count_two_down_tiles(self.position)
        possible_move_up = board.count_next_up_tiles(self.position)

        choose_move = None
        if chicken.tile_center[0] < self.position[0] and chicken.tile_center[1] > self.position[1]:
            choose_move = possible_move_down[0]
        elif chicken.tile_center[0] > self.position[0] and chicken.tile_center[1] > self.position[1]:
            choose_move = possible_move_down[1]
        elif chicken.tile_center[0] < self.position[0] and chicken.tile_center[1] < self.position[1]:
            choose_move = possible_move_up[0]
        elif chicken.tile_center[0] > self.position[0] and chicken.tile_center[1] < self.position[1]:
            choose_move = possible_move_up[1]

        if choose_move is not None:
            if board.if_tile_is_in_board(choose_move):
                self.set_position(choose_move)
        return choose_move

