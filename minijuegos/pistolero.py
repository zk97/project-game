import random
import time
import juego

BASE_BULL = 1
MAX_BULL=5
MAX_HP=2
TEXT="Que decides hacer?\n 1)Recargo\n 2)Disparo\n 3)Me cubro\n"
TEXT_EMPTY="Que decides hacer?\n 1)Recargo\n 2)Me cubro\n"
TEXT_FULL="Que decides hacer?\n 1)Disparo\n 2)Me cubro\n"

#Enemy

class Player:
    def __init__(self):
        self.bullets=BASE_BULL
        self.max=MAX_BULL
        self.hp=MAX_HP
        
    def shoot(self):
        self.bullets-=1
        
    def recharge(self):
        self.bullets+=1
        
    def player_choose_move(self):
        time.sleep(2)
        play_move=0
        if self.bullets==0:
            while play_move not in ['1','3']:
                play_move=input(TEXT_EMPTY)
                if play_move=='2':
                    play_move='3'
            
        elif self.bullets==self.max:
            while play_move not in ['2','3']:
                play_move=input(TEXT_FULL)
                if play_move=='1':
                    playe_move='2'
                elif play_move=='2':
                    play_move='3'
        else:
            while play_move not in ['1','2','3']:
                play_move=input(TEXT)
        return int(play_move)
    
    def cpu_choose_move(self):
        if self.bullets==0:
            return random.choice([1,3])
        elif self.bullets==self.max:
            return random.randint(2,3)
        else:
            return random.randint(1,3)
        
def play(player1):
    player=Player()
    cpu=Player()
    C_WINS=0
    P_WINS=0
    game_round=0
    while P_WINS!=2 and C_WINS!=2 :
        cpu_moves=0
        player.bullets=1
        cpu.bullets=1
        if game_round==0:
            cpu_first=cpu.cpu_choose_move()
        time.sleep(1)
        juego.slow_print("Inicia la ronda, cada quien tiene 1 bala cargada.")
        while True:
            play_move=player.player_choose_move()
            if cpu_moves==0:
                cpu_move=cpu_first
                cpu_moves+=1
            else:
                cpu_move=cpu.cpu_choose_move()
            if play_move==1:
                if cpu_move==1:
                    player.recharge()
                    cpu.recharge()
                    juego.slow_print("Logras cargar tu arma y notas que tu rival hizo lo mismo.")
                elif cpu_move==2:
                    player.hp-=1
                    juego.scream('¡BANG!')
                    juego.slow_print("Sientes un dolor y calor que se extiende en tu pierna.")
                    C_WINS+=1
                    juego.slow_talk("-¿Es todo lo que tienes?")
                    break
                else:
                    player.recharge()
                    juego.slow_print("En cuanto tocas tu pistola, tu rival se cubre. Tranquilamente recargas.")
            elif play_move==2:
                if cpu_move==1:
                    cpu.hp-=1
                    a=[1,2,3]
                    a.remove(cpu_first)
                    cpu_first=random.choice(a)
                    juego.scream('¡BANG!')
                    juego.slow_print("Agarras a tu enemigo tratando de recargar y das en el blanco.")
                    P_WINS+=1
                    juego.slow_talk("-¡¡No puedo creer que me diste!!")
                    break
                elif cpu_move==2:
                    player.shoot()
                    cpu.shoot()
                    juego.scream('¡¡BANG!!')
                    juego.slow_print("Ambos disparan a la vez y las balas chocan entre si.")
                else:
                    player.shoot()
                    juego.scream("Bang")
                    juego.slow_print("Justo antes de jalar el gatillo ves como tu enemigo alcanza a cubrirse, una bala desperdiciada")
            else:
                if cpu_move==1:
                    cpu.recharge
                    juego.slow_print("Te apresuras a cubrirte pero tu enemigo aprovecha esta oportunidad para recargar.")
                elif cpu_move==2:
                    cpu.shoot()
                    juego.scream('Bang')
                    juego.slow_print("Excelentes reflejos! Logras evitar que esa bala diera en el blanco")
                else:
                    juego.scream("...")
                    juego.slow_print("Se miran fijamente ambos protegiendose")
        game_round+=1
    if P_WINS==2:
        juego.slow_print('Sales airoso de este enfrentamiento.')
        player1.gun_up()
        return 1
    else:
        juego.slow_print('Fuiste derrotado.')
        player1.gun_down()
        return 0