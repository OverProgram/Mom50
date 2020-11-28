import pygame as pg


def main():
    pg.init()
    pg.font.init()

    pg.display.set_caption('Happy 50th birthday')
    font = pg.font.SysFont('DejaVu Sans', 30)

    board = pg.image.load('board.jpeg')
    player = pg.image.load('pawn.jpeg')

    spaces_per_line = board.get_size()[0] / player.get_size()[0]

    screen = pg.display.set_mode(board.get_size())

    cube_results = [2, 1] * 18
    turn = 0
    space = 0

    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    turn += 1
                    space += cube_results[turn]

        player_loc = ((player.get_size()[0] * space) % board.get_size()[0],
                      player.get_size()[1] * (space // spaces_per_line))

        dice_roll = font.render('{}'.format(cube_results[turn]), False, (0, 0, 0))

        screen.fill((0, 0, 0))
        screen.blit(board, (0, 0))
        screen.blit(player, player_loc)
        screen.blit(dice_roll, (0, 0))
        pg.display.flip()


if __name__ == '__main__':
    main()
