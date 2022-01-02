import pygame
import random
import time

class Game:
    
    def __init__(self):
        self.player= Player()



class Player(pygame.sprite.Sprite):
    
    def __init__(self) :
        super().__init__()
        self.vie= 5
        self.vie_max=5
        self.degats=1
        self.image= pygame.image.load('images/hammer_210x210.png')
        self.rect= self.image.get_rect()
    
    #def HP():
    #def Frapper():
   
        
class Taupe():
    def __init__(self):
        self.vie=0.1
        self.vie=0.1
        self.degats=1
        self.image=pygame.image.load('images/mole180x180.png')
        self.rect=self.image.get_rect()
    #def Spawn():
    #def Morsure(): 
    #def TypeTaupe():