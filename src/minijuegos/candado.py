from src.utils.functions import slow_print
import random
import time


def ask_player():
    answer = ''
    set_digit = set('0123456789')
    while len(answer) != 4 or not set(answer).issubset(set_digit):
        slow_print('¿Con qué combinación de cuatro dígitos quieres tratar?')
        answer = input()
    return answer


def compare(guess, real):
    right_place = 0
    wrong_place = 0
    right_string = ''
    wrong_string = ''
    list_guess = list(guess)
    list_real = list(real)
    # Check for right numbers in right place
    for g, r in zip(guess, real):
        if g == r:
            right_place += 1
            list_guess.remove(g)
            list_real.remove(g)
    # Check for remaining right numbers
    for g in list_guess:
        if g in list_real:
            wrong_place += 1
            list_real.remove(g)

    if right_place:
        right_string = f"{right_place} números son correctos y están en el lugar correcto"
    if wrong_place:
        wrong_string = f"{wrong_place} números son correctos pero están en la posición equivocada"

    if not right_place and not wrong_place:
        slow_print("Todos los números son incorrectos.")
    else:
        slow_print(f"{right_string}, {wrong_string}".strip(' ,') + '.')

    time.sleep(1)


def play(player, tutorial):
    number = str(random.randint(0, 9999)).zfill(4)
    num_round = 0
    player_guess = -1
    choice = 0
    if tutorial:
        while player_guess != number:
            player_guess = ask_player()
            compare(player_guess, number)
        slow_print('¡La clave introducida es correcta!')
    else:
        while player_guess != number and num_round < 7:
            slow_print(f'Intento #{num_round + 1}')
            player_guess = ask_player()
            compare(player_guess, number)
            num_round += 1
        if player_guess != number:
            slow_print('Parece ser que el candado dejó de funcionar es imposible meter una nueva combinación.')
            if player.magic >= 25:
                while choice not in ['1', '2']:
                    choice = input('¿Deseas sacrificar magia para restaurar el candado un poco?\n1)Si\n2)No')
                if choice == '1':
                    player.magic -= 25
                    while player_guess != number and num_round < 10:
                        slow_print('Usas no se qué pero ahora que lo pienso eso no toca ahorita jeje')
                        slow_print('Intento #{}'.format(num_round + 1))
                        player_guess = ask_player()
                        compare(player_guess, number)
                        num_round += 1
                else:
                    slow_print("No lograste abrir el candado.")
                    player.receive_damage(15, 0)
                    return 0
            else:
                slow_print("No lograste abrir el candado.")
                player.receive_damage(15, 0)
                return 0
        if num_round == 10:
            slow_print("No lograste descifrar la combinación.")
            player.receive_damage(15, 0)
            return 0
        else:
            slow_print("El candado se abre y puedes cruzar.")
            if num_round < 7:
                player.receive_damage(0, 20)
            return 1
