from characters import Warrior,Goblin

stop_function=False
options=[]
full_options=['Huir','Escudo mágico','Lanzar hechizo','Disparar','Recargar','Atacar con espada','Usar escudo','Hechizo prohibido']

def fill_options(player,enemy):
    global options
    options=[]
    if isinstance(enemy,Goblin):
        options.append('Huir')
    if player.magic_shiel:
        options.append('Escudo mágico')
    if player.magic_staff:
        options.append('Lanzar hechizo')
    if player.gun_lvl>0:
        if player.bullets>0
            options.append('Disparar')
        if player.bullets<player.max_bullets:
            options.append('Regargar')
    if player.sword_lvl>0:
        options.append('Atacar con espada')
    if player.shield_lvl>0:
        options.append('Usar escudo')
    if player.super_pow:
        options.append('Hechizo prohibido')
        
def action(player,move,enemy,enemy_move):
    global stop_function
    if move==0:
        if player.escape():
            print('Haz logrado escapar!')
            stop_function=True
        else:
            print('Te tropiezas y quedas indefenzo')
            if enemy_move==5:
                player.receive_damage(3,0)
    elif move==1:
        if enemy_move==1:
            player.charge_shield()
            enemy.charge_shield()
        elif enemy_move==
    elif move==2:
    elif move==3:
    elif move==4:
    elif move==5:
    elif move==6:
    else:

def goblin_duel(player,goblin):
    global stop_function
    stop_function=False
    while player.is_alive() and goblin.is_alive():
        if stop_function:
            break
        player_choice=''
        goblin_choice=goblin.move()
        while player_choice not in options:
            print('Que decides hacer?')
            for x in options:
                if not options.index(x)%2:
                    print(x, end=' '*(25-len(x)))
                else:
                    print(x)
            player_choice=input()
        action(player,full_options.index(player_choice),goblin,goblin_choice)
        time.sleep(3)
        if stop_function:
            break