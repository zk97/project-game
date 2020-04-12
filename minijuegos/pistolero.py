import random
import time

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
            while play_move not in [1,3]:
                play_move=int(input(TEXT_EMPTY))
                if play_move==2:
                    play_move+=1
            
        elif self.bullets==self.max:
            while play_move not in [2,3]:
                play_move=int(input(TEXT_FULL))
                play_move+=1
        else:
            while play_move not in [1,2,3]:
                play_move=int(input(TEXT))
        return play_move
    
    def cpu_choose_move(self):
        if self.bullets==0:
            return random.choice([1,3])
        elif self.bullets==self.max:
            return random.randint(2,3)
        else:
            return random.randint(1,3)
        
def simulate_duel(player,cpu):
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
        print("Inicia la ronda, cada quien tiene 1 bala cargada")
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
                    print("Logras cargar tu arma y notas que tu rival hizo lo mismo")
                elif cpu_move==2:
                    player.hp-=1
                    print("BANG! Sientes un dolor y calor que se extiende en tu pierna")
                    C_WINS+=1
                    print("'Es todo lo que tienes?'")
                    break
                else:
                    player.recharge()
                    print("En cuanto tocas tu pistola, tu rival se cubre. Tranquilamente recargas")
            elif play_move==2:
                if cpu_move==1:
                    cpu.hp-=1
                    a=[1,2,3]
                    a.remove(cpu_first)
                    cpu_firs=random.choice(a)
                    print("BANG! Agarras a tu enemigo tratando de recargar y das en el blanco")
                    P_WINS+=1
                    print("'No puedo creer que me diste!!'")
                    break
                elif cpu_move==2:
                    player.shoot()
                    cpu.shoot()
                    print("BANG!! Ambos disparan a la vez y las balas chocan entre si")
                else:
                    player.shoot()
                    print("Bang! Justo antes de jalar el gatillo ves como tu enemigo alcanza a cubrirse, una bala desperdiciada")
            else:
                if cpu_move==1:
                    cpu.recharge
                    print("Te apresuras a cubrirte pero tu enemigo aprovecha esta oportunidad para recargar")
                elif cpu_move==2:
                    cpu.shoot()
                    print("Bang! Excelentes reflejos! Logras evitar que esa bala diera en el blanco")
                else:
                    print("...")
                    print("Se miran fijamente ambos protegiendose")
        game_round+=1
    if P_WINS==2:
        print('Player wins')
    else:
        print('Player looses')