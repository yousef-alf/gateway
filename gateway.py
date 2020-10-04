import socket
import sys
import matplotlib.pyplot as plt
import time


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 4444

serversocket.bind((host, port))

serversocket.listen(5)

while True:

    clientsocket, addr = serversocket.accept()

    i=0
    x =[]
    y =[]
    timeout = time.time() + 0.1

    while True:

        while time.time() < timeout:
            rec = clientsocket.recv(1024).decode('utf-8')
            rec2 = int(rec)
            if(rec2<11):
                print(rec2)
                y.append(rec2)
                x.append(i)
            print(x)

            print(y)
            i=i+1
        plt.plot(x, y)
        plt.xlabel('Time')
        plt.ylabel('Mw')
        plt.title('station 1')
        plt.show()
        break;
    break;

clientsocket.close()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5555

serversocket.bind((host, port))

serversocket.listen(5)

while True:

    clientsocket, addr = serversocket.accept()

    i=0
    x2 =[]
    y2 =[]
    timeout = time.time() + 0.1

    while True:

        while time.time() < timeout:
            rec = clientsocket.recv(1024).decode('utf-8')
            rec2 = int(rec)
            if(rec2<11):
                print(rec2)
                y2.append(rec2)
                x2.append(i)
            print(x2)

            print(y2)
            i=i+1
        plt.plot(x2, y2)
        plt.xlabel('Time')
        plt.ylabel('Mw')
        plt.title('Station2')
        plt.show()
        break;
    break;


avgx = []
avgy = []
j = 0
while j<len(y)&j<len(y2):
    avgy0 = (y[j]+y2[j])/2
    avgy.append(avgy0)
    avgx.append(j)
    print(avgx)
    j=j+1
plt.plot(avgx, avgy)
plt.xlabel('Time')
plt.ylabel('Mw')
plt.title('Average moment magnitude')
plt.show()
clientsocket.close()
sys.exit()
