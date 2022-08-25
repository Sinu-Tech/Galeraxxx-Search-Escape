from models import Enemy, Player
from utils.map_utils import *
from models.maps import *
import keyboard 

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


    while True:                                                                 
        pressedKey = keyboard.read_key()
        if pressedKey == "a":
            print("clicou em a")
            if(user.pos_x >0):
                print('move a')
            
        if pressedKey == "d":
            print("clicou em d")
            if(user.pos_x >width_map):
                print('move d')
            
        if pressedKey == "w":
            print("clicou em w")
            if(user.pos_y >0):
                print('move w')
            
        if pressedKey == "s":
            print("clicou em s")
            if(user.pos_y >height_map):
                print('move s')
                
