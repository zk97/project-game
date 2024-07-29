from utils.functions import slow_print, slow_talk, scream
import random, time, threading, signal


stop_threads=False
switch = False
run = True
damage=0
move=''
arrows=[('> '*12+' '*26+'\n')*10,(' '*26+'< '*12+'\n')*10,('v '*25+'\n')*5,('^ '*25+'\n')*5,'\n'*5]

# Horde!

def count_space(dist):
    counter=0
    while True:
        a=input()
        if a==' ':
            counter+=1
        if counter>=dist:
            global stop_threads
            stop_threads= True
            break
        if switch:
            break
            
def goblins():
    tiempo=600
    while tiempo:
        mins, secs = divmod(tiempo, 60)
        horde= " "*(int(2.5*mins))+"...."*(20-int(2*mins))
        print(horde,end='\r')
        time.sleep(.008)
        if stop_threads: 
            break
        tiempo-=1
    if tiempo==0:
        global switch
        global run
        switch=True
        run=False
        
def run_trap(player,tutorial):
    if not tutorial:
        dist=15
    else:
        dist=25
    global stop_threads
    global switch
    global run
    run = True
    stop_threads=False
    switch=False
    scream('PELIGRO')
    time.sleep(1)
    slow_print('Algo se aproxima...')
    time.sleep(1)
    scream('CORRE')
    t1 = threading.Thread(target=count_space,args=(dist,))
    t2 = threading.Thread(target=goblins)

    t1.start()
    t2.start()
    t2.join()
    t1.join()
    time.sleep(0.5)
    print('')
    if not tutorial:
        if run:
            slow_print('Corriste lo suficientemente rápido.')
        else:
            slow_print('Necesitas ser más veloz, no llegaste a tiempo.')
    else:
        if run:
            slow_print('Lograste escapar de esta, que pesados son los duentes.')
        else:
            slow_print('Los dejas atrás pero te de das cuenta del daño que te hicieron.')
            vida=player.health
            player.receive_damage(50,0)
            slow_print('Perdiste {} de vida'.format(vida-player.health))

# Arrows!
    
def dodge_trap(var_time):
    global move
    global damage
    rounds=random.randint(3,5)
    damage=0
    while rounds:
        move=''
        arrow=random.randint(0,3)
        if arrow==2:
            print(arrows[arrow])
            print(arrows[4])
            time.sleep(var_time)
            if move!='s':
                damage+=1
        elif arrow==3:
            print(arrows[4])
            print(arrows[arrow])
            time.sleep(var_time)
            if move!='w':
                damage+=1
        elif arrow==1:
            print(arrows[arrow])
            time.sleep(var_time)
            if move != "a":
                damage+=1
        else:
            print(arrows[arrow])
            time.sleep(var_time)
            if move != "d":
                damage+=1
        rounds-=1
    global switch
    switch=True
        
def player_moves():
    while True:
        global move
        move=input()
        if switch:
            break
        
def arrow_trap(player,tutorial):
    global switch
    switch=False
    if not tutorial:
        tempo=2
    else:
        tempo=1
    scream('CUIDADO')
    time.sleep(2)
    t1 = threading.Thread(target=player_moves)
    t2 = threading.Thread(target=dodge_trap,args=(tempo,))
    t1.start()
    t2.start()
    t2.join()
    print('Presiona enter para continuar')
    t1.join()
    slow_print("Te pegaron {} piedras!".format(damage))
    if tutorial:
        if damage >=1:
            slow_print('Perdiste {} de vida'.format(10*damage - player.shield_lvl*3))
            player.receive_damage(10*damage,player.shield_lvl*3)
        else:
            slow_print('Lograste salir ileso, que molestos son esos duendes.')
    
# Decide!

def voice_trap(player):
    choice=False
    slow_print('Vas caminando cuando escuchas una voz que te habla...')
    slow_talk('FRENTE A TI ENCONTRARÁS UN REGALO, TÓMALO')
    time.sleep(2)
    slow_print('La voz sonaba un poco sospechosa...')
    while choice not in ['1','2']:
        choice = input('Decide:\n1)Mejor continuar tu camino\n2)Tomar regalo')
    if choice=='1':
        slow_print('Continuas tu camino ignorando la voz.')
    else:
        print(".",end="\r")
        time.sleep(1)
        print("..",end="\r")
        time.sleep(1)
        print("...",end="\r")
        time.sleep(1)
        luck=random.randint(1,5)
        if luck==5:
            slow_print('Encuentras una posión de vida y decides beberla.')
            vida=player.health
            player.receive_damage(0,30)
            if vida < player.health:
                slow_print('Has ganado {} de vida.'.format(player.health-vida))
            else:
                slow_print('Nada sucede.')
        else:
            slow_print('Encuentras una posión de vida y decides beberla.')
            slow_print('Inmediatamente te das cuenta que cometiste un error.')
            vida=player.health
            player.receive_damage(10,0)
            slow_print('Pierdes {} de vida'.format(vida-player.health))
            