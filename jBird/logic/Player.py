from jBird.utils.Constants import PlayerPos


class Player(object):
    """Class containing methods and attributes referring to current player."""

    def __init__(self, nick):
        """Player initialize."""
        self.nick = nick
        self.hp = 2
        self.points = 0
        self.width = PlayerPos.START_WIDTH.value
        self.height = PlayerPos.START_HEIGHT.value

    def add_points(self, points=10):
        """Adding player's health points."""
        self.points += points

    def add_hp(self):
        """Adding player's health points."""
        self.hp += 1

    def sub_hp(self):
        """Subtracting player's health points."""
        self.hp -= 1

    def did_i_lose(self):
        """Checking if player lost."""
        if self.hp < 0:
            return True
        return False
