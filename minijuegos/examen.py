import time
import random

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
        print('{}.-{}'.format(6-turn,ask[0]),end='\r')
        time.sleep(2)
        for x in ordered_options:
            print(x,end='\r')
        while player_choice not in choice:
            player_choice=input()+')'
        if player_choice==choice[0]:
            print('Correcto!')
            group+=1
        else:
            print('Incorrecto')
        turn-=1
    print('Tiviste {} respuestas correctas'.format(group-1))
    if group>4:
        return 1
    else:
        return 0
        
    