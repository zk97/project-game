import random
import time

NUMBER=0
ROUND=0



def ask_player():
    answer=0
    while answer not in range(1000,100000):
        answer=int(input('Con qué número quieres tratar?'))
    return answer

def compare(guess,real):
    right_place=0
    wrong_place=0
    list_guess=[x for x in str(guess)]
    list_real=[x for x in str(real)]
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
            print("Todos los números son incorrectos.")
        else:
            print("{} números son correctos pero están en la posición equivocada.".format(wrong_place))
    else:
        if wrong_place==0:
            print("{} números son correctos y están en el lugar correcto.".format(right_place))
        else:
            print("{} números son correctos y están en el lugar correcto, {} números son correctos pero están en la posición equivocada.".format(right_place,wrong_place))
    #time.sleep(2)
    
def try_to_unlock():
    number=random.randint(1000,9999)
    num_round=0
    player_guess=0
    choice=0
    while player_guess!=number and num_round<7:
        player_guess=ask_player()
        compare(player_guess,number)
        num_round+=1
    if player_guess!=number:
        while choice not in [1,2]:
            choice=int(input('Desea sacrificar magia?\n1)Si\n2)No'))
        if choice==1:
            while player_guess!=number and num_round<10:
                player_guess=ask_player()
                compare(player_guess,number)
                num_round+=1
        else:
            print("Perdiste")
            return None
    if num_round==10:
        print("Perdiste!")
    else:
        print("Ganaste!")
        