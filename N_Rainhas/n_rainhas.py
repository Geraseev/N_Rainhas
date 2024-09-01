import time

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(board, row + 1, n, solutions)
            board[row] = -1  # backtrack

def print_board(board, n):
    for i in range(n):
        row = ['.'] * n
        row[board[i]] = 'Q'
        print(" ".join(row))
    print("\n")

def n_queens(n):
    board = [-1] * n
    solutions = []
    
    start_time = time.time()
    solve_n_queens(board, 0, n, solutions)
    end_time = time.time()
    
    print(f"Número total de soluções: {len(solutions)}\n")
    for solution in solutions:
        print_board(solution, n)
    
    print(f"Número total de soluções: {len(solutions)}\n")
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos")

if __name__ == "__main__":
    N = 12  #você pode alterar esse valor
    n_queens(N)
