from src.utils.functions import slow_print, slow_talk, scream
import random
import time

MAX_BULL = 5


class Player:
    def __init__(self):
        self.bullets = 1
        self.max_bullets = 5
        self.hp = 2
        self.opciones = {}

    def shoot(self):
        self.bullets -= 1

    def recharge(self):
        self.bullets += 1

    def get_move_options(self):
        self.opciones = {1: 'Me cubro'}
        if self.bullets > 0:
            self.opciones[max(self.opciones.keys()) + 1] = 'Disparo'
        if self.bullets < self.max_bullets:
            self.opciones[max(self.opciones.keys()) + 1] = 'Recargo'

    def player_choose_move(self):
        time.sleep(2)
        play_move = 0
        self.get_move_options()
        while play_move not in self.opciones.keys():
            print("Que decides hacer?")
            for key, val in self.opciones.items():
                print(f'{key}) {val}')
            play_move = input()
            try:
                play_move = int(play_move)
            except ValueError:
                pass

        return play_move

    def cpu_choose_move(self):
        self.get_move_options()
        return random.choice(list(self.opciones.keys()))


def play(player1):
    global MAX_BULL
    MAX_BULL = 5
    if player1.gun_lvl > 0:
        MAX_BULL = player1.max_bullets
    player = Player()
    cpu = Player()
    C_WINS = 0
    P_WINS = 0
    game_round = 0
    while P_WINS != 2 and C_WINS != 2:
        cpu_moves = 0
        player.bullets = 1
        cpu.bullets = 1
        if game_round == 0:
            cpu_first = cpu.cpu_choose_move()
        time.sleep(1)
        slow_print("Inicia la ronda, cada quien tiene 1 bala cargada.")
        while True:
            play_move = player.player_choose_move()
            if cpu_moves == 0:
                cpu_move = cpu_first
                cpu_moves += 1
            else:
                cpu_move = cpu.cpu_choose_move()
            if play_move == 1:
                if cpu_move == 1:
                    player.recharge()
                    cpu.recharge()
                    slow_print("Logras cargar tu arma y notas que tu rival hizo lo mismo.")
                elif cpu_move == 2:
                    player.hp -= 1
                    scream('¡BANG!')
                    slow_print("Sientes un dolor y calor que se extiende en tu pierna.")
                    C_WINS += 1
                    slow_talk("-¿Es todo lo que tienes?")
                    break
                else:
                    player.recharge()
                    slow_print("En cuanto tocas tu pistola, tu rival se cubre. Tranquilamente recargas.")
            elif play_move == 2:
                if cpu_move == 1:
                    cpu.hp -= 1
                    a = [1, 2, 3]
                    a.remove(cpu_first)
                    cpu_first = random.choice(a)
                    scream('¡BANG!')
                    slow_print("Agarras a tu enemigo tratando de recargar y das en el blanco.")
                    P_WINS += 1
                    slow_talk("-¡¡No puedo creer que me diste!!")
                    break
                elif cpu_move == 2:
                    player.shoot()
                    cpu.shoot()
                    scream('¡¡BANG!!')
                    slow_print("Ambos disparan a la vez y las balas chocan entre si.")
                else:
                    player.shoot()
                    scream("Bang")
                    slow_print(
                        "Justo antes de jalar el gatillo ves como tu enemigo alcanza a cubrirse, una bala desperdiciada")
            else:
                if cpu_move == 1:
                    cpu.recharge
                    slow_print("Te apresuras a cubrirte pero tu enemigo aprovecha esta oportunidad para recargar.")
                elif cpu_move == 2:
                    cpu.shoot()
                    scream('Bang')
                    slow_print("Excelentes reflejos! Logras evitar que esa bala diera en el blanco")
                else:
                    scream("...")
                    slow_print("Se miran fijamente ambos protegiendose")
        game_round += 1
    if P_WINS == 2:
        slow_print('Sales airoso de este enfrentamiento.')
        player1.gun_up()
        return 1
    else:
        slow_print('Fuiste derrotado.')
        player1.gun_down()
        return 0
