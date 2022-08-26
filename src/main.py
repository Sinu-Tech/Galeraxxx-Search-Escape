from models import Enemy, Player
from utils.map_utils import *
from models.maps import *
import time
import pygame

if __name__ == "__main__":

    player_pos_x, player_pos_y = get_position(game_map, MAP_PLAYER)
    enemy_pos_x, enemy_pos_y = get_position(game_map, MAP_ENEMY)
    player_speed = 1.2
    enemy_speed = 1.0
    user = Player("Player", player_pos_x, player_pos_y, player_speed)
    enemy1 = Enemy("Enemy1", enemy_pos_x, enemy_pos_y, enemy_speed)

    print("player x:", player_pos_x,"player y:", player_pos_y)
    print("enemy x:",enemy_pos_x,"enemy y", enemy_pos_y)
    print(game_map)
    pygame.init()
    screen = pygame.display.set_mode((600, 400))    
    clock = pygame.time.Clock()

    path = enemy1.get_expansions(user.pos_x, user.pos_y)
    
    print("path:")
    print(path.x, path.y)
    while path is not None:
        path = path.expanded_by
        if path is not None:
            print(path.x, path.y)
    print_map_f(enemy1.map_bot)
    print_map_g(enemy1.map_bot)
    print_map_h(enemy1.map_bot)

    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:


                if  event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if user.pos_x - 1 >= 0 and game_map[user.pos_y][user.pos_x - 1] == 0:
                        game_map[user.pos_y][user.pos_x - 1] = 2
                        game_map[user.pos_y][user.pos_x] = 0
                        user.pos_x = user.pos_x - 1

                elif  event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if user.pos_x + 1 < len(game_map) and game_map[user.pos_y][user.pos_x+1] == 0:
                        game_map[user.pos_y][user.pos_x+1] = 2
                        game_map[user.pos_y][user.pos_x] = 0
                        user.pos_x = user.pos_x + 1

                elif  event.key == pygame.K_w or event.key == pygame.K_UP:
                    if user.pos_y - 1 >= 0 and game_map[user.pos_y-1][user.pos_x] == 0:
                        game_map[user.pos_y-1][user.pos_x] = 2
                        game_map[user.pos_y][user.pos_x] = 0
                        user.pos_y = user.pos_y - 1

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if user.pos_y + 1 < len(game_map) and game_map[user.pos_y+1][user.pos_x] == 0:
                        game_map[user.pos_y+1][user.pos_x] = 2
                        game_map[user.pos_y][user.pos_x] = 0
                        user.pos_y = user.pos_y + 1

                
                print(game_map)
            elif event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

