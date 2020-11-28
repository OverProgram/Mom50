import pygame as pg


class Board:
    def __init__(self, board_file_name):
        self.image = pg.image.load(str(board_file_name))

    def get_player_locations(self):
        player_size = (10, 10)
        spaces_per_line = self.image.get_size()[0] / player_size[0]
        return [
            ((player_size[0] * space) % self.image.get_size()[0],
             player_size[1] * (space // spaces_per_line))
            for space in range(10)
        ]
