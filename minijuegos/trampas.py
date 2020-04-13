import random
import time
import threading
import signal


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
        if counter==25:
            global stop_threads
            stop_threads= True
            break
        if switch:
            print(30-counter)
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
        
def run_trap():
    global stop_threads
    global switch
    global run
    run = True
    stop_threads=False
    switch=False
    t1 = threading.Thread(target=count_space)
    t2 = threading.Thread(target=goblins)

    t1.start()
    t2.start()
    t2.join()
    if run:
        print('\nSobreviviste a la trampa')
    else:
        print('\nNo lo lograste')

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
            time.sleep(1.5)
            if move!='s':
                print(move)
                damage+=1
        elif arrow==3:
            print(arrows[4])
            print(arrows[arrow])
            time.sleep(1.5)
            if move!='w':
                print(move)
                damage+=1
        elif arrow==1:
            print(arrows[arrow])
            time.sleep(1.5)
            if move != "a":
                print(move)
                damage+=1
        else:
            print(arrows[arrow])
            time.sleep(1.5)
            if move != "d":
                print(move)
                damage+=1
        rounds-=1
    switch=True
        
def player_moves():
    while not switch:
        global move
        move=input()
        
def arrow_trap():
    global switch
    switch=False
    t1 = threading.Thread(target=player_moves)
    t2 = threading.Thread(target=dodge_trap)

    t1.start()
    t2.start()
    t2.join()
    print("Te pegaron {} flechas!".format(damage))
    
# Decide!

def voice_trap():
    choice=False
    while choice not in ['1','2']:
        choice = input('Decide\n1)Continua tu camino\n2)Acepta el riesgo')
    if choice=='1':
        print('Continua tu camino.')
    else:
        print(".",end="\r")
        time.sleep(1)
        print("..",end="\r")
        time.sleep(1)
        print("...",end="\r")
        time.sleep(1)
        luck=random.randint(1,5)
        if luck==5:
            print('Ganaste!')
        else:
            print('Lastima!')