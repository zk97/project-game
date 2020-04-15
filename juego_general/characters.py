import random


class Warrior():
    def __init__(self,magic_lvl,gun_lvl,sword_lvl,shield_lvl):
        self.magic_lvl=magic_lvl
        self.gun_lvl=gun_lvl
        self.sword_lvl=sword_lvl
        self.shield_lvl=shield_lvl
        self.max_health=100
        self.max_magic=100
        self.health=100
        self.magic=100
        self.max_bullets=0
        self.magic_cost=0
        self.gun_dmg=0
        self.magic_dmg=0
        self.sword_dmg=0
        self.bullets=0
        self.exp=0
        self.life_pot=0
        self.magic_pot=0
        self.boots=False
        self.super_pow=False
        self.stunned=False
        self.magic_shield=True
        self.magic_staff=True
        
    def shoot(self):
        self.bullets-=1
        return self.gun_dmg
        
    def spell(self):
        self.magic-=self.magic_cost
        return self.magic_dmg
    
    def attack(self):
        return self.sword_dmg
        
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
        if self.bullets>self.max_bullets:
            self.bullets=self.max_bullets
        print(self.bullets)
            
    def sword_up(self):
        if self.sword_lvl<3:
            self.sword_lvl+=1
            self.set_sword_dmg()
        
    def sword_down(self):
        if self.sword_lvl>0:
            self.sword_lvl-=1
            self.set_sword_dmg()
        
    def gun_up(self):
        if self.gun_lvl<3:
            self.gun_lvl+=1
            self.set_gun_dmg()
        
    def gun_down(self):
        if self.gun_lvl>0:
            self.gun_lvl-=1
            self.set_gun_dmg()
            self.set_max_bullets()
        
    def shiel_up(self):
        if self.shield_lvl<3:
            self.shield_lvl+=1
        
    def shield_down(self):
        if self.shield_lvl>0:
            self.shield_lvl-=1
            
    def magic_up(self):
        self.magic_lvl+=1
        self.set_magic_dmg()
        self.set_magic_cost()
    
    def exp_up(self):
        self.exp+=1
    
    def new_boots(self):
        self.boots=True
        
    def super_power(self):
        self.super_pow=True
        
    def final_spell(self):
        self.super_pow=False
        self.magic=0
        
    def set_gun_dmg(self):
        self.gun_dmg=self.gun_lvl*5
        
    def set_sword_dmg(self):
        if self.sword_lvl==0:
            self.sword_dmg=0
        else:
            self.sword_dmg=10*self.sword_lvl-5
            
    def set_magic_dmg(self):
        if self.magic_lvl==3:
            self.magic_dmg=25
        else:
            self.magic_dmg=(self.magic_lvl+1)*5
            
    def set_max_bullets(self):
        if not self.gun_lvl:
            self.max_bullets=0
            self.bullets=0
        else:
            self.max_bullets=self.gun_lvl+4
            
    def set_magic_cost(self):
        if self.magic_lvl==1:
            self.magic_cost=50
        else:
            self.magic_cost= 50 - 10*self.magic_lvl
        
    def receive_damage(self,damage,protection):
        self.health-=(damage-protection)
        if self.health>self.max_health:
            self.health=self.max_health
     
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
            self.magic=self.max_magic 
            
    def stun_change(self):
        self.stunned = not self.stunned
        
    def shield_break(self):
        self.magic_shield=False
        
    def move(self,options):
        return random.choice(options)
  
    
    
class Goblin():
    def __init__(self):
        self.health=15
        self.stunned=False
        
    def receive_damage(self,damage,protection):
        self.health-=(damage-protection) 
        
    def attack(self):
        return 3
        
    def is_alive(self):
        return self.health>0

    def move(self,options):
        return random.choice(options)
    
    def stun_change(self):
        self.stunned= not self.stunned
        
