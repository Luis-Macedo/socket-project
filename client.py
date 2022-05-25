import json
import socket
import json

HOST = "127.0.0.1"
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    dados = s.recv(1024)
    message = dados.decode("utf-8")
    print(message)
    print("Comandos disponíveis: [1: Raiz], [2: Potência], [3:Seno], [4: Cosseno], [5: Tangente], [6: Fatorial], [SAIR]")
    comando = str(input("Digite o comando a enviar: "))
    while not comando.startswith(('1','2','3','4','5','6', "SAIR")):
        msg = "Não é um comando válido"
        print(msg)
        comando = input("Digite o comando a enviar: ")
    if comando.startswith("SAIR"):
        s.sendall(comando.encode())
        s.close
        print("Conexão encerrada.")
        break
    elif comando.startswith('1'):
        comando1 = comando
        raiz = input("Digite o número desejado: ")
        list = {
            'comando1': comando1,
            'raiz': raiz
        }
        msg = str.encode(json.dumps(list))
        s.sendall(msg)
    elif comando.startswith('2'):
        comando1 = comando
        base = input("Digite a base da potência: ")
        expoente = input("Digite o expoente:")
        
        list = {
            'comando1': comando1,
            'base': base,
            'expoente': expoente
        }
        msg = str.encode(json.dumps(list))
        s.sendall(msg)
    elif comando.startswith('3'):
        comando1 = comando
        seno = input("Digite o valor do seno que deseja encontrar: ")
        list = {
            'comando1': comando1,
            'seno': seno
        }
        msg = str.encode(json.dumps(list))
        s.sendall(msg)
    elif comando.startswith('4'):
        comando1 = comando
        cosseno = input("Digite o valor do cosseno que deseja encontrar: ")
        list = {
            'comando1': comando1,
            'cosseno': cosseno
        }
        msg = str.encode(json.dumps(list))
        s.sendall(msg)
    elif comando.startswith('5'):
        comando1 = comando
        tangente = input("Digite o valor da tangente que deseja encontrar: ")
        list = {
            'comando1': comando1,
            'tangente': tangente
        }
        msg = str.encode(json.dumps(list))
        s.sendall(msg)
    else:
        comando1 = comando
        fatorial = input("Digite o valor do fatorial que deseja encontrar: ")
        list = {
            'comando1': comando1,
            'fatorial': fatorial
        }
        msg = str.encode(json.dumps(list))
        s.sendall(msg)