from models import Enemy, Player
from utils.map_utils import *
from models.maps import *
if __name__ == "__main__":

    user = Player("Player", 4, 4, 1.2)
    enemy1 = Enemy("Enemy1", 0, 0, 1.0)

    path = enemy1.get_expansions(user.pos_x, user.pos_y)

    print("path:")
    print(path.x, path.y)
    while path != None:
        path = path.expanded_by
        if path != None:
            print(path.x, path.y)

    print(game_map)
    # print_map_f(enemy1.map_bot)
    # print_map_g(enemy1.map_bot)
    # print_map_h(enemy1.map_bot)
