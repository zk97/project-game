from characters import Warrior,Goblin
from duelos import duel
import sys, random, time
sys.path.append('..')
from minijuegos import acertijos,candado,examen,pistolero,trampas,valiente
import numpy as np


class Outdoors():
    def __init__(self,kind):
        self.kind=kind
        
    def get_kind(self):
        return self.kind
    
class Cave():
    def __init__(self):
        self.doors=5
        self.games=['Pistolero','Candado','Acertijos','Valiente','Examen']
        
    def set_doors(self):
        self.doors=random.randint(1,self.doors)
        
    def show_doors(self):
        if self.doors==1:
            return ['Salida']
        else:
            return random.sample(self.games,self.doors)

#[forest,lake,begining,cave]

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
    options_nesw=[]
    if player.location[0]!=0:
        options.append('a')
        options_nesw.append('Oeste')
    if player.location[0]!=4:
        options.append('d')
        options_nesw.append('Este')
    if player.location[1]!=0:
        options.append('s')
        options_nesw.append('Sur')
    if player.location[1]!=4:
        options.append('w')
        options_nesw.append('Norte')
    return options,options_nesw
                
def walk(player,direction):
    old_location=player.location.copy()
    if direction=='a':
        player.location[0]-=1
    elif direction=='d':
        player.location[0]+=1
    elif direction=='s':
        player.location[1]-=1
    else:
        player.location[1]+=1
    evento=event(player)
    if evento==4:
        player.location=old_location
    return evento

def coliseum(player):
    past_health=player.health
    past_magic=player.magic
    while True:
        keep=''
        while keep.lower() not in ['si','no']:
            keep=input('¿Quieres pelear en el coliseo?\nSi    No')
        if keep.lower()=='no':
            break
        apuesta=''
        while apuesta.lower() not in ['si','no']:
            apuesta=input('¿Quierés pelear por dinero?\nSi   No')
        if apuesta.lower()=='no':
            challenger=Warrior(1,1,1,1)
            challenger.set_warrior()
            fake=Warrior(1,1,1,1)
            if fake.sword_lvl<player.sword_lvl:
                fake.sword_lvl=player.sword_lvl
            if fake.gun_lvl<player.gun_lvl:
                fake.gun_lvl=player.gun_lvl
            if fake.shield_lvl<player.shield_lvl:
                fake.shield_lvl=player.shield_lvl
            if fake.magic_lvl<player.magic_lvl:
                fake.magic_lvl=player.magic_lvl
            fake.set_warrior()
            duel(fake,challenger)
        else:
            player.health=100
            player.magic=100
            challenger=Warrior(1,1,1,1)
            challenger.set_warrior()
            result=duel(player,challenger)
    player.health=past_health
    player.magic=past_magic
        
def tutorial():
    practicar=['Decisiones','Esquivar','Escapar','Pelear','Pistolero','Candado','Acertijos','Valiente','Examen']
    while True:
        vuelta=0
        out=''
        game=''
        while out.lower() not in ['si','no']:
            print('¿Deseas abandonar tutorial?\nSi   No')
            out=input()
        if out.lower()=='si':
            break
        player=Warrior(1,1,1,1)
        player.set_warrior()
        while game not in practicar:
            print('¿Qué quieres practicar?')
            for x in practicar:
                if practicar.index(x)%3!=2:
                    print(x,end=' '*(25-len(x)))
                else:
                    print(x)
            game=input().capitalize()
        vuelta=practicar.index(game)+1
        if vuelta==1:
            trampas.voice_trap(player)
        elif vuelta==2:
            trampas.arrow_trap(player)
        elif vuelta==3:
            trampas.run_trap(player)
        elif vuelta==4:
            duel(player,Goblin())
        elif vuelta==5:
            pistolero.play(player)
        elif vuelta==6:
            candado.play(player)
        elif vuelta==7:
            acertijos.play(player)
        elif vuelta==8:
            valiente.play(player)
        elif vuelta==9:
            examen.play(player)

        
def cueva(player):
    cave=Cave()
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
    while True:
        items=dict()
        answer=''
        item=''
        if not player.sword_lvl:
            items['Espada']=15
        if not player.gun_lvl:
            items['Revolver']=15
        if not player.shield_lvl:
            items['Escudo']=10
        items['Posion de vida']=5
        items['Posion de magia']=5
        items['Salir']=0
        while item not in items.keys():
            print('¿Que deseas comprar?')
            for x in items.keys():
                if x !='Salir':
                    print("{}  ${}".format(x,items[x]))
                else:
                    print(x)
            item=input().capitalize()
        if item=='Espada':
            player.buy_sword(items[item])
        elif item=='Revolver':
            player.buy_gun(items[item])
        elif item=='Escudo':
            player.buy_shield(items[item])
        elif item=='Posion de vida':
            player.buy_pot(items[item],'health')
        elif item=='Posion de magia':
            player.buy_pot(items[item],'magic')
        else:
            break
        while answer not in ['Si','No']:
            print('¿Desea seguir comprando?\nSi    No')
            answer=input().capitalize()
        if answer=='No':
            break
         
        
#8 nada,7miniduelo,6trampa,5objetoaleatorio,4,bloqueado,3,cueva,2tienda,1coliseo,0base        

def event(player):
    location=player.location[0],player.location[1]
    event=0
    if outdoors[location].get_kind()=='Coliseum':
        event=1
    elif outdoors[location].get_kind()=='Store':
        event=2
    elif outdoors[location].get_kind()=='Cave':
        event=3
    elif outdoors[location].get_kind()=='Lake':
        luck=random.randint(1,10)
        if luck<10:
            event=8
        else:
            event=5
    elif outdoors[location].get_kind()=='Dessert':
        luck=random.randint(1,10)
        if luck==1:
            event=8
        elif luck<4:
            event=7
        else:
            event=6
    elif outdoors[location].get_kind()=='Forest':
        luck=random.randint(1,10)
        if luck==1:
            event=5
        elif luck<4:
            event=7
        else:
            event=6
    elif outdoors[location].get_kind()=='Cemetery':
        luck=random.randint(1,10)
        if luck<3:
            event=5
        else:
            event=7
    elif outdoors[location].get_kind()=='Normal':
        luck=random.randint(1,10)
        if luck==1:
            event=5
        elif luck<7:
            event=8
        elif luck<9:
            event=6
        else:
            event=7
    elif outdoors[location].get_kind()=='Blocked':
        event=4
    return event    
    
    