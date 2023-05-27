import socket
import sys
import threading


def main():
    """Coloca o servidor em execução no host e port informada na chamada do sistema ou nas configurações padrão:
        
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
        HOST = 'localhost'
        PORT = 8080

    server = criarServidor(HOST, PORT)

    conn, addr = server.accept()
    print(f"Conectado com {addr[0]}")
    conn.sendall('Conectado ao servidor!'.encode('utf-8'))
    threading.Thread(target=receberMensagem, args=[conn, addr]).start()
    threading.Thread(target=enviarMensagem, args=[conn]).start()


def criarServidor(host:str, port:int):
    """Cria o servidor no host e port informada.
    Argumentos:
        host: Endereço de IP host do servidor.
        port: Porta do servidor.

    Retorno:
        server: Retorna o objeto socket do servidor já configurado e escutando no host e port informada.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Servidor escutando: {host, port}")
    print('Esperando conexão com o cliente.')
    return server


def enviarMensagem(clientconn, msg=""):
    """Envia mensagem ao 'clientconn' informado.
    Se msg for informado a mensagem que será enviada é o msg, caso contrário terá um input para um usuário no servidor.

    Argumentos:
        clientconn: Objeto da conexão com o cliente.
        msg: Mensagem a ser enviada para o cliente.
    
    Retorno:
        Sem retorno.
    """
    while True:
        try:
            msg = input()
            clientconn.sendall(msg.encode('utf-8'))
            print()
        except:
            clientconn.sendall(msg.encode('utf-8'))


def receberMensagem(clientconn, addr):
    """Recebe as mensagens do objeto de conexão clientconn informado e exibe no terminal do servidor.

    Argumentos:
        clientconn: Objeto da conexão com o cliente.
        addr: Endereço de IP do cliente.
    
    Retorno:
        Sem retorno.
    """
    while True:
        try:
            msg = clientconn.recv(2048).decode('utf-8')
            print(f"{addr}: {msg}\n")
        except:
            pass


if __name__ == "__main__":
    main()