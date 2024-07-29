import general.mapa as mapa
import general.walk as walk
from general.characters import Warrior
from utils.functions import slow_print, slow_talk, scream
import time

def start_game():
    slow_print('Otro día igual que siempre, fuera de tus sueños lo único que puedes ver son estas letras dentro de tu cabeza.')
    scream('-HEY!')
    slow_talk('-Ven, tengo que mostrarte algo.')
    slow_print('Caminas hacia donde está tu abuelo.')
    slow_talk('-Pronto llegará el día en que no esté y tendrás que cuidarte por tu cuenta.\n-Tengo un regalo para ti, pero tendrás que aprender a dominarlo por tu cuenta')
    print('.',end='\r')
    time.sleep(1)
    print("..",end="\r")
    time.sleep(1)
    print("...",end="\r")
    time.sleep(1)
    slow_print('VARA MÁGICA CONSEGUIDA')
    time.sleep(1)
    slow_print('ESCUDO MÁGICO CONSEGUIDO')
    slow_talk('-Hora de entrenar un poco')
    mapa.create_map()
    player=Warrior(1,0,0,0)
    player.set_warrior()
    mapa.tutorial()
    slow_print('Saliendo del tutorial')
    time.sleep(1)
    print('.',end='\r')
    time.sleep(1)
    print("..",end="\r")
    time.sleep(1)
    print("...",end="\r")
    time.sleep(1)
    while True:
        walk.player_move(player)
        if not player.is_alive():
            break
    print('GAME OVER')