import pygame as pg

from board import Board
from clip_manager import ClipManager
from common import RESOURCE_FOLDER


def main():
    pg.init()
    pg.font.init()

    pg.display.set_caption('Happy 50th birthday')
    font = pg.font.SysFont('DejaVu Sans', 30)

    board = Board(RESOURCE_FOLDER / 'board.jpeg')
    player = pg.image.load(str(RESOURCE_FOLDER / 'pawn.jpeg'))
    clip_manager = ClipManager()
    player_locations = board.get_player_locations()

    screen = pg.display.set_mode(board.image.get_size())
    running = True
    turn = True
    player_loc = None

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    turn = True
                if event.key == pg.K_p:
                    clip_manager.play('levi')

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
