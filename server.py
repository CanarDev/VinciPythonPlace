import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '127.0.0.1'
port = 5432

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")


boardPixels = []
for i in range(16):# lignes
        row = []
        for j in range(16):# colonnes
            row.append("green")
        boardPixels.append(row)



currentId = "0"
pos = ["0:50,50", "1:100,100"]
def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    savex = -1
    savey = -1
    saveColor =0
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: " + reply)
                arr = reply.split(":")
                id = int(arr[0])
                dataPixel = arr[1].split(",")
                pixelX = int(dataPixel[0])
                pixelY = int(dataPixel[1])
                pixelColor = dataPixel[2]
                print("ok")
                if pixelX == -1 and pixelY == -1:
                    #TAB
                    print("ok1")
                    data1 =""
                    """for i in range(3):# ligne
                       for j in range(3):
                            data+= str(i) +"," + str(j) +","+ str(boardPixels[i][j]) + "/"
                    """
                    print(savex)
                    print(savey)
                    print(str(saveColor))
                    data1 = str(savex)+","+str(savey)+","+str(saveColor)
                    print("ok2")
                    print("Sending: " + data1)
                


                else:
                    savex = pixelX
                    savey = pixelY
                    saveColor = pixelColor

                    data1 = "ok"
                    print("Sending: " + data1)
                print("ok4")
                conn.sendall(str.encode(data1))
                print("ok5")
        except:
            print("lose")
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))