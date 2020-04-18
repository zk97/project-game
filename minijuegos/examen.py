import time
import random
import juego

turn=5
group=1
choice=['a)','b)','c)','d)']
#Group of questions
q1=[]
q2=[]
q3=[]
q4=[]
q5=[]

#Filling each group
def fill_q():
    global q1,q2,q3,q4,q5

    q1=[]
    question1=open('../minijuegos/preg1.txt','r',encoding='utf8')
    for _ in range(0,41):
        q1.append([question1.readline() for _ in range(1,6)])

    q2=[]
    question2=open('../minijuegos/preg2.txt','r',encoding='utf8')
    for _ in range(0,42):
        q2.append([question2.readline() for _ in range(1,6)])

    q3=[]
    question3=open('../minijuegos/preg3.txt','r',encoding='utf8')
    for _ in range(0,45):
        q3.append([question3.readline() for _ in range(1,6)])

    q4=[]
    question4=open('../minijuegos/preg4.txt','r',encoding='utf8')
    for _ in range(0,42):
        q4.append([question4.readline() for _ in range(1,6)])

    q5=[]
    question5=open('../minijuegos/preg5.txt','r',encoding='utf8')
    for _ in range(0,39):
        q5.append([question5.readline() for _ in range(1,6)])
        
def mix_choice():
    global choice
    choice=['a)','b)','c)','d)']
    choice=random.sample(choice,4)
    
def get_question(grp):
    return random.sample(grp,1)
    
def play(player):
    global group,turn
    group=1
    turn=5
    ordered_options=[]
    fill_q()
    while turn>0:
        player_choice=''
        if group==1:
            ask=get_question(q1)[0]
        if group==2:
            ask=get_question(q2)[0]
        if group==3:
            ask=get_question(q3)[0]
        if group==4:
            ask=get_question(q4)[0]
        if group==5:
            ask=get_question(q5)[0]
        mix_choice()
        ordered_options=sorted([choice[i]+ask[i+1] for i in range(4)])
        juego.slow_print('{}.-{}'.format(6-turn,ask[0]))
        time.sleep(1)
        for x in ordered_options:
            print(x,end='\r')
        while player_choice not in choice:
            player_choice=input()+')'
        if player_choice==choice[0]:
            juego.slow_print('Respuesta correcta.')
            group+=1
        else:
            juego.scream('Incorrecto')
        turn-=1
    juego.slow_print('Tiviste {} respuestas correctas'.format(group-1))
    if group>4:
        if group>5:
            juego.slow_talk('-Me pusiste de buen humor, mejoraré todos tus objetos')
            player.shield_up()
            player.sword_up()
            player.gun_up()
        else:
            juego.slow_talk('Casi logras tener 5 respuestas correctas. ¿Qué objeto quieres que mejore para ti?')
            cosas=[]
            if player.sword_lvl<3:
                cosas.append('Espada')
            if player.gun_lvl<3:
                cosas.append('Revolver')
            if player.shield_lvl<3:
                cosas.append('Escudo')
            if not len(cosas):
                cosas.append('Nada')
            cosa=''
            while cosa not in cosas:
                for x in cosas:
                    print(x, end='    ')
                cosa=input().capitalize()
            if cosa=='Espada':
                player.sword_up()
            elif cosa=='Revolver':
                player.gun_up()
            elif cosa=='Escudo':
                player.shield_up()
            else:
                juego.slow_talk('-Veo que ya tienes todo mejorado al máximo, tal vez para la otra.')
        return 1
    else:
        if group>1:
            vida = player.health
            player.receive_damage(20,0)
            juego.slow_talk('-Me haces enfurecer con tu poco conocimiento.')
            juego.slow_print('Te dispara una flecha al estomago.\nPierdes {} de vida.'.format(vida-player.health))
            if player.magic>=30:
                player.magic-=30
            else:
                player.magic=0
        else:
            juego.slow_talk('-Eres tan inculto que pierdes todos tus objetos.')
            for _ in range(3):
                player.shield_down()
                player.sword_down()
                player.gun_down()
        return 0
        
    