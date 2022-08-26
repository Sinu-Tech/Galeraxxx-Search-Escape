from models import Enemy, Player
from utils.map_utils import *
from models.maps import *
import pygame

from pygame.locals import *


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

    PIXEL_SIZE = 30
    largura = len(game_map)*PIXEL_SIZE
    altura = len(game_map)*PIXEL_SIZE
    COLOR_GREY = (46, 46, 46)
    COLOR_BLUE = (169, 160, 181)
    COLOR_GREEN = (144, 238, 144)
    COLOR_RED = (255, 69, 0)

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Garelaxxx-IA')
    clock = pygame.time.Clock()

    while True:

        # clock.tick(30)
        tela.fill((13, 34, 43))
        # for i in

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # if pygame.key.get_pressed()[K_a]:
            #     x -= 10
            # if pygame.key.get_pressed()[K_d]:
            #     x += 10
            # if pygame.key.get_pressed()[K_w]:
            #     y -= 10
            # if pygame.key.get_pressed()[K_s]:
            #     y += 10

            # if y > altura:
            #     y = 0

            # if y < 0:
            #     y = 720

            # if x > largura:
            #     x = 0

            # if x < 0:
            #     x = 1280

            alt = PIXEL_SIZE
            larg = PIXEL_SIZE
            for y in range(0, len(game_map)): 
                for x in range(0, len(game_map)):
                    pos_x = x*larg
                    pos_y = y*alt
                    if(game_map[y][x] == 2):
                        pygame.draw.rect(tela, COLOR_GREEN, (pos_x, pos_y, larg, alt))
                    elif (game_map[y][x] == 3):
                        pygame.draw.rect(tela, COLOR_RED, (pos_x, pos_y, larg, alt))
                    elif (game_map[y][x] == 1):
                        pygame.draw.rect(tela, COLOR_BLUE, (pos_x, pos_y, larg, alt))
                    elif (game_map[y][x] == 0):
                        pygame.draw.rect(tela, COLOR_GREY, (pos_x, pos_y, larg, alt))

            # player = pygame.draw.rect(tela, (26, 196, 57), (0, 0, 40, PIXEL_SIZE))
            # player = pygame.draw.rect(tela, (255, 0, 0), (0, PIXEL_SIZE, 40, PIXEL_SIZE))

            # garelax = pygame.draw.rect(
            #     tela, (255, 0, 0), (garelaxx, garelayy, 40, PIXEL_SIZE))

            # if player.colliderect(garelax) and lifes > 0:
            #     garelaxx = randint(100, 1000)
            #     garelayy = randint(30, 600)
            #     lifes -= 1

            # tela.blit(texto, (1100, 10))

            pygame.display.update()

            # [[2, 0, 0, 0, 0],
            #   [0, 1, 0, 1, 0],
            #   [0, 0, 0, 1, 1],
            #   [0, 1, 0, 1, 0],
            #   [1, 1, 0, 0, 3]]

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
                

    
