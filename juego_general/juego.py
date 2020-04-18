import mapa,walk
from characters import Warrior

def start_game():
    mapa.create_map()
    player=Warrior(1,0,0,0)
    player.set_warrior()
    mapa.tutorial()
    while True:
        walk.player_move(player)
        if not player.is_alive():
            break