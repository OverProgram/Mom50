import pygame as pg
from pathlib import Path

from Board import Board

RESOURCE_FOLDER = Path(__file__).parent / "resources"


def main():
    pg.init()
    pg.font.init()

    pg.display.set_caption('Happy 50th birthday')
    font = pg.font.SysFont('DejaVu Sans', 30)

    board = Board(RESOURCE_FOLDER / 'board.jpeg')
    player = pg.image.load(str(RESOURCE_FOLDER / 'pawn.jpeg'))
    player_locations = board.get_player_locations()

    screen = pg.display.set_mode(board.image.get_size())
    running = True
    turn = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    turn = True

        if turn:
            if len(player_locations) == 0:
                running = False
            else:
                player_loc = player_locations.pop(0)
                turn = False

        screen.fill((0, 0, 0))
        screen.blit(board.image, (0, 0))
        screen.blit(player, player_loc)
        pg.display.flip()


if __name__ == '__main__':
    main()
