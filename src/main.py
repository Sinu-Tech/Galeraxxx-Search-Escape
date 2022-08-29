import time
from models import Enemy, Player
from utils.map_utils import *
from models.maps import *
import pygame
import sys


PLAYER_SPEED = 1.2
ENEMY_SPEED = 1.0
PLAYER_POS_Y, PLAYER_POS_X = get_position(game_map, MAP_PLAYER)
ENEMY_POS_X, ENEMY_POS_Y = get_position(game_map, MAP_ENEMY)

COLOR_GREY = (46, 46, 46)
COLOR_BLUE = (0, 200, 255)
COLOR_DARK_GREY = (169, 160, 181)
COLOR_GREEN = (144, 238, 144)
COLOR_RED = (255, 69, 0)
PIXEL_SIZE = 30
WIDTH_POSITION = len(game_map) * PIXEL_SIZE
HEIGHT_POSITION = len(game_map) * PIXEL_SIZE


def update_screen():
    for y in range(0, len(game_map)):
        for x in range(0, len(game_map)):
            pos_x = x * PIXEL_SIZE
            pos_y = y * PIXEL_SIZE
            if game_map[y][x] == MAP_PLAYER:
                pygame.draw.rect(screen, COLOR_GREEN,
                                 (pos_x, pos_y, PIXEL_SIZE, PIXEL_SIZE))
            elif game_map[y][x] == MAP_ENEMY:
                pygame.draw.rect(screen, COLOR_RED,
                                 (pos_x, pos_y, PIXEL_SIZE, PIXEL_SIZE))
            elif game_map[y][x] == MAP_WALL:
                pygame.draw.rect(screen, COLOR_BLUE,
                                 (pos_x, pos_y, PIXEL_SIZE, PIXEL_SIZE))
            elif game_map[y][x] == MAP_FREE:
                pygame.draw.rect(screen, COLOR_GREY,
                                 (pos_x, pos_y, PIXEL_SIZE, PIXEL_SIZE))

            pygame.display.update()


def game_over():
    width = screen.get_width()
    height = screen.get_height()

    # print("larg", width)
    # print("altura", height)

    text_font = pygame.font.SysFont('Corbel', 35)

    text_color = (255, 255, 255)
    text_red = (227, 38, 54)
    color_dark = (0, 0, 0)

    # desenhando o texto GAMEOVER
    text = text_font.render('GAME OVER', True, text_red)
    pygame.draw.rect(screen, color_dark, [width * 0.2, height * 0.05, 340, 30], border_radius=10)
    screen.blit(text, (width * 0.36, height * 0.055))  # sobrepondo o  texto ao botão

    text_font = pygame.font.SysFont('Corbel', 40)
    # desenhando o botão restart
    text = text_font.render('restart', True, text_color)
    pygame.draw.rect(screen, color_dark, [width * 0.02, height * 0.9, 140, 30], border_radius=10)
    screen.blit(text, (width * 0.02 + width * 0.04, height * 0.9))  # sobrepondo o  texto ao botão

    # desenhando o botão quit
    text = text_font.render('quit', True, text_color)
    pygame.draw.rect(screen, color_dark, [width * 0.75, height * 0.9, 140, 30], border_radius=10)
    screen.blit(text, (width * 0.75 + width * 0.07, height * 0.9))  # sobrepondo o  texto ao botão

    pygame.display.update()
    while True:
        for ev in pygame.event.get():
            mouse = pygame.mouse.get_pos()

            if ev.type == pygame.QUIT:
                # print("QUITANDOO")
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # checando se foi clicado em restart
                if 13 <= mouse[0] <= 148 and 544 <= mouse[1] <= 568:
                    print("Botao Restart")
                    # implementar aqui a lógica para restart
                    #
                    #
                    #

                # checando se foi clicando em quit
                if 457 <= mouse[0] <= 586 and 544 <= mouse[1] <= 568:
                    print("Botao Quit")
                    sys.exit()

def debug(path):
    expansions = []
    if path != None:
        expansions.append((path.y, path.x))

    while path != None:
        path = path.expanded_by
        if path != None:
            expansions.append((path.y, path.x))

    return expansions[-2]


if __name__ == "__main__":
    pygame.init()

    user = Player("Player", PLAYER_POS_X, PLAYER_POS_Y, PLAYER_SPEED)
    enemy1 = Enemy("Enemy1", ENEMY_POS_X, ENEMY_POS_Y, ENEMY_SPEED)

    screen = pygame.display.set_mode((WIDTH_POSITION, HEIGHT_POSITION))
    pygame.display.set_caption('Garelaxxx-IA')
    clock = pygame.time.Clock()
    clock.tick(120)
    screen.fill(COLOR_GREY)
    update_screen()

    #musica de fundo
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.load('./src/data/cristais.mp3')
    pygame.mixer.music.play(-1)
    
    #efeito sonoro do jogo
    click = pygame.mixer.Sound('./src/data/click.wav')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                click.play() #efeito sonoro do click

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if user.pos_x - 1 >= 0 and game_map[user.pos_y][user.pos_x - 1] == MAP_FREE:
                        game_map[user.pos_y][user.pos_x - 1] = MAP_PLAYER
                        game_map[user.pos_y][user.pos_x] = MAP_FREE
                        user.pos_x = user.pos_x - 1

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if user.pos_x + 1 < len(game_map) and game_map[user.pos_y][user.pos_x + 1] == MAP_FREE:
                        game_map[user.pos_y][user.pos_x + 1] = MAP_PLAYER
                        game_map[user.pos_y][user.pos_x] = MAP_FREE
                        user.pos_x = user.pos_x + 1

                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if user.pos_y - 1 >= 0 and game_map[user.pos_y - 1][user.pos_x] == MAP_FREE:
                        game_map[user.pos_y - 1][user.pos_x] = MAP_PLAYER
                        game_map[user.pos_y][user.pos_x] = MAP_FREE
                        user.pos_y = user.pos_y - 1

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if user.pos_y + 1 < len(game_map) and game_map[user.pos_y + 1][user.pos_x] == MAP_FREE:
                        game_map[user.pos_y + 1][user.pos_x] = MAP_PLAYER
                        game_map[user.pos_y][user.pos_x] = MAP_FREE
                        user.pos_y = user.pos_y + 1

                path = enemy1.get_expansions(user.pos_x, user.pos_y)
                game_map[enemy1.pos_x][enemy1.pos_y] = MAP_FREE
                temp = debug(path)
                enemy1.pos_y = temp[1]
                enemy1.pos_x = temp[0]
                game_map[temp[0]][temp[1]] = MAP_ENEMY

                update_screen()

                if user.pos_y == enemy1.pos_x and user.pos_x == enemy1.pos_y:
                    game_over()

            elif event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
