from typing import List


class Player:

    def __init__(self, current_players: List):
        """
        :param current_players: Players Currently Playing
        TODO: Find the average score of people currently playing. Make it into an int, and assign it to player
        TODO: Give a random uid to current player
        TODO: Give a random name to current player. Be fun.
        """
        self.score, self.uid, self.name = 0, None, None

    """DO NOT TOUCH!"""
    def update_name(self, name):
        pass

    """DO NOT TOUCH!"""
    def set_score(self, new_score):
        pass
