from models import Enemy, Player
from utils.map_utils import *
from models.maps import *
import time
import pygame
from math import radians
from tkinter import font

from pygame.locals import *
from sys import exit       #valores Fechar aplicação
from random import randint #valores randomicos


if __name__ == "__main__":
    # user = Player("Player", 0, 0, 1.2)
    # enemy1 = Enemy("Enemy1", 19, 19, 1.0)
    # pygame.init()
    # screen = pygame.display.set_mode((600, 400))    
    # clock = pygame.time.Clock()

    # path = enemy1.get_expansions(user.pos_x, user.pos_y)
    #
    # print("path:")
    # print(path.x, path.y)
    # while path is not None:
    #     path = path.expanded_by
    #     if path is not None:
    #         print(path.x, path.y)
    # print_map_f(enemy1.map_bot)
    # print_map_g(enemy1.map_bot)
    # print_map_h(enemy1.map_bot)
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if  event.key == pygame.K_a or event.key == pygame.K_LEFT:
    #                 if user.pos_x - 1 >= 0 and game_map[user.pos_y][user.pos_x - 1] == 0:
    #                     game_map[user.pos_y][user.pos_x - 1] = 2
    #                     game_map[user.pos_y][user.pos_x] = 0
    #                     user.pos_x = user.pos_x - 1

    #             elif  event.key == pygame.K_d or event.key == pygame.K_RIGHT:
    #                 if user.pos_x + 1 < len(game_map) and game_map[user.pos_y][user.pos_x+1] == 0:
    #                     game_map[user.pos_y][user.pos_x+1] = 2
    #                     game_map[user.pos_y][user.pos_x] = 0
    #                     user.pos_x = user.pos_x + 1

    #             elif  event.key == pygame.K_w or event.key == pygame.K_UP:
    #                 if user.pos_y - 1 >= 0 and game_map[user.pos_y-1][user.pos_x] == 0:
    #                     game_map[user.pos_y-1][user.pos_x] = 2
    #                     game_map[user.pos_y][user.pos_x] = 0
    #                     user.pos_y = user.pos_y - 1


    #             elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
    #                 if user.pos_y + 1 < len(game_map) and game_map[user.pos_y+1][user.pos_x] == 0:
    #                     game_map[user.pos_y+1][user.pos_x] = 2
    #                     game_map[user.pos_y][user.pos_x] = 0
    #                     user.pos_y = user.pos_y + 1
    #             print(game_map)
                
pygame.init()

lifes = 2
largura =  1280
altura = 720
x = largura/2 
y = altura/2
garelaxx = randint(100,1000) 
garelayy = randint(30, 600)
fonte =  pygame.font.SysFont('consolas', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Garelaxxx-IA')
clock = pygame.time.Clock()

while True:

    for i in map_2:
        for j in i:
            print(j, end= ' ')
        print()

    clock.tick(30)
    tela.fill((13, 34, 43))
    mensagem = f'Lifes: {lifes}'
    texto = fonte.render(mensagem, True, (255,255,255))
    # for i in 

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit() 
        if pygame.key.get_pressed()[K_a]:
            x -= 10
        if pygame.key.get_pressed()[K_d]:
            x += 10
        if pygame.key.get_pressed()[K_w]:
            y -= 10
        if pygame.key.get_pressed()[K_s]:
            y += 10

        if y > altura:
            y= 0

        if y < 0:
            y= 720

        if x > largura:
            x= 0

        if x < 0:
            x= 1280

        player = pygame.draw.rect(tela, (26, 196, 57), (x,y,40,50))

        garelax = pygame.draw.rect(tela, (255,0,0), (garelaxx,garelayy,40,50))

        if player.colliderect(garelax) and lifes > 0:
            garelaxx = randint(100,1000) 
            garelayy = randint(30, 600) 
            lifes -= 1
        
        tela.blit(texto,(1100,10))

        pygame.display.update()

                # [[2, 0, 0, 0, 0],
                #   [0, 1, 0, 1, 0],
                #   [0, 0, 0, 1, 1],
                #   [0, 1, 0, 1, 0],
                #   [1, 1, 0, 0, 3]]
