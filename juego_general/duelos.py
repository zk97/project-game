from characters import Warrior,Goblin
import time

stop_function=False
options=[]
full_options=['huir','escudo mágico','lanzar hechizo','disparar','recargar','atacar con espada','usar escudo','hechizo prohibido']

def fill_options(player,enemy):
    global options
    options=[]
    if isinstance(player,Goblin):
        options.append('Atacar con espada')
        options.append('Usar escudo')
    else:
        if isinstance(enemy,Goblin):
            options.append('Huir')
        if player.magic_shield:
            options.append('Escudo mágico')
        if player.magic_staff and player.magic>=player.magic_cost:
            options.append('Lanzar hechizo')
        if player.gun_lvl>0:
            if player.bullets>0:
                options.append('Disparar')
            if player.bullets<player.max_bullets:
                options.append('Recargar')
        if player.sword_lvl>0:
            options.append('Atacar con espada')
        if player.shield_lvl>0:
            options.append('Usar escudo')
        if player.super_pow:
            options.append('Hechizo prohibido')

def action(player,move,enemy,enemy_move):
    print(move,enemy_move,player.stunned)
    global stop_function
    if player.stunned:
        if enemy.stunned:
            enemy.stun_change()
        elif enemy_move==1:
            enemy.charge_shield()
        elif enemy_move==2:
            player.receive_damage(enemy.spell(),0)
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
            enemy.receive_damage(player.spell(),(enemy.magic_lvl**2)*5)
        elif enemy_move==2:
            enemy.receive_damage(player.spell(),0)
            player.receive_damage(enemy.spell(),0)
        elif enemy_move==3:
            enemy.receive_damage(player.spell(),0)
            player.receive_damage(enemy.shoot(),enemy.gun_dmg)
        elif enemy_move==4:
            enemy.receive_damage(player.spell(),0)
        elif enemy_move==5:
            enemy.receive_damage(player.spell(),0)
        elif enemy_move==6:
            if isinstance(enemy,Goblin):
                enemy.receive_damage(player.spell(),2)
            else:
                enemy.receive_damage(player.spell(),enemy.shield_lvl**2)
        else:
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.final_spell()
    elif move==3:
        if enemy.stunned:
            enemy.receive_damage(player.shoot(),0)
            enemy.stun_change()
        elif enemy_move==1:
            enemy.receive_damage(player.shoot(),0)
        elif enemy_move==2:
            player.receive_damage(enemy.spell(),0)
            enemy.receive_damage(player.shoot(),player.gun_dmg)
        elif enemy_move==3:
            enemy.receive_damage(player.shoot(),0)
            player.receive_damage(enemy.shoot(),0)
        elif enemy_move==4:
            enemy.receive_damage(player.shoot(),0)
        elif enemy_move==5:
            enemy.receive_damage(player.shoot(),0)
            player.receive_damage(enemy.attack(),0)
        elif enemy_move==6:
            if isinstance(enemy,Goblin):
                enemy.receive_damage(player.shoot(),2)
            elif player.gun_lvl>enemy.shield_lvl:
                enemy.receive_damage(player.shoot(),5*enemy.shield_lvl)
            else:
                enemy.receive_damage(player.shoot(),player.gun_dmg)
        else:
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.receive_damage(player.shoot(),player.gun_dmg)
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
            enemy.final_spell()
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
            if isinstance(enemy,Goblin):
                enemy.receive_damage(8*player.sword_lvl-4,0)
            elif player.sword_lvl<enemy.sword_lvl:
                player.receive_damage(10,0)
            elif player.sword_lvl>enemy.sword_lvl:
                enemy.receive_damage(10,0)
            else:
                pass
        elif enemy_move==6:
            if isinstance(enemy,Goblin):
                enemy.receive_damage(player.attack(),2)
            elif player.attack()>enemy.shield_lvl*5:
                enemy.receive_damage(player.attack(),enemy.shield_lvl*5)
            else:
                pass
            player.stun_change()
        else:
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.final_spell()
    elif move==6:
        if enemy.stunned:
            enemy.stun_change()
        elif enemy_move==1:
            enemy.charge_shield()
        elif enemy_move==2:
            player.receive_damage(enemy.spell(),player.shield_lvl**2)
        elif enemy_move==3:
            if enemy.gun_lvl>player.shield_lvl:
                player.receive_damage(enemy.shoot(),5*player.shield_lvl)
            else:
                player.receive_damage(enemy.shoot(),enemy.gun_dmg)
        elif enemy_move==4:
            enemy.recharge()
            enemy.recharge()
        elif enemy_move==5:
            if enemy.attack()>player.shield_lvl*5:
                player.receive_damage(enemy.attack(),player.shield_lvl*5)
            else:
                pass
            enemy.stun_change()
        elif enemy_move==6:
            pass
        else:
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.final_spell()
    else:   
        if enemy_move==1:
            enemy.receive_damage(30,0)
            enemy.shield_break()
            player.final_spell()
        else:
            enemy.receive_damage(enemy.health,0)
            player.final_spell()

def duel(player,enemy):
    global stop_function
    stop_function=False
    if isinstance(enemy,Warrior):
        enemy.set_warrior()
        if enemy.magic_lvl>=2:
            enemy.super_power()
    player_health=player.health
    enemy_health=enemy.health
    while player.is_alive() and enemy.is_alive():
        if stop_function:
            break
        player_choice=''
        fill_options(enemy,player)
        print(options)
        enemy_choice=enemy.move(options)
        print(options)
        fill_options(player,enemy)
        if player.stunned:
            print('No puedes moverte este turno')
            player_choice='Huir'
        else:
            while player_choice.lower() not in [x.lower() for x in options]:
                print('Que decides hacer?')
                for x in options:
                    if not options.index(x)%2:
                        print(x, end=' '*(25-len(x)))
                    else:
                        print(x)
                player_choice=input()
        action(player,full_options.index(player_choice.lower()),enemy,full_options.index(enemy_choice.lower()))
        #time.sleep(3)
        if player_health>player.health:
            print('Perdiste {} de vida'.format(player_health-player.health))
            player_health=player.health
        elif player_health<player.health:
            print('Ganaste {} de vida'.format(player.health-player_health))
            player_health=player.health
        if enemy_health>enemy.health:
            print('El enemigo perdio {} de vida'.format(enemy_health-enemy.health))
            enemy_health=enemy.health
        elif enemy_health<enemy.health:
            print('El enemigo gano {} de vida'.format(enemy.health-enemy_health))
            enemy_health=enemy.health
    if player.is_alive():
        print('Venciste')
        return 1
    else:
        if enemy.is_alive():
            print('Perdiste')
            return 0
        else:
            print('Empate')
            return 2
    