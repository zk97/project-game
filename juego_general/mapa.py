import time
import random
import numpy as np


#[forest,lake,begining,cave]

class Outdoors():
    def __init__(self,kind):
        self.kind=kind
        
    def get_kind(self):
        return self.kind
    
    
class Cave():
    def __init__(self):
        self.doors=5
        self.games=['Pistolero','Candado','Acertijos','Valiente','Examen']
        
    def set_doors(self):
        self.doors=random.randint(1,self.doors)
        
    def show_doors(self):
        if self.doors==1:
            return ['Salida']
        else:
            return random.sample(self.games,self.doors)
    
    
        
        
    