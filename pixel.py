import pygame

class Pixel :
    def __init__(self):
        self.color = "purple"
        print("pixel Init")
    def draw (self, ecran):
        pygame.draw.rect(ecran, self.color, (30, 30, 30, 30)) # on dessine un pixel
    def isClicked (self, pixelColor):
        self.color = pixelColor