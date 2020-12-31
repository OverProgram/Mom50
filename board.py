import pygame as pg


class Board:
    def __init__(self, board_file_name):
        self.image = pg.image.load(str(board_file_name))

    def get_player_locations(self):
        player_size = (10, 10)
        return [
            (187, 592),
            (354, 559),
            (258, 447),
            (264, 336),
            (370, 357),
            (480, 340),
            (595, 367),
            (640, 508),
            (438, 586),
            (510, 400)
        ]
