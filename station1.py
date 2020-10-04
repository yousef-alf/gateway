import socket
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'

port = 4444

s.connect((host, port))
i = 0;
timeout = time.time() + 0.1
while True:

    while time.time()<=timeout:


        y = random.randint(0,10)
        s.send((str(y).encode('utf-8')))

    break;

s.close()
