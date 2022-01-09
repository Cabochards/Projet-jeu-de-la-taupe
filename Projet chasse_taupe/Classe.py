import pygame
import random
import time






class Player(pygame.sprite.Sprite):
    
    def __init__(self) :
        
        super().__init__()
        
        self.vie=  500
        self.vie_max= 500
        self.degats= 50
        self.bdv=500
        self.image= pygame.image.load('images/viseur.png')
        self.rect= self.image.get_rect()
   
    def Barrede_vie(self,screen):#On dessine 2 barres qui permettent de creer la barre de vie
       
       pygame.draw.rect(screen,(244,203,164),[10,20,self.vie_max,10])#C est cette barre la qui change
       
       pygame.draw.rect(screen,(244,121,131),[10,20,self.vie,10])
   
    def Gainde_vie(self): # quand on clique sur la taupe on gagne de la vie
        self.vie += 30

    def perte_devie(self): # si on clqiue sur l ecran on perd la vie
        self.vie -=10

class Taupe():
    
    def __init__(self):
        
        self.vie= 50
        self.vie_max= 150
        self.image= pygame.image.load("images/basique.png")
        self.degats= 1
        self.rect= self.image.get_rect()
        self.rect.x= 480
        self.rect.y= 345
    
    nombreEnnemis= 4 #On definit a 3 le nombre d ennemi
   

    def Spawn(self):
        
        positions = [  (480,345), (140,450),(20,362),(280,370),(710,410) ] #on definit une liste de positions
        self.image= pygame.image.load("images/basique.png") #taupe 1 hit qui apparait a un lieu de base
        nid= random.choice(positions)
        self.rect.x= nid[0]  
        self.rect.y= nid[1]
        self.vie=50
        
    
    def Sustain(self):#Dans le cas d un missclick notre taupe gagne des hps 
        
        self.vie+=50
        if self.vie > self.vie_max:
            self.vie= self.vie_max
        