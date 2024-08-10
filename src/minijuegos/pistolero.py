from src.utils.functions import slow_print, slow_talk, scream
import random
import time


class Player:
    def __init__(self, max_bullets=5):
        self.max_bullets = max_bullets
        self.bullets = 1
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


def play(gen_player):
    if gen_player.gun_lvl > 0:
        player = Player(gen_player.max_bullets)
    else:
        player = Player()

    cpu = Player()
    cpu_first_move = 0
    starting_game = True

    while player.hp > 0 and cpu.hp > 0:
        starting_round = True
        player.bullets = 1
        cpu.bullets = 1
        time.sleep(1)
        slow_print("Inicia la ronda, cada quien tiene 1 bala cargada.")
        while True:
            play_move = player.player_choose_move()
            cpu_move = cpu.cpu_choose_move()
            if starting_round:
                starting_round = False
                if starting_game:
                    cpu_first_move = cpu_move
                    starting_game = False
                else:
                    opciones_limitadas = [1, 2, 3]
                    opciones_limitadas.remove(cpu_first_move)
                    cpu_move = random.choice(opciones_limitadas)
            match (player.opciones[play_move], cpu.opciones[cpu_move]):
                case ('Me cubro', 'Me cubro'):
                    scream("...")
                    slow_print("Se miran fijamente ambos protegiendose")
                case ('Me cubro', 'Recargo'):
                    cpu.recharge()
                    slow_print("Te apresuras a cubrirte pero tu enemigo aprovecha esta oportunidad para recargar.")
                case ('Me cubro', 'Disparo'):
                    cpu.shoot()
                    scream('Bang')
                    slow_print("Excelentes reflejos! Logras evitar que esa bala diera en el blanco")
                case ('Recargo', 'Me cubro'):
                    player.recharge()
                    slow_print("En cuanto tocas tu pistola, tu rival se cubre. Tranquilamente recargas.")
                case ('Recargo', 'Recargo'):
                    player.recharge()
                    cpu.recharge()
                    slow_print("Logras cargar tu arma y notas que tu rival hizo lo mismo.")
                case ('Recargo', 'Disparo'):
                    player.hp -= 1
                    scream('¡BANG!')
                    slow_print("Sientes un dolor y calor que se extiende en tu pierna.")
                    slow_talk("-¿Es todo lo que tienes?")
                    break
                case ('Disparo', 'Me cubro'):
                    player.shoot()
                    scream("Bang")
                    slow_print(
                        "Justo antes de jalar el gatillo ves como tu enemigo alcanza a cubrirse, una bala desperdiciada")
                case ('Disparo', 'Recargo'):
                    cpu.hp -= 1
                    scream('¡BANG!')
                    slow_print("Agarras a tu enemigo tratando de recargar y das en el blanco.")
                    slow_talk("-¡¡No puedo creer que me diste!!")
                    break
                case ('Disparo', 'Disparo'):
                    player.shoot()
                    cpu.shoot()
                    scream('¡¡BANG!!')
                    slow_print("Ambos disparan a la vez y las balas chocan entre si.")
    if player.hp > 0:
        slow_print('Sales airoso de este enfrentamiento.')
        gen_player.gun_up()
        return 1
    else:
        slow_print('Fuiste derrotado.')
        gen_player.gun_down()
        return 0
