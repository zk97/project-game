import random


class Warrior():
    def __init__(self,magic_lvl,gun_lvl,sword_lvl,shield_lvl,max_bull,magic_cost):
        self.magic_lvl=magic_lvl
        self.gun_lvl=gun_lvl
        self.sword_lvl=sword_lvl
        self.shield_lvl=shield_lvl
        self.max_bullets=max_bull
        self.magic_cost=magic_cost
        self.max_healt=100
        self.max_magic=100
        self.health=100
        self.magic=100
        self.gun_dmg=0
        self.magic_dmg=0
        self.sword_dmg=0
        self.bullets=0
        self.exp=0
        self.life_pot=0
        self.magic_pot=0
        self.boots=False
        self.super_pow=False
        self.stunned=True
        self.magic_shield=True
        self.magic_staff=True
        
    def shoot(self):
        self.bullets-=1
        return self.gum_dmg
        
    def spell(self):
        self.magic-=self.magic_cost
        return self.maigc_dmg
    
    def attack(self):
        return self.attack_dmg
        
    def drink_magic():
        self.magic+=50
        self.magic_pot-=1
        if self.magic>self.max_magic:
            self.magic=self.max_magic
    
    def heal(self):
        self.health+=50
        self.magic_pot-=1
        if self.health>self.max_health:
            self.health=self.max_health
            
    def recharge(self):
        self.bullets+=1
        if self.bullets>self.max_bull:
            self.bullets=self.max_bull
            
    def sword_up(self):
        self.sword_lvl+=1
        
    def sword_down(self):
        self.sword_lvl-=1
        
    def gun_up(self):
        self.gun_lvl+=1
        
    def gun_down(self):
        self.gun_lvl-=1
        
    def shiel_up(self):
        self.shield_lvl+=1
        
    def shield_down(self):
        self.shield_lvl-=1
            
    def magic_up(self):
        self.magic_lvl+=1
    
    def exp_up(self):
        self.exp+=1
    
    def new_boots(self):
        self.boots=True
        
    def super_power(self):
        self.super_pow=True
        
    def final_spell(self):
        self.super_pow=False
        
    def set_gun_dmg(self):
        self.gun_dmg=self.gun_lvl*5
        
    def set_sword_dmg(self):
        if self.sword_lvl==0:
            self.sword_dmg=0
        else:
            self.sword_dmg=10*self.sword_lvl-5
            
    def set_magic_dmg():
        if self.magic_lvl==3:
            self.magic_dmg=25
        else:
            self.magic_dmd=(self.magic_lvl+1)*5
        
    def receive_damage(self,damage):
        self.health-=damage
     
    def is_alive(self):
        return self.health>0
    
    def escape(self):
        if self.boots:
            return True
        elif random.randint(1,5)!=1:
            return True
        else:
            return False
        
    def charge_shield(self):
        self.magic+=self.magic_lvl*10
        if self.magic>self.max_magic:
            self.magi=self.max_magic 
        
    def receive_damage(self,damage,protection):
        self.healt-=(damage-protection)
            
    def stun_change(self):
        self.stunned = not self.stunned
        
    def shield_break(self):
        self.magic_shield=False
        
    def move(self,options):
        random.choice(options)
    
    
class Goblin():
    def __init__(self):
        self.health=15
        self.shield_lvl=5
        self.sword_lvl=5
        
    def receive_damage(self,damage,protection):
        self.health-=(damage-protection) 
        
    def attack(self):
        return 3
        
    def is_alive(self):
        return self.health>0
    #1 = attack, 0=defend
    def move(options):
        return random.choice(options)
        
