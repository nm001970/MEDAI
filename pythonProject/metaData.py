import socket
import numpy as np
from sklearn.linear_model import LinearRegression


class socketServer:
    def __init__(self, address='', port=''):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.port = port
        self.sock.bind((self.address, self.port))

    def listen(self):
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        print('connection to', self.addr)
        self.cummdata = ''

        while True:
            data = self.conn.recv(10000)
            if not data:
                print('no data')
                break
            self.cummdata += data.decode('utf-8')
            print(data)
            self.conn.send(bytes(calcregr(self.cummdata), 'utf-8'))

        return self.cummdata

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()


def calcregr(msg=''):
    chartdata = np.frombuffer(msg.encode('utf-8'), dtype=float, sep=' ')
    print(chartdata)
    Y = np.array(chartdata).reshape(-1, 1)
    X = np.array(np.arange(len(chartdata))).reshape(-1, 1)

    lr = LinearRegression()
    lr.fit(X, Y)
    Y_pred = lr.predict(X)
    P = Y_pred.astype(str).item(-1) + ' ' + Y_pred.astype(str).item(0)
    print(P)
    return str(P)


server = socketServer('192.168.1.184', 14201)
print("Start Python server at", server.address, "on port", server.port)

while True:
    msg = server.listen()
