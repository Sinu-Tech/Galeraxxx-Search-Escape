from models import Enemy, Player
from utils.map_utils import *
from models.maps import *
import keyboard

if __name__ == "__main__":

    user = Player("Player", 1, 1, 1.2)
    enemy1 = Enemy("Enemy1", 19, 19, 1.0)

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

    while True:
        print(game_map)
        pressedKey = keyboard.read_key()
        if pressedKey == "a":
            if game_map[user.pos_x - 1][user.pos_y] == 0:
                game_map[user.pos_x - 1][user.pos_y] = 3
                game_map[user.pos_x][user.pos_y] = 0
                user.pos_x = user.pos_x - 1

        elif pressedKey == "d":
            if game_map[user.pos_x + 1][user.pos_y + 1] == 0:
                game_map[user.pos_x + 1][user.pos_y + 1] = 3
                game_map[user.pos_x][user.pos_y] = 0
                user.pos_x = user.pos_x + 1

        elif pressedKey == "w":
            if game_map[user.pos_x ][user.pos_y - 1] == 0:
                game_map[user.pos_x][user.pos_y - 1] = 3
                game_map[user.pos_x][user.pos_y] = 0
                user.pos_y = user.pos_y - 1

        elif pressedKey == "s":
            if game_map[user.pos_x][user.pos_y + 1] == 0:
                game_map[user.pos_x][user.pos_y + 1] = 3
                game_map[user.pos_x][user.pos_y] = 0
                user.pos_y = user.pos_y + 1