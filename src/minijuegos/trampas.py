from src.utils.functions import slow_print, slow_talk, scream
import sys
import time
import random
import threading


class Trampas:
    def __init__(self):
        self.stop_threads = False
        self.escape = True
        self.damage = 0
        self.move = ''
        self.arrows = {"derecha": f"{('> ' * 12).ljust(38)}\n" * 10,
                       "izquierda": f"{('< ' * 12).rjust(38)}\n" * 10,
                       "abajo": ('v ' * 38 + '\n') * 5,
                       "arriba": ('^ ' * 38 + '\n') * 5,
                       "espacios": '\n' * 5}

    def count_space(self, dist):
        counter = 0
        while True:
            space = input()
            if space == ' ':
                counter += 1
            if counter >= dist:
                self.stop_threads = True
                break
            if self.stop_threads:
                break

    def goblins(self):
        tiempo = random.randint(18, 23)
        while tiempo:
            horde = "..." * (23 - tiempo)
            sys.stdout.flush()
            print(horde.center(99))
            time.sleep(.25)
            if self.stop_threads:
                break
            tiempo -= 1
        if tiempo == 0:
            self.stop_threads = True
            self.escape = False

    def run_trap(self, player, tutorial):
        scream('PELIGRO')
        time.sleep(1)
        slow_print('Algo se aproxima...')
        time.sleep(1)
        scream('CORRE')
        t1 = threading.Thread(target=self.count_space, args=(30,))
        t2 = threading.Thread(target=self.goblins)
        t1.start()
        t2.start()
        t2.join()
        print('Presiona enter para continuar')
        t1.join()
        time.sleep(1)
        print('')
        if tutorial:
            if self.escape:
                slow_print('Corriste lo suficientemente rápido.')
            else:
                slow_print('Necesitas ser más veloz, no llegaste a tiempo.')
        else:
            if self.escape:
                slow_print('Lograste escapar de esta, que pesados son los duendes.')
            else:
                slow_print('Los dejas atrás pero te de das cuenta del daño que te hicieron.')
                vida = player.health
                player.receive_damage(50, 0)
                slow_print(f'Perdiste {vida - player.health} de vida')

    def player_moves(self):
        while True:
            self.move = input().lower()
            if self.stop_threads:
                break

    def dodge_trap(self, var_time):
        rounds = random.randint(3, 5)
        self.damage = 0
        while rounds:
            self.move = ''
            arrow = random.choice(['derecha', 'izquierda', 'abajo', 'arriba'])
            if arrow == 'abajo':
                print(self.arrows[arrow])
                print(self.arrows['espacios'])
                time.sleep(var_time)
                if self.move != 's':
                    self.damage += 1
            elif arrow == 'arriba':
                print(self.arrows['espacios'])
                print(self.arrows[arrow])
                time.sleep(var_time)
                if self.move != 'w':
                    self.damage += 1
            elif arrow == 'izquierda':
                print(self.arrows[arrow])
                time.sleep(var_time)
                if self.move != "a":
                    self.damage += 1
            else:
                print(self.arrows[arrow])
                time.sleep(var_time)
                if self.move != "d":
                    self.damage += 1
            rounds -= 1
        self.stop_threads = True

    def arrow_trap(self, player, tutorial):
        if tutorial:
            tempo = 2
        else:
            tempo = 1
        scream('CUIDADO')
        time.sleep(2)
        t1 = threading.Thread(target=self.player_moves)
        t2 = threading.Thread(target=self.dodge_trap, args=(tempo,))
        t1.start()
        t2.start()
        t2.join()
        print('Presiona enter para continuar')
        t1.join()
        slow_print(f"Te pegaron {self.damage} piedras!")
        if not tutorial:
            if self.damage >= 1:
                slow_print(f'Perdiste {10 * self.damage - player.shield_lvl * 3} de vida')
                player.receive_damage(10 * self.damage, player.shield_lvl * 3)
            else:
                slow_print('Lograste salir ileso, que molestos son esos duendes.')


    def voice_trap(self, player):
        choice = False
        slow_print('Vas caminando cuando escuchas una voz que te habla...')
        slow_talk('FRENTE A TI ENCONTRARÁS UN REGALO, TÓMALO')
        time.sleep(2)
        slow_print('La voz sonaba un poco sospechosa...')
        while choice not in ['1', '2']:
            choice = input('Decide:\n1)Mejor continuar tu camino\n2)Tomar regalo')
        if choice == '1':
            slow_print('Continuas tu camino ignorando la voz.')
        else:
            print(".", end="\r")
            time.sleep(1)
            print("..", end="\r")
            time.sleep(1)
            print("...", end="\r")
            time.sleep(1)
            luck = random.randint(1, 5)
            if luck == 5:
                slow_print('Encuentras una posión de vida y decides beberla.')
                vida = player.health
                player.receive_damage(0, 30)
                if vida < player.health:
                    slow_print(f'Has ganado {player.health - vida} de vida.')
                else:
                    slow_print('Nada sucede.')
            else:
                slow_print('Encuentras una posión de vida y decides beberla.')
                slow_print('Inmediatamente te das cuenta que cometiste un error.')
                vida = player.health
                player.receive_damage(10, 0)
                slow_print(f'Pierdes {vida - player.health} de vida')
