from src.utils.functions import slow_print, slow_talk
import random
import time
import json
import re


def load_riddles(path):
    with open(path, "r") as rid_file:
        riddles = json.load(rid_file)
    return riddles


def choose_riddle(riddles):
    return random.choice(list(riddles.items()))


def player_guess(player, answer):
    choice = False
    if player.magic >= 50:
        slow_print('Por 50 de magia puedes tratar de leer la mente de la esfinge si no sabes la respuesta.')
        while choice not in ['a', 'b']:
            choice = input("a)Contestar\nb)Leer mente").lower()
        if choice == 'b':
            player.magic -= 50
            slow_print("".join(answer))
    slow_print("¿Cuál es tu respuesta al acertijo?")


def play(player, tutorial):
    switch = False
    op = 2
    bet = 0
    if not tutorial:
        riddles = load_riddles('riddles_tutorial.json')
        rid, ans = choose_riddle(riddles)
        slow_print(rid)
        while not switch:
            slow_print("¿Cuál es tu respuesta al acertijo?\nPara ver la respuesta y salir escribe 'Salir'.")
            guess = input()
            if guess.lower() == 'salir':
                slow_print("La respuesta era '{}'.".format(ans[0].capitalize()))
                return None
            else:
                for i in ans:
                    if re.search(i, guess.lower()):
                        switch = True
                if not switch:
                    slow_talk('-¡Incorrecto!')
                    time.sleep(1.5)
        slow_talk('-Tu respuesta es correcta.')
        return None
    else:
        riddles = load_riddles('riddles.json')
        slow_print(
            "¿Por qué no hacemos ésto más interesante?\nSi ganas puedo mejorar tu espada, si aún no es de nivel 3.\nPero si pierdes la cambiaré por una peor, o te daré un mordisco si no tienes una.")
        while bet not in ['1', '2']:
            bet = input("1)Aceptas la apuesta\n2)No tienes interés")
        rid, ans = choose_riddle(riddles)
        slow_print(rid)
        while op > 0 and not switch:
            player_guess(player, ans[0])
            guess = input()
            for i in ans:
                if re.search(i, guess.lower()):
                    switch = True
            if not switch and op > 1:
                slow_talk('-¡Incorrecto! Te queda sólo una oportunidad.')
                time.sleep(2)
            elif not switch:
                op -= 1
        if op == 0:
            slow_talk('-No encontraste la respuesta al acertijo.')
            if bet == '1':
                if not player.sword_lvl:
                    vida = player.health
                    player.receive_damage(50, 0)
                    slow_print('La esfinge te suelta un mordisco que te quita {} de vida.'.format(vida - player.health))
                else:
                    player.sword_down()
            return 0
        else:
            slow_talk('-Tu respuesta es correcta.')
            if bet == '1':
                player.sword_up()
            return 1
