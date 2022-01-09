import pygame
from pygame.sprite import collide_rect
import Classe
from pygame.display import set_icon


pygame.init()

vitesse=pygame.time.Clock()
#creation de la taille de la fenetre 

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Chasse-taupe')


Icone = pygame.image.load('images/Mole.png')
pygame.display.set_icon(Icone)

background= pygame.image.load('images/bg.jpg')

game= Classe.Game()
player= Classe.Player()
Ennemis= []

for i in range(Classe.Taupe.nombreEnnemis):
    taupe= Classe.Taupe()
    Ennemis.append(taupe)

pygame.mouse.set_visible(False)
#On maintient la fenetre ouverte
running= True
 
while running :
    
    screen.blit(background,(0,0))
    player.rect.center = pygame.mouse.get_pos() 
    player.Barrede_vie(screen)
    player.vie-= 0.1 #vitesse de la barre de vie
    
    for event in pygame.event.get():
        
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False # running est sur False
        
        
        
        for a in Ennemis:
            Enemmies_envie=[]
            if player.rect.colliderect(a.rect) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                a.vie-=player.degats       
                player.Gainde_vie()
                a.Spawn()
                if a.Spawn():
                   Enemmies_envie.append(a)
            
            if not player.rect.colliderect(a.rect) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:        
                a.Sustain()           
                player.perte_devie()
                a.Spawn()
            
            if player.vie_max < player.vie:
                player.vie= player.vie_max
            
            
                
                      
            
        if event.type==pygame.QUIT:
           running = False
    screen.blit(player.image,player.rect) # applique le curseur
    
    for k in Ennemis:
        screen.blit(k.image,k.rect)
        
        
    
    pygame.display.flip()
    vitesse.tick(169)

pygame.quit() 