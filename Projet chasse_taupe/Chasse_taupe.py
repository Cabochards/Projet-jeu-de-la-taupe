import pygame
import Classe
from pygame.display import set_icon


pygame.init()

#creation de la taille de la fenetre 

screen=pygame.display.set_mode((864,816))
pygame.display.set_caption('Chasse-taupe')


Icone = pygame.image.load('images/Mole.png')
pygame.display.set_icon(Icone)

background= pygame.image.load('images/la foret.png')

game=Classe.Game()
player=Classe.Player()
taupe=Classe.Taupe()
pygame.mouse.set_visible(False)
#On maintient la fenetre ouverte
running= True
 
while running :
    
    screen.blit(background,(0,0))


    player.rect.center = pygame.mouse.get_pos() 
    screen.blit(player.image,player.rect) # applique le curseur
    
    screen.blit(taupe.image,taupe.rect)
    
    pygame.display.flip()

   
    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False # running est sur False
        if event.type==pygame.QUIT:
            running = False

pygame.quit() 