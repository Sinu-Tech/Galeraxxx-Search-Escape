from models import Enemy, Player
from views.pygame import *


if __name__ == "__main__":
    player = Player("Player", PLAYER_POS_X, PLAYER_POS_Y)
    enemy = Enemy("Enemy", ENEMY_POS_X, ENEMY_POS_Y)

    pygame_start_game(player, enemy)
