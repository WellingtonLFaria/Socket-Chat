import socket
import threading
import sys

try:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
except:
    HOST = "localhost"
    PORT = 8080

class Connection:
    def __init__(self, conn, address) -> None:
        self.conn = conn
        self.address = address

class Message:
    def __init__(self, connection: Connection, message: str) -> None:
        self.connection = connection
        self.message = message

class Server:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.connections: list[Connection] = []
        self.messages: list[Message] = []
        self.startServer()
        t1 = threading.Thread(target=self.sendMessageService).start()
        t2 = threading.Thread(target=self.acceptConnectionService).start()
    
    def startServer(self) -> None:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"Server listening at {self.host}:{self.port} ...")

    def acceptConnectionService(self):
        while True:
            conn, addr = self.server.accept()
            connection = Connection(conn, addr)
            t1 = threading.Thread(target=self.receiveMessageService, args=[connection]).start()
            self.connections.append(Connection(conn, addr))
    
    def receiveMessageService(self, connection: Connection) -> None:
        while True:
            try:
                message = connection.conn.recv(2048).decode("utf-8")
                self.messages.append(Message(connection, message))
                print(f"{connection.address}: {message}")
            except:
                pass
    
    def sendMessageService(self) -> None:
        while True:
            if len(self.messages) > 0:
                try:
                    message = self.messages.pop(0)
                    print(message)
                    for connection in self.connections:
                        if connection.address != message.connection.address:
                            connection.conn.sendall(message.message.encode("utf-8"))
                except:
                    pass

server = Server(HOST, PORT)
