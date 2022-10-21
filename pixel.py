import pygame

class Pixel :
    def __init__(self,x,y):
        self.color = "purple"
        self.x = x
        self.y = y
        print("pixel Init")
    def draw (self, ecran):
        print(self.x)
        print(self.y)
        print(self.color)
        pygame.draw.rect(ecran, self.color, (self.x*100, self.y*100, 30, 30)) # on dessine un pixel
    def isClicked (self, pixelColor):
        self.color = pixelColor