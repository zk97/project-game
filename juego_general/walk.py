from mapa import Outdoors,Cave
from characters import Warrior
from duelos import duel
import sys
sys.path.append('..')
from minijuegos import acertijos,candado,examen,pistolero,trampas,valiente
import numpy as np

full_options=['a','s','w','d']
options=[]
outdoors=np.empty((5,5),dtype=type)

def create_map():
    outdoors[0,0]=Outdoors('Base')
    outdoors[0,1]=Outdoors('Lake')
    outdoors[0,2]=Outdoors('Lake')
    outdoors[1,2]=Outdoors('Lake')
    outdoors[2,1]=Outdoors('Forest')
    outdoors[3,1]=Outdoors('Forest')
    outdoors[3,2]=Outdoors('Forest')
    outdoors[4,2]=Outdoors('Forest')
    outdoors[0,3]=Outdoors('Dessert')
    outdoors[1,3]=Outdoors('Dessert')
    outdoors[1,4]=Outdoors('Dessert')
    outdoors[2,3]=Outdoors('Blocked')
    outdoors[2,4]=Outdoors('Blocked')
    outdoors[0,4]=Outdoors('Coliseum')
    outdoors[4,0]=Outdoors('Store')
    outdoors[np.random.randint(3,4),np.random.randint(3,4)]=Outdoors('Cave')
    for x in range(3,5):
        for y in range(3,5):
            if outdoors[x,y]==None:
                outdoors[x,y]=Outdoors('Cemetery')
    for x in range(5):
        for y in range(5):
            if outdoors[x,y]==None:
                outdoors[x,y]=Outdoors('Normal')
                
                
def make_options(player):
    global options
    options=[]
    if player.location[0]!=0:
        options.append('a')
    if player.location[0]!=4:
        options.append('d')
    if player.location[1]!=0:
        options.append('s')
    if player.location[1]!=4:
        options.append('w')
        
                
def walk(player,direction):
    if direction=='a':
        player.location[0]-=1
    elif direction=='d':
        player.location[0]+=1
    elif direction=='s':
        player.location[1]-=1
    else:
        player.location[1]+=1
    return event(player)
        
def coliseum(player):
    past_health=player.health
    past_magic=player.magic
    while true:
        keep=''
        while keep.lower() not in ['si','no']:
            keep=input('¿Quieres pelear en el coliseo?')
        if keep.lower()=='no':
            break
        player.health=100
        player.magic=100
        challenger=Warrior(1,1,1,1)
        challenger.set_gun_dmg()
        challenger.set_magic_cost()
        challenger.set_magic_dmg()
        challenger.set_max_bullets()
        challenger.set_sword_dmg()
        duel(player,challenger)
    player.health=past_health
    player.magic=past_magic
        
    
def cueva(player,cave):
    enemy=Warrior(2,2,2,2)
    while True:
        result=0
        final_result=3
        choice='Salida'
        doors=cave.show_doors()
        while choice.lower() not in [x.lower() for x in doors]:
            for door in doors:
                print("Puerta '{}'".format(door),end='   ')
            choice=input()
        if choice.lower()=='pistolero':
            result=pistolero.play(player)
        elif choice.lower()=='candado':
            result=candado.play(player)
        elif choice.lower()=='acertijos':
            result=acertijos.play(player)
        elif choice.lower()=='valiente':
            result=valiente.play(player)
        elif choice.lower()=='examen':
            result=examen.play(player)
        else:
            final_result=duel(player,enemy)
        if result:
            cave.set_doors()
        if final_result==1:
            print('Ganaste')
            break
        elif final_result==2:
            print('Empate, ambos ganan 50 de vida')
            player.health+=50
            enemy.health+=50
        elif final_result==0:
            print('Game over')
            break
            
    
    
def store(player):
    items=dict()
    item=''
    answer=''
    while True:
        if not player.sword_lvl:
            items['Espada']=15
        if not player.gun_lvl:
            items['Revolver']=15
        if not player.shield_lvl:
            items['Escudo']=10
        items['Posion de vida']=5
        items['Posion de magia']=5
        items['Salir']=0
        while item.lower() not in [x.lower() for x in items.keys()]:
            print('¿Que deseas comprar?')
            for x in items.keys():
                if x !='Salir':
                    print("{}  ${}".format(x,items[x]))
                else:
                    print(x)
            item=input()
        if item=='Espada':
            player.buy_sword(items[item])
        elif item=='Revolver':
            player.buy_gun(items[item])
        elif item=='Escudo':
            player.buy_gun(items[item])
        elif item=='Posion de vida':
            player.buy_pot(items[item],'health')
        elif item=='Posion de magia':
            player.buy_pot(items[item],'magic')
        else:
            break
        while answer.lower() not in ['si','no']:
            print('¿Desea seguir comprando?\nSi    No')
            answer=input()
        if answer=='No':
            break
         
        
#8 nada,7miniduelo,6trampa,5objetoaleatorio,4,bloqueado,3,cueva,2tienda,1coliseo,0base        

def event(player):
    location=player.location()[0],player.location()[1]
    event=0
    if outdoors[location]=='Coliseum':
        event=1
    elif outdoors[location]=='Store':
        event=2
    elif outdoors[location]=='Cave':
        event=3
    elif outdoors[location]=='Lake':
        luck=random.randint(1,10)
        if luck<10:
            event=8
        else:
            event=5
    elif outdoors[location]=='Dessert':
        luck=random.randint(1,10)
        if luck==1:
            event=8
        elif luck<4:
            event=7
        else:
            event=6
    elif outdoors[location]=='Forest':
        luck=random.randint(1,10)
        if luck==1:
            event=5
        elif luck<4:
            event=7
        else:
            event=6
    elif outdoors[location]=='Cemetery':
        luck=random.randint(1,10)
        if luck<3:
            event=5
        else:
            event=7
    elif outdoors[location]=='Normal':
        luck=random.randint(1,10)
        if luck==1:
            event=5
        elif luck<7:
            event=8
        elif luck<9:
            event=6
        else:
            event=7
    else:
        event=4
    return event