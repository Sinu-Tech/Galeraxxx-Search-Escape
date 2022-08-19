from models.Player import Player
from models.Enemy import Enemy


if __name__ == "__main__":
    user = Player("Player", 0, 0, 1.2)

    user.move('down')
    print(user.pos_x, user.pos_y)
    user.move('up')
    user.move('right')
    print(user.pos_x, user.pos_y)
    user.move('left')

    enemy1 = Enemy("Enemy1", 0, 0, 1.0)

    enemy1.move('down')
    print(enemy1.pos_x, enemy1.pos_y)
    enemy1.move('up')
    enemy1.move('right')
    print(enemy1.pos_x, enemy1.pos_y)
    enemy1.move('left')
