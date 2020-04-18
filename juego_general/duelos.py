from characters import Warrior,Goblin
import time
import juego

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
        if player.super_pow and player.health<=25:
            options.append('Hechizo prohibido')

def action(player,move,enemy,enemy_move):
    global stop_function
    if player.stunned:
        if enemy.stunned:
            enemy.stun_change()
            juego.slow_print('Ambos están aturdidos.')
        elif enemy_move==1:
            enemy.charge_shield()
            juego.slow_print('Tu rival aprovecha para cargar magia.')
        elif enemy_move==2:
            player.receive_damage(enemy.spell()*1.5,0)
            juego.slow_print('No puedes evitar que te lancen un hechizo.')
        elif enemy_move==3:
            player.receive_damage(enemy.shoot()*1.5,0)
            juego.slow_print('Crees escuchar un disparo y sientes un ardor en el pecho.')
        elif enemy_move==4:
            enemy.recharge()
            enemy.recharge()
            juego.slow_print('Esuchas como tu rival aprovecha para cargar su arma.')
        elif enemy_move==5:
            player.receive_damage(enemy.attack()*1.5,0)
            juego.slow_print('Sientes el corte de la espada en un costado.')
        elif enemy_move==6:
            juego.slow_print('Tu rival decidió cubrirse con su escudo...\n ¿Se está burlando de ti?')
        else:
            juego.slow_talk('-Prepárate para ver mi poder, por algo soy el elegido.')
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.final_spell()
            juego.slow_print('El hechizo sale defectuozo.')
        player.stun_change()
    elif move==0:
        if player.escape():
            juego.slow_print('Haz logrado escapar!')
            stop_function=True
        else:
            juego.slow_print('Te tropiezas y quedas indefenzo.')
            if enemy_move==5:
                player.receive_damage(3,0)
                juego.slow_print('El duende aprovecha para clavarte su daga.')
            else:
                juego.slow_print('El duende se cubrió.\nParece que está confundido con lo que pasó.')
    elif move==1:
        if enemy.stunned:
            player.charge_shield()
            juego.slow_print('Aprovechas que tu enemigo está aturdido para cargar tus reservas de magia.')
            enemy.stun_change()
        elif enemy_move==1:
            player.charge_shield()
            enemy.charge_shield()
            juego.slow_print('Ambos usan su escudo mágico y recuperan un poco de magia.')
        elif enemy_move==2:
            player.charge_shield()
            player.receive_damage(enemy.spell(),(player.magic_lvl**2)*5)
            juego.slow_print('Reaccionas a tiempo y usas tu escudo mágico para cubrirte del hechizo que viene en tu camino.')
        elif enemy_move==3:
            player.receive_damage(enemy.shoot(),0)
            juego.slow_print('El escudo mágico no es buena protección contra la bala que acaba de golpearte.')
        elif enemy_move==4:
            juego.slow_print('Mientras tu cargas tus niveles de magia, ves como tu rival aprovecha para cargar su arma.')
            player.charge_shield()
            enemy.recharge()
            enemy.recharge()
        elif enemy_move==5:
            player.receive_damage(enemy.attack(),0)
            juego.slow_print('Parece que te protegiste de la manera equivocada, el acero de la espada hace un corte limpio.')
        elif enemy_move==6:
            player.charge_shield()
            juego.slow_print('Haces que tu enemigo se cubra con su escudo y mientras tu recuperas magia perdida.')
        else:
            juego.slow_talk('-Prepárate para ver mi poder, por algo soy el elegido.')
            juego.slow_print('Reaccionas lo más rápido posible y te cubres.\n El hechizo rebota y ves cómo pega en el blanco.')
            enemy.receive_damage(enemy.health,0)
            enemy.final_spell()
    elif move==2:
        if enemy.stunned:
            juego.slow_print('Con tu rival incapaz de moverse lanzas un hechizo que pega en el blanco.')
            enemy.receive_damage(player.spell()*1.5,0)
            enemy.stun_change()
        elif enemy_move==1:
            juego.slow_print('Era buena tu intención pero tu adversario alcanza a cubrirse.')
            enemy.charge_shield()
            enemy.receive_damage(player.spell(),(enemy.magic_lvl**2)*5)
        elif enemy_move==2:
            juego.slow_talk('-Mi magia es más poderoza que la tuya.')
            juego.slow_print('Cada hechizo golpea de lleno en el contrario.')
            enemy.receive_damage(player.spell(),0)
            player.receive_damage(enemy.spell(),0)
        elif enemy_move==3:
            juego.slow_print('Tu hechizo te cubre del disparo rival y causa daño en tu oponente.')
            enemy.receive_damage(player.spell(),0)
            player.receive_damage(enemy.shoot(),enemy.gun_dmg)
        elif enemy_move==4:
            juego.slow_print('Antes de que tu rival logre cargar su arma lanzas un hechizo que da en el blanco.')
            enemy.receive_damage(player.spell(),0)
        elif enemy_move==5:
            juego.slow_print('Tu rival trata de atacarte cuerpo a cuerpo pero mantienes tu distancia y das en el blanco.')
            enemy.receive_damage(player.spell(),0)
        elif enemy_move==6:
            if isinstance(enemy,Goblin):
                enemy.receive_damage(player.spell(),2)
                juego.slow_print('El duende trata de cubrirse tu hechizo con su escudo.')
            else:
                enemy.receive_damage(player.spell(),enemy.shield_lvl**2)
                juego.slow_print('Tu rival trata de usar su escudo para cubrir tu hechizo.')
        else:
            juego.slow_talk('-Prepárate para ver mi poder, por algo soy el elegido.')
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.final_spell()
            juego.slow_print('El hechizo sale defectuozo.')
    elif move==3:
        if enemy.stunned:
            juego.slow_print('Tu oponente aturdido es un blanco facil, sin mucho problema das en el blanco.')
            enemy.receive_damage(player.shoot()*1.5,0)
            enemy.stun_change()
        elif enemy_move==1:
            juego.slow_print('Ese escudo mágico no lo cubre de tu bala, que acierta sin problemas.')
            enemy.receive_damage(player.shoot(),0)
        elif enemy_move==2:
            juego.slow_print('El disparo se ve deviado por su hechizo que no logras evitar.')
            player.receive_damage(enemy.spell(),0)
            enemy.receive_damage(player.shoot(),player.gun_dmg)
        elif enemy_move==3:
            juego.slow_print('Disparan a la vez y ambos dan en el blanco.')
            enemy.receive_damage(player.shoot(),0)
            player.receive_damage(enemy.shoot(),0)
        elif enemy_move==4:
            juego.slow_print('Notas que quiere recargar y sin darle oportunidad aprietas el gatillo.')
            enemy.receive_damage(player.shoot(),0)
        elif enemy_move==5:
            juego.slow_print('Disparas en cuanto lo ves venir, pero eso no lo frena lo suficiente y alcanza a atacar.')
            enemy.receive_damage(player.shoot(),0)
            player.receive_damage(enemy.attack(),0)
        elif enemy_move==6:
            if isinstance(enemy,Goblin):
                enemy.receive_damage(player.shoot(),2)
                juego.slow_print('De algo debe ayudar ese escudo contra tu bala.')
            elif player.gun_lvl>enemy.shield_lvl:
                juego.slow_print('Tu rival logra evitar algo del daño al cubrirse.')
                enemy.receive_damage(player.shoot(),5*enemy.shield_lvl)
            else:
                juego.slow_print('El escudo de tu oponente parece demasiado resistente, no creo que le hicieras daño.')
                enemy.receive_damage(player.shoot(),player.gun_dmg)
        else:
            juego.slow_talk('-Prepárate para ver mi poder, por algo soy el elegido.')
            juego.slow_print('Tratas de disparar antes de que pueda hacer algo pero no eres tan rápido y tu bala se desvía.')
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.receive_damage(player.shoot(),player.gun_dmg)
            enemy.final_spell()
            juego.slow_print('El hechizo sale defectuozo.')
    elif move==4:
        if enemy.stunned:
            juego.slow_print('Aprovehcas este tiempo para recargar.')
            player.recharge()
            player.recharge()
            enemy.stun_change()
        elif enemy_move==1:
            juego.slow_print('Mientras tu cargas tu arma tu rival decide recuperar algo de magia.')
            enemy.charge_shield()
            player.recharge()
            player.recharge()
        elif enemy_move==2:
            juego.slow_print('Tratas de recargar pero apenas te mueves un poco y un hechizo te manda a volar.')
            player.receive_damage(enemy.spell(),0)
        elif enemy_move==3:
            juego.slow_print('Ni tiempo te dio de moverte cuando una bala golpeó tu hombro.')
            player.receive_damage(enemy.shoot(),0)
        elif enemy_move==4:
            juego.slow_print('Hacen un pacto de no atacar y ambos cargan sus armas.')
            player.recharge()
            player.recharge()
            enemy.recharge()
            enemy.recharge()
        elif enemy_move==5:
            juego.slow_print('Apenas ibas a cargar la segunda bala cuando te alcanza tu rival y hace un corte en tu brazo.')
            player.receive_damage(enemy.attack(),0)
            player.recharge()
        elif enemy_move==6:
            juego.slow_print('Logras hacer que tu oponente se cubra y aprovechas para recargar.')
            player.recharge()
            player.recharge()
        else:
            juego.slow_talk('-Prepárate para ver mi poder, por algo soy el elegido.')
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.final_spell()
            juego.slow_print('El hechizo sale defectuozo.')
    elif move==5:
        if enemy.stunned:
            juego.slow_print('Mientras tu oponente está aturdido atacas con tu espada.')
            enemy.receive_damage(player.attack()*1.5,0)
            enemy.stun_change()
        elif enemy_move==1:
            juego.slow_print('El escudo mágico no sirve de nada contra el filo de tu espada')
            enemy.receive_damage(player.attack(),0)
        elif enemy_move==2:
            player.receive_damage(enemy.spell(),0)
            juego.slow_print('Estás decidido a atacar pero en cuento te acercas el hechizo de tu rival te pega y te lanza hacia atrás.')
        elif enemy_move==3:
            enemy.receive_damage(player.attack(),0)
            player.receive_damage(enemy.shoot(),0)
            juego.slow_print('Vas hacia adelante, tu oponente dispara y da en tu pierna izquierda pero logras hacer un corte en su costado.')
        elif enemy_move==4:
            enemy.receive_damage(player.attack(),0)
            enemy.recharge()
            juego.slow_print('Alcanzas a evitar que cargue una segunda vala haciendo un corte profundo.')
        elif enemy_move==5:
            if isinstance(enemy,Goblin):
                enemy.receive_damage(8*player.sword_lvl-4,0)
                juego.slow_print('El duende trata de atacar con su daga pero logras desarmarlo y devuelves el ataque.')
            elif player.sword_lvl<enemy.sword_lvl:
                player.receive_damage(10*(enemy.sword_lvl-player.sword_lvl),0)
                juego.slow_print('Después de un breve compate espada contra espada, la experiencia de tu rival le permitión golpear tu pecho.')
                
            elif player.sword_lvl>enemy.sword_lvl:
                enemy.receive_damage(10*(player.sword_lvl-enemy.sword_lvl),0)
                juego.slow_print('Hay un duelo de espadas durante un momento pero finalmente tu ataque es el que logra conectar.')
            else:
                juego.slow_print('Ambos atacan con espadas pero después de un pequeño duelo sin resultados se retiran un poco.')
        elif enemy_move==6:
            if isinstance(enemy,Goblin):
                enemy.receive_damage(player.attack(),2)
                juego.slow_print('Tu espada golpea contra el escudo del duende.')
            elif player.attack()>enemy.shield_lvl*5:
                enemy.receive_damage(player.attack(),enemy.shield_lvl*5)
                juego.slow_print('Tu rival se cubre con su escudo pero lograste hacer daño.')
            else:
                juego.slow_print('Atacas con fuerza pero el escudo de tu oponente es increiblemente fuerte.')
            player.stun_change()
            juego.slow_print('Golpear directo contra el escudo te deja aturdido.')
        else:
            juego.slow_talk('-Prepárate para ver mi poder, por algo soy el elegido.')
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.final_spell()
            juego.slow_print('El hechizo sale defectuozo.')
    elif move==6:
        if enemy.stunned:
            enemy.stun_change()
            juego.slow_print('Te cubres mientras tu oponente está aturdido. No sabes si se dio cuenta de que te burlas de él.')
        elif enemy_move==1:
            enemy.charge_shield()
            juego.slow_print('Reaccionaste muy precipitadamente, tu rival logra recuperar un poco de magia.')
        elif enemy_move==2:
            juego.slow_print('Tus reflejos solo te permitieron cubrirte con tu escudo normal ante el hechizo que iba en camino.')
            player.receive_damage(enemy.spell(),player.shield_lvl**2)
        elif enemy_move==3:
            if enemy.gun_lvl>player.shield_lvl:
                player.receive_damage(enemy.shoot(),5*player.shield_lvl)
                juego.slow_print('Te cubres del disparo pero logra hacer algo de daño.')
            else:
                player.receive_damage(enemy.shoot(),enemy.gun_dmg)
                juego.slow_print('Tu escudo resiste sin problemas la bala que iba hacia ti.')
        elif enemy_move==4:
            enemy.recharge()
            enemy.recharge()
            juego.slow_print('Trataste de predecir el movimiento de tu rival, pero eso le dio tiempo de recargar tranquilamente su arma.')
        elif enemy_move==5:
            if enemy.attack()>player.shield_lvl*5:
                player.receive_damage(enemy.attack(),player.shield_lvl*5)
                juego.slow_print('Te cubres del ataque rival pero su espada hace algo de daño, logras aturdirlo.')
            else:
                juego.slow_print('Tu escudo es bastante resistente, aturdes a tu oponente y no sufres daño alguno.')
            enemy.stun_change()
        elif enemy_move==6:
            juego.slow_print('Ambos levantan sus respectivos escudos, están listos para continuar con el combate.')
        else:
            juego.slow_talk('-Prepárate para ver mi poder, por algo soy el elegido.')
            player.receive_damage(30,0)
            enemy.receive_damage(15,0)
            enemy.final_spell()
            juego.slow_print('El hechizo sale defectuozo.')
    else:   
        if enemy_move==1:
            juego.slow_print('Lanzas el hechizo prohibido que aprendiste pero tu oponente reacciona a tiempo y logra cubrirse.')
            juego.slow_print('Notas como su escudo mágico es destruido.')
            enemy.receive_damage(30,0)
            enemy.shield_break()
            player.final_spell()
        else:
            enemy.receive_damage(enemy.health,0)
            player.final_spell()
            juego.slow_print('Lanzas el hechizo prohibido que aprendiste y a tu rival le es imposible evitarlo.')

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
        enemy_choice=enemy.move(options)
        fill_options(player,enemy)
        if player.stunned:
            juego.slow_print('No puedes moverte este turno.')
            player_choice='Huir'
            time.sleep(1.5)
        else:
            while player_choice.lower() not in [x.lower() for x in options]:
                juego.slow_print('¿Qué decides hacer?')
                for x in options:
                    if not options.index(x)%2:
                        print(x, end=' '*(25-len(x)))
                    else:
                        print(x)
                player_choice=input()
        action(player,full_options.index(player_choice.lower()),enemy,full_options.index(enemy_choice.lower()))
        time.sleep(1.5)
        if player_health>player.health:
            juego.slow_print('Perdiste {} de vida'.format(player_health-player.health))
            player_health=player.health
        elif player_health<player.health:
            juego.slow_print('Ganaste {} de vida'.format(player.health-player_health))
            player_health=player.health
        if enemy_health>enemy.health:
            juego.slow_print('El enemigo perdio {} de vida'.format(enemy_health-enemy.health))
            enemy_health=enemy.health
        elif enemy_health<enemy.health:
            juego.slow_print('El enemigo gano {} de vida'.format(enemy.health-enemy_health))
            enemy_health=enemy.health
    if player.is_alive():
        juego.slow_print('Lograste salir vencedor de este enfrentamiento.')
        return 1
    else:
        if enemy.is_alive():
            juego.slow_print('Has sido derrotado.')
            return 0
        else:
            juego.slow_print('El combate ha terminado en empate.')
            return 2
    