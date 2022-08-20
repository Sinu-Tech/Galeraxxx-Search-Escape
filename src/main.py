from pprint import pprint
from models import Cell, Enemy, Player

if __name__ == "__main__":
    user = Player("Player", 4,4, 1.2)
    enemy1 = Enemy("Enemy1", 0, 0, 1.0)

    # enemy1.update_map_fh(user.pos_x, user.pos_y)

    back = enemy1.get_expansions(user.pos_x, user.pos_y)

    enemy1.print_map_f()
    enemy1.print_map_g()
    enemy1.print_map_h()
    print("back:")    
    print(back.x, back.y)
    while back != None:
        back = back.expanded_by
        if back != None:
            print(back.x, back.y)

    enemy1.print_visiteds()