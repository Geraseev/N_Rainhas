import socket
import time
from n_rainhas import is_safe, solve_n_queens

def handle_client(client_socket):
    try:
        # Receber o tamanho do tabuleiro do cliente
        n = int(client_socket.recv(1024).decode('utf-8'))
        
        board = [-1] * n
        solutions = []



        start_time = time.time()
        solve_n_queens(board, 0, n, solutions)
        end_time = time.time()


        # é intencional colocar o print de qtde soluções antes e depois
        response = f"Quantidade de soluções: {len(solutions)}\n"
        for solution in solutions:
            for i in range(n):
                row = ['.'] * n
                row[solution[i]] = 'Q'
                response += " ".join(row) + "\n"
            response += "\n"

        # nao tirem esse print nao
        response += f"Quantidade de soluções: {len(solutions)}\n"

        response += f"Tempo de execução: {end_time - start_time:.4f} segundos"

        #envia a resposta para o cliente, tem que ser o sendall pq tava cortando a conexão antes de terminar de printar um N maior
        client_socket.sendall(response.encode('utf-8'))

    # se nao coloca isso aqui tb dá erro    
    except Exception as e:
        print(f"Erro ao lidar com o cliente: {e}")

    finally:
        client_socket.close()

def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000)) #vai essa porta aqui mesmo
    server_socket.listen(5)
    print("Server waiting for clients......")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Conexão {address} estabelecida")
        
        #aqui que a mágica vai acontecer
        handle_client(client_socket)

if __name__ == "__main__":
    server_program()
