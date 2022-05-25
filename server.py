import socket
import threading
import json
import math

HOST = "127.0.0.1" # localhost
PORT = 1234 # > 1023

def calculate(cliente, endereco):
    print(f"Conectado em {endereco}")
    while True:
        
        menu = "Bem vindo a calculadora! Envie seu comando"
        cliente.sendall(menu.encode())

        dados = cliente.recv(1024).decode('utf-8')
        msg = json.loads(dados)
        print(f"{endereco} enviou o comando {msg}")
        if msg['comando1'].startswith('1'):
            print(f"raiz enviada: ", msg['raiz'])
            resultado = math.sqrt(int(msg['raiz']))
            mensagem = f"[INFO] Resultado: {resultado} \n"
            cliente.sendall(mensagem.encode())
        elif msg['comando1'].startswith('2'):
            print(f"Base e expoente enviados: {msg['base']}, {msg['expoente']}")
            resultado = int(msg['base'])**int(msg['expoente'])
            mensagem = f"[INFO] Resultado da potencia: {resultado} \n"
            cliente.sendall(mensagem.encode())
        elif msg['comando1'].startswith('3'):
            print(f"Seno enviado: {msg['seno']}")
            resultado = math.sin(int(msg['seno']))
            mensagem = f"[INFO] Resultado do seno: {resultado} \n"
            cliente.sendall(mensagem.encode())
        elif msg['comando1'].startswith('4'):
            print(f"Cosseno enviado: {msg['cosseno']}")
            resultado = math.cos(int(msg['cosseno']))
            mensagem = f"[INFO] Resultado do cosseno: {resultado} \n"
            cliente.sendall(mensagem.encode())
        elif msg['comando1'].startswith('5'):
            print(f"Tangente enviada: {msg['tangente']}")
            resultado = math.tan(int(msg['tangente']))
            mensagem = f"[INFO] Resultado da tangente: {resultado} \n"
            cliente.sendall(mensagem.encode())
        else:
            print(f"Fatorial dada: {msg['fatorial']}")
            resultado = math.factorial(int(msg['fatorial']))
            mensagem = f"[INFO] Resultado do fatorial: {resultado} \n"
            cliente.sendall(mensagem.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
print("Aguardando conexões")
while True:
    cliente, endereco = s.accept()
    cliente.settimeout(120)
    threading.Thread(target=calculate, args=(cliente, endereco)).start()


