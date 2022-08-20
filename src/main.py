from pprint import pprint
from models import Cell, Enemy, Player

if __name__ == "__main__":
    user = Player("Player", 19, 19, 1.2)
    enemy1 = Enemy("Enemy1", 0, 0, 1.0)

    enemy1.update_map_fh(user.pos_x, user.pos_y)
    # print("Mapa de f antes:")
    # enemy1.print_maph()

    back = enemy1.get_expansions(user.pos_x, user.pos_y)
    # print("Mapa de f depois:")
    # enemy1.print_maph()
    # print("Expansões:")

    while back != None:
        back = back.expanded_by
        if back != None:
            print(back.x, back.y)
