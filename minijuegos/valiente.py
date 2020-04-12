# BARRA EN LUGAR DE TEMPORIZADOR
import random
import time
import threading
import sys

stop_threads=False
player_time=10

def player_timer():
    tiempo=600
    while tiempo:
        mins, secs = divmod(tiempo, 60)
        timeformat = '{:02d}:{:02d} '.format(mins, secs)
        if tiempo<180:
            timeformat='     '
        bar= timeformat+'.'*(int(2.5*mins+secs/24))+" "*(25-int(2.5*mins+secs/24))
        print(bar,end='\r')
        time.sleep(.0065)
        if stop_threads: 
            break
        tiempo -= 1
    global player_time
    if tiempo==0:
        print('BAM! Es un golpe crítico')
        player_time=0
    else:
        player_time=mins+secs/100
    
def cpu_time():
    intervalo=random.randint(1,20)
    if intervalo <=15:
        respuesta=random.randint(60,120)
    elif intervalo >19:
        respuesta=random.randint(30,60)
    else:
        respuesta=random.randint(100,150)
    mins, secs= divmod(respuesta,60)
    return mins+secs/100

def stop():
    while True:
        global stop_threads
        input() 
        stop_threads = True
        break

def set_player_time():
    global stop_threads
    stop_threads=False
    t1 = threading.Thread(target=stop)
    t2 = threading.Thread(target=player_timer)
    t1.start()
    t2.start()
    t1.join()

def brave_dumb():
    p_time=10
    c_time=10
    while p_time==c_time:
        set_player_time()
        time.sleep(1)
        p_time=player_time
        c_time=cpu_time()
        if p_time==c_time:
            print("El jugador paró con {:.2f} segundos restantes.\nEl campeón paró con {:.2f} segundos restantes.\n Es un empate! Listos para el desempate.".format(p_time,c_time))
            time.sleep(5)
    if p_time==0:
        print("Tal vez necesitas tus ojos más de lo que creías. Te han reventado la cabeza.")
    elif p_time<c_time:
        print("Haz ganado, tus sentidos no te engañan.\nParaste con {:.2f} segundos restantes\nAquel cobarde tenía {:.2f} segundos restantes.".format(p_time,c_time))  
    else:
        print("Tal vez necesitas tus ojos más de lo que creías.\nTe has acobardado, aun te restaban {:.2f} segundos. Tu rival paro con tan solo {:.2f} segundos restantes.".format(p_time,c_time))