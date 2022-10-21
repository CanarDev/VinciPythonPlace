import pygame
from network import Network

""" class Pixel :
    def __init__(self,x,y):
        self.color = "purple"
        self.x = x
        self.y = y
        print("pixel Init")
    def draw (self, ecran):
        pygame.draw.rect(ecran, self.color, (self.x*30, self.y*30, 30, 30)) # on dessine un pixel
    def isClicked (self, pixelColor):
        self.color = pixelColor """

class Player():
    width = height = 50

    def __init__(self, startx, starty, color=(255,0,0)):
        self.x = startx
        self.y = starty
        self.velocity = 2
        self.color = color

    def draw(self, g):
        pygame.draw.rect(g, self.color ,(self.x, self.y, self.width, self.height), 0)

    def move(self, dirn):
        """
        :param dirn: 0 - 3 (right, left, up, down)
        :return: None
        """

        if dirn == 0:
            self.x += self.velocity
        elif dirn == 1:
            self.x -= self.velocity
        elif dirn == 2:
            self.y -= self.velocity
        else:
            self.y += self.velocity



class Game:

    def __init__(self, w, h):
        self.net = Network()
        self.width = w
        self.height = h
        self.canvas = Canvas(self.width, self.height, "TheVinciPlace")

        pixelColor = (110, 200, 80)
        boardPixels = []
        for i in range(16):# lignes
            row = []
            for j in range(16):# colonnes
                row.append(Pixel(i, j))
            boardPixels.append(row)

    def run(self):
        session = True
        while session:

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

            for i in range(16):# lignes
                    for j in range(16):# colonnes
                        boardPixels[i][j].draw(ecran)
        pygame.quit()

    def send_data(self):
        """
        Send position to server
        :return: None
        """
        data = str(self.net.id) + ":" + str(self.player.x) + "," + str(self.player.y)
        reply = self.net.send(data)
        return reply

    @staticmethod
    def parse_data(data):
        try:
            d = data.split(":")[1].split(",")
            return int(d[0]), int(d[1])
        except:
            return 0,0


class Canvas:

    def __init__(self, w, h, name="None"):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((w,h))
        pygame.display.set_caption(name)

    @staticmethod
    def update():
        pygame.display.update()

    def draw_text(self, text, size, x, y):
        pygame.font.init()
        font = pygame.font.SysFont("comicsans", size)
        render = font.render(text, 1, (0,0,0))

        self.screen.draw(render, (x,y))

    def get_canvas(self):
        return self.screen

    def draw_background(self):
        self.screen.fill((255,255,255))
