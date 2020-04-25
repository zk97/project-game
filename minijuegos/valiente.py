# BARRA EN LUGAR DE TEMPORIZADOR
import random
import time
import threading
import juego

stop_threads=False
player_time=10

def player_timer():
    tiempo=600
    while tiempo:
        if stop_threads: 
            break
        mins, secs = divmod(tiempo, 60)
        timeformat = '{:02d}:{:02d} '.format(mins, secs)
        if tiempo<180:
            timeformat='     '
        bar= timeformat+'.'*(int(2.5*mins+secs/24))+" "*(25-int(2.5*mins+secs/24))
        print(bar,end='\r')
        time.sleep(.0065)
        tiempo -= 1
    global player_time
    if tiempo==0:
        print('                                      ')
        time.sleep(0.4)
        juego.scream('¡BAM!')
        juego.slow_print('Es un golpe crítico')
        player_time=0
    else:
        print('                                        ')
        player_time=mins+secs/100
    
def cpu_time():
    intervalo=random.randint(1,20)
    if intervalo <=15:
        respuesta=random.randint(40,100)
    elif intervalo >19:
        respuesta=random.randint(10,40)
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
    t2.join()

def play(player,tutorial):
    p_time=10
    c_time=10
    if not tutorial:
        set_player_time()
        time.sleep(1)
        p_time=player_time
        if p_time==0:
            juego.slow_print('No presionaste enter a tiempo, hazlo antes para la próxima.')
        else:
            juego.slow_print('Paraste con {:.2f} segundos restantes.'.format(p_time))
    else:
        while p_time==c_time:
            set_player_time()
            time.sleep(1)
            p_time=player_time
            c_time=cpu_time()
            if p_time==c_time:
                juego.slow_print("El jugador paró con {:.2f} segundos restantes.\nEl campeón paró con {:.2f} segundos restantes.\n Es un empate! Listos para el desempate.".format(p_time,c_time))
                time.sleep(4)
        if p_time==0:
            vida = player.health
            player.receive_damage(15,0)
            juego.slow_talk("-Tal vez necesitas tus ojos más de lo que creías. Te reventaste la cabeza.\nY me quedo con tu escudo.")
            juego.slow_print("Pierdes {} de vida.".format(vida-player.health))
            player.shield_down()
            return 0
        elif p_time<c_time:
            print('')
            juego.slow_print("Has ganado, tus sentidos no te engañan.\nParaste con {:.2f} segundos restantes.\nAquel cobarde tenía {:.2f} segundos restantes.".format(p_time,c_time))
            player.shield_up()
            return 1
        else:
            juego.slow_print("Tal vez necesitas tus ojos más de lo que creías.\nTe has acobardado, aun te restaban {:.2f} segundos. Tu rival paro con tan solo {:.2f} segundos restantes.".format(p_time,c_time))
            juego.slow_talk('-Gracias por tu escudo camarada')
            player.shield_down()
            return 0
