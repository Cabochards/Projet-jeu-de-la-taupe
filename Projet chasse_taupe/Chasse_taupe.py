import pygame
from pygame.draw import rect
from pygame.sprite import collide_rect
import Classe
from pygame.display import set_icon


pygame.init()

vitesse=pygame.time.Clock()#pour les fps
#creation de la taille de la fenetre 

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Chasse-taupe')


Icone = pygame.image.load('images/Mole.png')
pygame.display.set_icon(Icone)

background= pygame.image.load('images/bg.jpg')
background_rect= background.get_rect()

player= Classe.Player()
Ennemis= []

for i in range(Classe.Taupe.nombreEnnemis): #sert pr le nombre de taupe qui apparait sur le terrain tant qu il y aura pas le nombre d ennemis max il en  refera automatiquement respawn
    taupe= Classe.Taupe()
    Ennemis.append(taupe)#On cree une liste taupe qui nous permettre de faire apparaitre les ennemis

pygame.mouse.set_visible(False)
#On maintient la fenetre ouverte
running= True
 
while running :
    
    screen.blit(background,(0,0))
    player.rect.center = pygame.mouse.get_pos() 
    player.Barrede_vie(screen)
    player.vie-= 0.1 # vitesse de la barre de vie
    
    for event in pygame.event.get():
        
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False # running est sur False
        if event.type==pygame.QUIT:
           running = False
        
        
        for a in Ennemis:

            if a.vie == 0:
                a.Spawn()
              
            if player.rect.colliderect(a.rect) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               
                a.vie-=player.degats
                player.Gainde_vie()
                
            elif player.rect.colliderect(background_rect) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1  :        
            #On met une condition si on touche l ecran avec notre souris on perd de la vie on en fait gagner aux autres
            
                
                if not player.rect.colliderect(a.rect) :
                # on redistribue les pv car on a pas touche la hitbox de la taupe
    
                    a.Sustain()
                   
                    if a.vie == 50 :
                        a.image= pygame.image.load("images/basique.png")
                        a.vie-=50
                    
                    if a.vie == 100:
                        a.image= pygame.image.load("images/alien.png") 
                        
                
                    if a.vie == 150:
                        a.image= pygame.image.load("images/mcdo.png")
                   
                player.perte_devie()
               
            
            if player.vie_max < player.vie:#on fait en sorte que nos pv ne depasse jamais 500
                player.vie= player.vie_max
            
        if player.vie < 0 :
             running= False
  
    screen.blit(player.image,player.rect) # applique le curseur
    
    for k in Ennemis:
        screen.blit(k.image,k.rect)
        
        
    
    pygame.display.flip()
    vitesse.tick(60) #fps

pygame.quit() 