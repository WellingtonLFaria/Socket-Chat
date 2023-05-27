import socket
import sys
import threading


def main():
    """Coloca o cliente em execução no host e port informada na chamada do sistema ou nas configurações padrão:
        
        host: 'localhost'
        port: 8080
    
        E cria as threads de envio e recebimento de mensagens.

        Argumentos:
            HOST: Endereço de IP host do servidor. (Chamada do sistema)
            PORT: Porta do servidor. (Chamada do sistema)
        
        Retorno:
            Sem retorno.
    """
    try:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
    except:
        HOST = '127.0.0.1'
        PORT = 8080

    client = criarCliente(HOST, PORT)
    threading.Thread(target=enviarMensagem, args=[client]).start()
    threading.Thread(target=receberMensagem, args=[client]).start()


def criarCliente(host:str, port:int):
    """Cria e tenta conectar o cliente ao servidor no host e port informada.
    
    Argumentos:
        host: Endereço de IP do servidor.
        port: Porta em que está aberto o servidor.

    Retorno:
        client: Socket do cliente já conectado ao servidor se obtido sucesso com a conexão.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except:
        print("Não foi possível conectar ao servidor!")
    return client


def enviarMensagem(cliente):
    """Envia a mensagem informada pelo usuário ao servidor.
    
    Argumentos:
        cliente: Socket do cliente já conectado ao servidor.
    
    Retorno:
        Sem retorno.
    """
    while True:
        try:
            msg = input()
            cliente.sendall(msg.encode('utf-8'))
            print()
        except:
            pass


def receberMensagem(cliente):
    """Recebe a mensagem enviada pelo servidor.
    
    Argumentos:
        cliente: Socket do cliente já conectado ao servidor.

    Retorno:
        Sem retorno.
    """
    while True:
        try:
            msg = cliente.recv(2048).decode('utf-8')
            print(f"Servidor: {msg}\n")
        except:
            pass


if __name__ == "__main__":
    main()