import pygame
import random
import time


class Game:
    
    def __init__(self):
        self.player= Player()



class Player(pygame.sprite.Sprite):
    
    def __init__(self) :
        
        super().__init__()
        
        self.vie=  500
        self.vie_max= 500
        self.degats= 50
        self.bdv=500
        self.image= pygame.image.load('images/crosshair_1_50.png')
        self.rect= self.image.get_rect()
   
    def Barrede_vie(self,screen):
       
       pygame.draw.rect(screen,(244,203,164),[10,20,self.vie_max,10])
       pygame.draw.rect(screen,(244,121,131),[10,20,self.vie,10])
   
    def Gainde_vie(self):
        self.vie += 30

    def perte_devie(self):
        self.vie -=10

class Taupe():
    
    def __init__(self):
        
        taupeimage=['images/alien.png','images/mcdo.png','images/basique.png']
        self.image=pygame.image.load(random.choice(taupeimage))
    
        self.vie= 50
        self.vie_max= 50
        self.degats= 1
        self.rect= self.image.get_rect()
        self.rect.x= 480
        self.rect.y= 345
    
    nombreEnnemis= 2
    
    def Spawn(self):
        
        positions = [  (480,345), (140,450),(20,362),(280,370),(710,410) ]
        
        nid= random.choice(positions)
        self.rect.x= nid[0]  
        self.rect.y= nid[1]
        self.vie+=1
        
    
    def Sustain(self):
        self.vie+=1
        if self.vie > self.vie_max:
            self.vie= self.vie_max
