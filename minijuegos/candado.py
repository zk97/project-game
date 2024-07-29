from utils.functions import slow_print
import random, time


def ask_player():
    answer=-1
    set_digit=set([str(x) for x in range(10)])
    while answer not in range(0,10000) or len(list_answer)!=4:
        set_answer=set('a')
        while not set_answer.issubset(set_digit):
            slow_print('¿Con qué combinación de cuatro dígitos quieres tratar?')
            answer=input()
            list_answer=[x for x in answer]
            set_answer=set(list_answer)
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
            slow_print("Todos los números son incorrectos.")
        else:
            slow_print("{} números son correctos pero están en la posición equivocada.".format(wrong_place))
    else:
        if wrong_place==0:
            slow_print("{} números son correctos y están en el lugar correcto.".format(right_place))
        else:
            slow_print("{} números son correctos y están en el lugar correcto, {} números son correctos pero están en la posición equivocada.".format(right_place,wrong_place))
    time.sleep(1)
    
def play(player,tutorial):
    number=random.randint(0,9999)
    num_round=0
    player_guess=-1
    choice=0
    if not tutorial:
        while player_gess!=number:
            player_guess=ask_player()
            compare(player_guess,number)
        slow_print('¡La clave introducida es correcta!')
    else:
        while player_guess!=number and num_round<7:
            slow_print('Intento #{}'.format(num_round+1))
            player_guess=ask_player()
            compare(player_guess,number)
            num_round+=1
        if player_guess!=number:
            slow_print('Parece ser que el candado dejó de funcionar es imposible meter una nueva combinación.')
            if player.magic>=25:
                while choice not in ['1','2']:
                    choice=input('¿Deseas sacrificar magia para restaurar el candado un poco?\n1)Si\n2)No')
                choice=int(choice)
                if choice:
                    player.magic-=25
                    while player_guess!=number and num_round<10:
                        slow_print('Usas no se qué pero ahora que lo pienso eso no toca ahorita jeje')
                        slow_print('Intento #{}'.format(num_round+1))
                        player_guess=ask_player()
                        compare(player_guess,number)
                        num_round+=1
                else:
                    slow_print("No lograste abrir el candado.")
                    player.receive_damage(15,0)
                return 0
            else:
                slow_print("No lograste abrir el candado.")
                player.receive_damage(15,0)
                return 0
        if num_round==10:
            slow_print("No lograste descifrar la combinación.")
            player.receive_damage(15,0)
            return 0
        else:
            slow_print("El candado se abre y puedes cruzar.")
            if num_round<7:
                player.receive_damage(0,20)
            return 1
        