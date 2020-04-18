import random
import time
import threading
import signal
import juego


stop_threads=False
switch = False
run = True
damage=0
move=''
arrows=[('> '*12+' '*26+'\n')*10,(' '*26+'< '*12+'\n')*10,('v '*25+'\n')*5,('^ '*25+'\n')*5,'\n'*5]

# Horde!

def count_space():
    counter=0
    while True:
        a=input()
        if a==' ':
            counter+=1
        if counter==20:
            global stop_threads
            stop_threads= True
            break
        if switch:
            break
            
def goblins():
    tiempo=600
    while tiempo:
        mins, secs = divmod(tiempo, 60)
        horde= " "*(int(2.5*mins))+"\U0001F47A"*(20-int(2*mins))
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
    print(mins+secs/100)
        
def run_trap(player):
    global stop_threads
    global switch
    global run
    run = True
    stop_threads=False
    switch=False
    juego.scream('PELIGRO')
    time.sleep(1)
    juego.slow_print('Algo se aproxima..')
    time.sleep(1)
    juego.scream('CORRE')
    t1 = threading.Thread(target=count_space)
    t2 = threading.Thread(target=goblins)

    t1.start()
    t2.start()
    t2.join()
    t1.join()
    time.sleep(2)
    if run:
        juego.slow_print('Lograste escapar de esta, que pesados son los duentes.')
    else:
        juego.slow_print('Los dejas atrás pero te de das cuenta del daño que te hicieron.')
        vida=player.health
        player.receive_damage(50,0)
        juego.slow_print('Perdiste {} de vida'.format(vida-player.health))

# Arrows!
    
def dodge_trap():
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
            time.sleep(1)
            if move!='s':
                damage+=1
        elif arrow==3:
            print(arrows[4])
            print(arrows[arrow])
            time.sleep(1)
            if move!='w':
                damage+=1
        elif arrow==1:
            print(arrows[arrow])
            time.sleep(1)
            if move != "a":
                damage+=1
        else:
            print(arrows[arrow])
            time.sleep(1)
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
        
def arrow_trap(player):
    global switch
    switch=False
    juego.scream('CUIDADO')
    time.sleep(2)
    t1 = threading.Thread(target=player_moves)
    t2 = threading.Thread(target=dodge_trap)
    t1.start()
    t2.start()
    t2.join()
    print('Presiona enter para continuar')
    t1.join()
    juego.slow_print("Te pegaron {} flechas!".format(damage))
    if damage >=1:
        juego.slow_print('Perdiste {} de vida'.format(10*damage - player.shield_lvl*3))
        player.receive_damage(10*damage,player.shield_lvl*3)
    else:
        juego.slow_print('Lograste salir ileso, que molestos son esos duendes.')
    
# Decide!

def voice_trap(player):
    choice=False
    juego.slow_print('Vas caminando cuando escuchas una voz que te habla...')
    juego.slow_talk('FRENTE A TI ENCONTRARÁS UN REGALO, TÓMALO')
    time.sleep(2)
    juego.slow_print('La voz sonaba un poco sospechosa...')
    while choice not in ['1','2']:
        choice = input('Decide:\n1)Mejor continuar tu camino\n2)Tomar regalo')
    if choice=='1':
        juego.slow_print('Continuas tu camino ignorando la voz.')
    else:
        print(".",end="\r")
        time.sleep(1)
        print("..",end="\r")
        time.sleep(1)
        print("...",end="\r")
        time.sleep(1)
        luck=random.randint(1,5)
        if luck==5:
            juego.slow_print('Encuentras una posión de vida y decides beberla.')
            vida=player.health
            player.receive_damage(0,30)
            if vida < player.health:
                juego.slow_print('Has ganado {} de vida.'.format(player.health-vida))
            else:
                juego.slow_print('Nada sucede.')
        else:
            juego.slow_print('Encuentras una posión de vida y decides beberla.')
            juego.slow_print('Inmediatamente te das cuenta que cometiste un error.')
            vida=player.health
            player.receive_damage(10,0)
            juego.slow_print('Pierdes {} de vida'.format(vida-player.health))
            