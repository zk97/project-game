from characters import Warrior,Goblin

stop_function=False
options=[]
full_options=['Huir','Escudo mágico','Lanzar hechizo','Disparar','Recargar','Atacar con espada','Usar escudo','Hechizo prohibido']

def fill_options(player,enemy):
    global options
    options=[]
    if isinstance(player,Goblin):
        options.append('Atacar con espada')
        options.append('Usar escudo')
    else:
        if isinstance(enemy,Goblin):
            options.append('Huir')
        if player.magic_shiel:
            options.append('Escudo mágico')
        if player.magic_staff and player.magic>player.magic_cost:
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
    if player.stunned:
        if enemy.stunned:
            enemy.stun_change()
        elif enemy_move==1:
            enemy.charge_shield()
        elif enemy_move==2:
            playe.receive_damage(enemy.spell(),0)
        elif enemy_move==3:
            player.receive_damage(enemy.shoot(),0)
        elif enemy_move==4:
            enemy.recharge()
            enemy.recharge()
        elif enemy_move==5:
            player.receive_damage(enemy.attack(),0)
        elif enemy_move==6:
            pass
        else:
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.final_spell()
        player.stun_change()
    elif move==0:
        if player.escape():
            print('Haz logrado escapar!')
            stop_function=True
        else:
            print('Te tropiezas y quedas indefenzo')
            if enemy_move==5:
                player.receive_damage(3,0)
    elif move==1:
        if enemy.stunned:
            player.charge_shield()
            enemy.stun_change()
        elif enemy_move==1:
            player.charge_shield()
            enemy.charge_shield()
        elif enemy_move==2:
            player.charge_shield()
            player.receive_damage(enemy.spell(),(player.magic_lvl**2)*5)
        elif enemy_move==3:
            player.receive_damage(enemy.shoot(),0)
        elif enemy_move==4:
            player.charge_shield()
            enemy.recharge()
            enemy.recharge()
        elif enemy_move==5:
            player.receive_damage(enemy.attack(),0)
        elif enemy_move==6:
            player.charge_shield()
        else:
            enemy.receive_damage(enemy.health,0)
            enemy.final_spell()
    elif move==2:
        if enemy.stunned:
            enemy.receive_damage(player.spell(),0)
            enemy.stun_change()
        elif enemy_move==1:
            enemy.charge_shield()
            enemy.receive_damage(player.spell(),20)
        elif enemy_move==2:
            enemy.receive_damage(player.spell(),0)
            player.receive_damage(enemy.spell(),0)
        elif enemy_move==3:
            enemy.receive_damage(player.spell(),0)
        elif enemy_move==4:
            enemy.receive_damage(player.spell(),0)
        elif enemy_move==5:
            enemy.receive_damage(player.spell(),0)
        elif enemy_move==6:
            enemy.receive_damage(player.spell(),5)
        else:
            enemy.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.final_spell()
    elif move==3:
        if enemy.stunned:
            enemy.receive_damage(player.shoot(),0)
            enemy.stun_change()
        elif enemy_move==1:
            enemy.receive_damage(player.shoot(),0)
        elif enemy_move==2:
            player.receive_damage(enemy.shoot(),0)
        elif enemy_move==3:
            enemy.receive_damage(player.shoot(),0)
            player.receive_damage(enemy.shoot(),0)
        elif enemy_move==4:
            enemy.receive_damage(player.shoot(),0)
        elif enemy_move==5:
            enemy.receive_damage(player.shoot(),0)
            player.receive_damage(enemy.attack(),0)
        elif enemy_move==6:
            if player.gun_lvl==3:
                enemy.receive_damage(player.shoot(),10)
            else:
                enemy.receive_damage(player.shoot(),player.gun_dmg)
        else:
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.final_spell()
    elif move==4:
        if enemy.stunned:
            player.recharge()
            player.recharge()
            enemy.stun_change()
        elif enemy_move==1:
            enemy.charge_shield()
            player.recharge()
            player.recharge()
        elif enemy_move==2:
            player.receive_damage(enemy.spell(),0)
        elif enemy_move==3:
            player.receive_damage(enemy.shoot(),0)
        elif enemy_move==4:
            player.recharge()
            player.recharge()
            enemy.recharge()
            enemy.recharge()
        elif enemy_move==5:
            player.receive_damage(enemy.attack(),0)
            player.recharge()
        elif enemy_move==6:
            player.recharge()
            player.recharge()
        else:
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
    elif move==5:
        if enemy.stunned:
            enemy.receive_damage(player.attack(),0)
            enemy.stun_change()
        elif enemy_move==1:
            enemy.receive_damage(player.attack(),0)
        elif enemy_move==2:
            player.receive_damage(enemy.spell(),0)
        elif enemy_move==3:
            enemy.receive_damage(player.attack(),0)
            player.receive_damage(enemy.shoot(),0)
        elif enemy_move==4:
            enemy.receive_damage(player.attack(),0)
            enemy.recharge()
        elif enemy_move==5:
            if player.sword_lvl==1:
                player.receive_damage(10,0)
            elif player.sword_lvl==3:
            enemy.receive_damage(10,0)
            else:
                pass
        elif enemy_move==6:
            enemy.receive_damage(player.attack(),player.sword_lvl*5)
            player.stun_change()
        else:
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
    elif move==6:
        if enemy.stunned:
            enemy.stun_change()
        elif enemy_move==1:
            enemy.charge_shield()
        elif enemy_move==2:
            player.receive_damage(enemy.spell(),5*(player.shield_lvl-1))
        elif enemy_move==3:
            if player.shield_lvl==1:
            player.receive_damage(enemy.shoot(),5)
            else:
                player.receive_damage(enemy.shoot(),enemy.gun_dmg)
        elif enemy_move==4:
            enemy.recharge()
            enemy.recharge()
        elif enemy_move==5:
            player.receive_damage(enemy.attack(),player.shield_lvl*5)
            enemy.stun_chage()
        elif enemy_move==6:
            pass
        else:
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
    else:   
        if enemy_move==1:
            enemy.receive_damage(30,0)
            enemy.shield_break()
        else:
            enemy.receive_damage(enemy.health,0)

def duel(player,enemy):
    global stop_function
    stop_function=False
    player_health=player.health
    enemy_health=enemy.health
    while player.is_alive() and enemy.is_alive():
        if stop_function:
            break
        player_choice=''
        fill_options(enemy,player)
        enemy_choice=enemy.move(options)
        fill_options(player,enemy)
        while player_choice not in options:
            print('Que decides hacer?')
            for x in options:
                if not options.index(x)%2:
                    print(x, end=' '*(25-len(x)))
                else:
                    print(x)
            player_choice=input()
        action(player,full_options.index(player_choice),enemy,full_options.index(enemy_choice))
        time.sleep(3)
        if player_health>player.health:
            print('Perdiste {} de vida'.format(player_health-player.health))
        elif player_health<player.health:
            print('Ganaste {} de vida'.format(player.health-player_health))
        if enemy_health>enemy.health:
            print('El enemigo perdio {} de vida'.format(enemy_health-enemy.health))
        elif enemy_health<enemy.health:
            print('El enemigo gano {} de vida'.format(enemy.health-enemy_health))
    if player.is_alive():
        print('Venciste')
    else:
        print('Perdiste')
    