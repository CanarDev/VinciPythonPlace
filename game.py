import pygame
from network import Network

class Pixel :
    def __init__(self,x,y):
        self.color = "purple"
        self.x = x
        self.y = y
    def draw (self, ecran):
        print(self.x)
        print(self.y)
        print(self.color)
        try:
            pygame.draw.rect(ecran, self.color, (self.x*30, self.y*30, 30, 30)) # on dessine un pixel
        except: 
            print(self.x)
            print(self.y)
            print(self.color)

    def isClicked (self, pixelColor):
        self.color = pixelColor

class Player():

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
        self.canvas = Canvas(w,h)#pygame.display.set_mode((self.width,self.height))

    def run(self):
        pixelColor = "yellow"
        boardPixels = []
        for i in range(3):# lignes

            row = []
            for j in range(3):# colonnes
                row.append(Pixel(i, j))
            boardPixels.append(row)
        # for i in range(16):
        #     for j in range(16):
        #         print(str(boardPixels[i][j].x) + " " + str(boardPixels[i][j].y))
        timer = 0
        ecran = pygame.display.set_mode((1000, 800))
        session = True
        testPixel = Pixel(1, 1)
        while session:
            timer +=1
            ecran.fill("red")
            for event in pygame.event.get():# on déclare une variable event qui va récupérer les événements
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
                        # boardPixels[posX][posY].isClicked(pixelColor)
                        print(self.parse_data(self.send_data(posX, posY, pixelColor)))
            if timer > 60:
                timer = 0
                data = self.parse_data(self.send_data(-1, -1, "wesh"))
                try:

                    pixelRecieved = data.split(',')
                    print("wesh")
                    print (pixelRecieved) 
                    boardPixels[int(pixelRecieved[0])][int(pixelRecieved[1])].color = pixelRecieved[2]
                    #for pixels in pixelRecieved:
                    #    pixeldata = pixels.split(",")
                    #    boardPixels[int(pixeldata[0])][int(pixeldata[1])].color = pixeldata[2]
                except:
                    print("error")

                
        

            for i in range(3):
                for j in range(3):
                    boardPixels[i][j].draw(ecran)
                    
            testPixel.draw(ecran)
            pygame.display.flip()
            # self.canvas.update()

        pygame.quit()

    def send_data(self, posX, posY, pixelColor):
        """
        Send position to server
        :return: None
        """
        data = str(self.net.id) + ":" + str(posX) + "," + str(posY) + "," + str(pixelColor)
        reply = self.net.send(data)
        return reply

    @staticmethod
    def parse_data(data):
        print(data)
        return data


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
