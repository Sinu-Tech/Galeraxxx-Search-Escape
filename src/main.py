from models import Cell, Enemy, Player


if __name__ == "__main__":
    user = Player("Player", 4, 2, 1.2)
    enemy1 = Enemy("Enemy1", 10, 10, 1.0)

    enemy1.update_maph(user.pos_x, user.pos_y)
    enemy1.print_maph()

    # print(enemy1.get_expansions(user.pos_x, user.pos_y))
