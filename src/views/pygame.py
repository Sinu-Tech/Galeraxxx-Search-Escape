import time
from utils.map_utils import *
from models.maps import *
import pygame
import sys


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


pygame.init()
screen = pygame.display.set_mode((WIDTH_POSITION, HEIGHT_POSITION))
pygame.display.set_caption('Garelaxxx-IA')
clock = pygame.time.Clock()
clock.tick(120)
screen.fill(COLOR_GREY)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load('./src/data/cristais.mp3')
pygame.mixer.music.play(-1)
click = pygame.mixer.Sound('./src/data/click.wav')

def render_screen():
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

def reset_game(player,enemy):
    game_map = get_map()
    print(game_map)
    PLAYER_POS_Y, PLAYER_POS_X = get_position(game_map, MAP_PLAYER)
    ENEMY_POS_X, ENEMY_POS_Y = get_position(game_map, MAP_ENEMY)
    player.pos_x = PLAYER_POS_X
    player.pos_y = PLAYER_POS_Y
    enemy.pos_x = ENEMY_POS_X
    enemy.pos_y = ENEMY_POS_Y
    pygame.display.update()
    pygame_start_game(player, enemy)


def exit_game():
    pygame.display.quit()
    pygame.quit()
    exit()


def game_over(player,enemy):
    width = screen.get_width()
    height = screen.get_height()

    text_font = pygame.font.SysFont('Corbel', 35)

    color_dark = (0, 0, 0)
    text_blue = (77,77,255)

    # desenhando o texto GAMEOVER
    text = text_font.render('Obrigado por jogar', True, text_blue)
    pygame.draw.rect(screen, color_dark, [width * 0.21, height * 0.04, 360, 48], border_radius=12)
    screen.blit(text, (width * 0.29, height * 0.05))  # sobrepondo o  texto ao botão

   


    pygame.display.update()
    while True:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                exit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # checando se foi clicado em restart
                if 13 <= mouse[0] <= 148 and 544 <= mouse[1] <= 568:
                    # implementar aqui a lógica para restart
                    print("Botao Restart")
                    reset_game(player, enemy)
                    

                # checando se foi clicando em quit
                if 457 <= mouse[0] <= 586 and 544 <= mouse[1] <= 568:
                    print("Botao Quit")
                    exit_game()

def enemy_decision(player,enemy):
    expansions = enemy.get_expansions(player.pos_x, player.pos_y)
    if expansions == None:
        exit()

    path = []
    if expansions != None:
        path.append((expansions.y, expansions.x))

    while expansions != None:
        expansions = expansions.expanded_by
        if expansions != None:
            path.append((expansions.y, expansions.x))
    
    game_map[enemy.pos_x][enemy.pos_y] = MAP_FREE
    decision = path[-2]
    enemy.pos_y = decision[1]
    enemy.pos_x = decision[0]

    game_map[decision[0]][decision[1]] = MAP_ENEMY


def pygame_start_game(player, enemy):

    render_screen()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                click.play() #efeito sonoro do click

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if player.pos_x - 1 >= 0 and game_map[player.pos_y][player.pos_x - 1] == MAP_FREE:
                        game_map[player.pos_y][player.pos_x - 1] = MAP_PLAYER
                        game_map[player.pos_y][player.pos_x] = MAP_FREE
                        player.move("left")

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if player.pos_x + 1 < len(game_map) and game_map[player.pos_y][player.pos_x + 1] == MAP_FREE:
                        game_map[player.pos_y][player.pos_x + 1] = MAP_PLAYER
                        game_map[player.pos_y][player.pos_x] = MAP_FREE
                        player.pos_x = player.pos_x + 1
                        player.move("rigth")

                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if player.pos_y - 1 >= 0 and game_map[player.pos_y - 1][player.pos_x] == MAP_FREE:
                        game_map[player.pos_y - 1][player.pos_x] = MAP_PLAYER
                        game_map[player.pos_y][player.pos_x] = MAP_FREE
                        player.move("up")

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if player.pos_y + 1 < len(game_map) and game_map[player.pos_y + 1][player.pos_x] == MAP_FREE:
                        game_map[player.pos_y + 1][player.pos_x] = MAP_PLAYER
                        game_map[player.pos_y][player.pos_x] = MAP_FREE
                        player.move("down")

                enemy_decision(player,enemy)
                render_screen()

                if player.pos_y == enemy.pos_x and player.pos_x == enemy.pos_y:
                    game_over(player, enemy)

            elif event.type == pygame.QUIT:
                exit_game()