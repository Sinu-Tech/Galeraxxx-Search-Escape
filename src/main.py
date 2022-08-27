from models import Enemy, Player
from utils.map_utils import *
from models.maps import *
import pygame


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
WIDTH_POSITION = len(game_map)*PIXEL_SIZE
HEIGHT_POSITION = len(game_map)*PIXEL_SIZE


def update_screen():
    for y in range(0, len(game_map)):
        for x in range(0, len(game_map)):
            pos_x = x*PIXEL_SIZE
            pos_y = y*PIXEL_SIZE
            if (game_map[y][x] == MAP_PLAYER):
                pygame.draw.rect(screen, COLOR_GREEN,
                                 (pos_x, pos_y, PIXEL_SIZE, PIXEL_SIZE))
            elif (game_map[y][x] == MAP_ENEMY):
                pygame.draw.rect(screen, COLOR_RED,
                                 (pos_x, pos_y, PIXEL_SIZE, PIXEL_SIZE))
            elif (game_map[y][x] == MAP_WALL):
                pygame.draw.rect(screen, COLOR_BLUE,
                                 (pos_x, pos_y, PIXEL_SIZE, PIXEL_SIZE))
            elif (game_map[y][x] == MAP_FREE):
                pygame.draw.rect(screen, COLOR_GREY,
                                 (pos_x, pos_y, PIXEL_SIZE, PIXEL_SIZE))

            pygame.display.update()


def debug(path, enemy):
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

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if user.pos_x - 1 >= 0 and game_map[user.pos_y][user.pos_x - 1] == MAP_FREE:
                        game_map[user.pos_y][user.pos_x - 1] = MAP_PLAYER
                        game_map[user.pos_y][user.pos_x] = MAP_FREE
                        user.pos_x = user.pos_x - 1

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if user.pos_x + 1 < len(game_map) and game_map[user.pos_y][user.pos_x+1] == MAP_FREE:
                        game_map[user.pos_y][user.pos_x + 1] = MAP_PLAYER
                        game_map[user.pos_y][user.pos_x] = MAP_FREE
                        user.pos_x = user.pos_x + 1

                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if user.pos_y - 1 >= 0 and game_map[user.pos_y-1][user.pos_x] == MAP_FREE:
                        game_map[user.pos_y-1][user.pos_x] = MAP_PLAYER
                        game_map[user.pos_y][user.pos_x] = MAP_FREE
                        user.pos_y = user.pos_y - 1

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if user.pos_y + 1 < len(game_map) and game_map[user.pos_y+1][user.pos_x] == MAP_FREE:
                        game_map[user.pos_y+1][user.pos_x] = MAP_PLAYER
                        game_map[user.pos_y][user.pos_x] = MAP_FREE
                        user.pos_y = user.pos_y + 1

                path = enemy1.get_expansions(user.pos_x, user.pos_y)
                game_map[enemy1.pos_x][enemy1.pos_y] = MAP_FREE
                temp = debug(path,enemy1)
                enemy1.pos_y = temp[1]
                enemy1.pos_x = temp[0]
                game_map[temp[0]][temp[1]] = MAP_ENEMY

                update_screen()

            elif event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

