from models.Player import Player
from models.Enemy import Enemy


if __name__ == "__main__":
    user = Player("Player", 5, 10, 1.2)

    enemy1 = Enemy("Enemy1", 10, 19, 1.0)

    enemy1.print_maph()
    enemy1.update_maph(user.pos_x, user.pos_y)
    enemy1.print_maph()
