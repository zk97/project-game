import mapa,duelos
from characters import Warrior,Goblin
import sys,random
sys.path.append('..')
from minijuegos import acertijos,candado,examen,pistolero,trampas,valiente


#8 nada,7miniduelo,6trampa,5objetoaleatorio,4,bloqueado,3,cueva,2tienda,1coliseo,0base        

def player_move(player):
    player_move=''
    options,show_opt = mapa.make_options(player)
    while player_move not in options:
        print('¿Hacia dónde deseas moverte?\nTus opciones son:')
        for x in show_opt:
            print(x,end='   ')
        print('\n')
        player_move=input()
    event=mapa.walk(player,player_move)
    if event==1:
        mapa.coliseum(player)
    elif event==2:
        mapa.store(player)
    elif event==3:
        mapa.cueva(player)
    elif event==4:
        print('Camino bloqueado')
    elif event==5:
        found=random.randint(1,10)
        if found <8:
            player.find_money()
        elif found <10:
            player.find_bag()
        else:
            player.find_pot()
    elif event==6:
        trap=random.randint(1,3)
        if trap==1:
            trampas.run_trap(player,1)
        elif trap==2:
            trampas.arrow_trap(player,1)
        else:
            trampas.voice_trap(player)
    elif event==7:
        duelos.duel(player,Goblin())
    elif event==8:
        print('Nada pasa')
    else:
        tutorial=''
        while tutorial.lower() not in ['si','no']:
            print('¿Quieres volver a jugar el tutorial?\nSi   No')
            tutorial=input()
        if tutorial.lower()=='si':
            mapa.tutorial()
        else:
            pass