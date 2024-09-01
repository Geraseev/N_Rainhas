import socket

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5000))  #bota essa porta aqui mesmo
    
    try:
        #input do user aqui
        n = int(input("Digite o número de rainhas (n): "))
        
        #mandando o n pro server
        client_socket.send(str(n).encode())
        
        #aqui vai printar no terminal do client.py
        response = ""
        while True:
            data = client_socket.recv(4096).decode('utf-8')
            if not data:
                break
            response += data
        print("Resposta do servidor:\n", response)
        
    finally:
        client_socket.close()

if __name__ == "__main__":
    client_program()
