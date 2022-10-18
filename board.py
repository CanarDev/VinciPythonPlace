import pygame
from pixel import Pixel

module_charge = pygame.init()
print(module_charge)

# Création de la fenêtre
ecran = pygame.display.set_mode((1000,800))
pygame.display.set_caption("VinciPythonPlace")


session = True 
pixel = Pixel()
pixelColor = (110, 200, 80)
while session:
    ecran.fill((110, 110, 110))




    for event in pygame.event.get():# on déclare une variable event qui va récupérer les événements
    #fermer la fenêtre
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                session = False
        if event.type == pygame.QUIT:
            session = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t: #Test command : T key
                print("IsClicked !")
                pixel.isClicked(pixelColor)
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            print("j'ai cliqué")
            pos = pygame.mouse.get_pos()
            
            pixel.isClicked(pixelColor)



    pixel.draw(ecran)
    # on met à jour l'écran
    pygame.display.flip()

# on vide le cache
pygame.quit()