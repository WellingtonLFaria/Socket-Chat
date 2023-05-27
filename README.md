# Socket Chat
Comunicação socket servidor e cliente em Python.

## Como realizar a comunicação
Para realizar a comunicação entre servidor e cliente é preciso iniciar os serviços primeiro.

### Iniciando servidor:
```bash
python server.py
```

### Iniciando cliente:
```bash
python client.py
```

Após iniciar os dois serviços a conexão está completa e já pode ser enviadas mensagens entre o servidor e o cliente.

## Alterando endereço de IP e porta do servidor ou conexão do cliente
Basta informar o **endereço de IP seguida da porta** no momento de executar o serviço.

**Ex:**

Iniciando servidor:
```
python server.py 0.0.0.0 80
```

Iniciando cliente:
```bash
python server.py 255.255.255.255 80
```
