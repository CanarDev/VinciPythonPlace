import pygame
from pixel import Pixel

module_charge = pygame.init()
print(module_charge)

# Création de la fenêtre
pygame.display.set_caption("VinciPythonPlace")


session = True 
pixelColor = (110, 200, 80)
boardPixels = []
for i in range(16):
    row = []
    for j in range(16):
        row.append(Pixel(i, j))
    boardPixels.append(row)

            

while session:
    ecran.fill((110, 110, 110))




    for event in pygame.event.get():# on déclare une variable event qui va récupérer les événements
    #fermer la fenêtre
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                session = False
        if event.type == pygame.QUIT:
            session = False
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            print("j'ai cliqué")
            posX, posY = pygame.mouse.get_pos()
            posX = int(posX/30)
            posY = int(posY/30)
            if posX < 16 and posY < 16:
                boardPixels[posX][posY].isClicked(pixelColor)


    for i in range(16):
        for j in range(16):
            boardPixels[i][j].draw(ecran)

    # on met à jour l'écran
    pygame.display.flip()

# on vide le cache
pygame.quit()