from src.utils.functions import slow_print, slow_talk, scream
import time
import json
import random


# Filling each group
def load_questions(path):
    with open(path, "r") as que_file:
        questions = json.load(que_file)
    return questions


def get_question(preguntas, grp):
    question = random.choice(list(preguntas[grp].keys()))
    options = preguntas[grp][question]
    return question, options


def mix_choice(options):
    return random.sample(list(options), 4)


def modify_objects(player, group):
    if group == 1:
        slow_talk('-Eres tan inculto que pierdes todos tus objetos.')
        for _ in range(3):
            player.shield_down()
            player.sword_down()
            player.gun_down()
        return 0
    elif group < 5:
        damage = 20 - 5 * (group - 2)
        magic_damage = 10 + damage
        vida = player.health
        player.receive_damage(damage, 0)
        slow_talk('-Me haces enfurecer con tu poco conocimiento.')
        slow_print(f'Te dispara una flecha al estomago.\nPierdes {vida - player.health} de vida.')
        if player.magic >= magic_damage:
            player.magic -= magic_damage
        else:
            player.magic = 0
        return 0

    elif group == 5:
        slow_talk('Casi logras tener 5 respuestas correctas. ¿Qué objeto quieres que mejore para ti?')
        opciones_mejora = []
        if player.sword_lvl < 3:
            opciones_mejora.append('Espada')
        if player.gun_lvl < 3:
            opciones_mejora.append('Revolver')
        if player.shield_lvl < 3:
            opciones_mejora.append('Escudo')
        if not len(opciones_mejora):
            slow_talk('-Veo que ya tienes todo mejorado al máximo, tal vez para la otra.')
            return 1

        mejora = ''
        while mejora not in opciones_mejora:
            for x in opciones_mejora:
                print(x, end='    ')
            mejora = input().capitalize()
        if mejora == 'Espada':
            player.sword_up()
        elif mejora == 'Revolver':
            player.gun_up()
        elif mejora == 'Escudo':
            player.shield_up()

        return 1
    else:
        slow_talk('-Me pusiste de buen humor, mejoraré todos tus objetos')
        player.shield_up()
        player.sword_up()
        player.gun_up()
        return 1


def play(player, tutorial):
    group = 1
    turn = 1
    option_names = ['a)', 'b)', 'c)', 'd)']
    questions = load_questions('preguntas_examen.json')
    while turn < 6:
        player_choice = ''
        real_answers = {}
        if tutorial:
            question, ans_options = get_question(questions, 'g1')
        else:
            question, ans_options = get_question(questions, f'g{group}')
        mixed_options = mix_choice(ans_options.keys())
        slow_print(f'{turn}.-{question}')
        time.sleep(1)
        for name, option in zip(option_names, mixed_options):
            real_answers[name] = ans_options[option]
            print(name, option, end='\r')
            time.sleep(0.5)
        while player_choice not in option_names:
            player_choice = input().lower() + ')'
        if real_answers[player_choice]:
            slow_print('Respuesta correcta.')
            group += 1
        else:
            scream('Incorrecto')
        turn += 1
    slow_print(f'Tuviste {group - 1} respuestas correctas')

    if not tutorial:
        return modify_objects(player, group)
