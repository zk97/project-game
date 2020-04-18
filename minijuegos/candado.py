import random
import time
import juego

NUMBER=0
ROUND=0



def ask_player():
    answer=-1
    while answer not in range(0,10000) or len(list_answer)!=4:
        juego.slow_print('¿Con qué número quieres tratar?')
        answer=input()
        list_answer=[x for x in answer]
        answer=int(answer)
    return answer

def compare(guess,real):
    right_place=0
    wrong_place=0
    list_guess=[x for x in str(guess)]
    list_real=[x for x in str(real)]
    while len(list_guess)<4:
        list_guess.insert(0,'0')
    while len(list_real)<4:
        list_real.insert(0,'0')
    #Check for right numbers in right place
    for i in range(4):
        if list_guess[i]==list_real[i]:
            right_place+=1
            list_guess[i]='z'
            list_real[i]='g'
    #Check for remaining right numbers
    for i in list_guess:
        if i in list_real:
            wrong_place+=1
            list_real.remove(i)
    if right_place==0:
        if wrong_place==0:
            juego.slow_print("Todos los números son incorrectos.")
        else:
            juego.slow_print("{} números son correctos pero están en la posición equivocada.".format(wrong_place))
    else:
        if wrong_place==0:
            juego.slow_print("{} números son correctos y están en el lugar correcto.".format(right_place))
        else:
            juego.slow_print("{} números son correctos y están en el lugar correcto, {} números son correctos pero están en la posición equivocada.".format(right_place,wrong_place))
    time.sleep(2)
    
def play(player):
    number=random.randint(0,9999)
    num_round=0
    player_guess=-1
    choice=0
    while player_guess!=number and num_round<7:
        player_guess=ask_player()
        compare(player_guess,number)
        num_round+=1
    if player_guess!=number:
        juego.slow_print('Te quedaste si oportunidades.')
        if player.magic>=25:
            while choice not in ['1','2']:
                choice=input('¿Deseas sacrificar magia para restaurar el candado?\n1)Si\n2)No')
            choice=int(choice)
            if choice:
                player.magic-=25
                while player_guess!=number and num_round<10:
                    player_guess=ask_player()
                    compare(player_guess,number)
                    num_round+=1
            else:
                juego.slow_print("No lograste abrir el candado.")
                player.receive_damage(15,0)
            return 0
        else:
            juego.slow_print("No lograste abrir el candado.")
            player.receive_damage(15,0)
            return 0
    if num_round==10:
        juego.slow_print("No lograste descifrar la combinación.")
        player.receive_damage(15,0)
        return 0
    else:
        juego.slow_print("El candado se abre y puedes cruzar.")
        if num_round<7:
            player.receive_damage(0,20)
        return 1
        