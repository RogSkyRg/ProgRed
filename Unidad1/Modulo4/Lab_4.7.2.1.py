'''
Nombre: Méndez Fernandez Alan Eusebio
Descripcion: Lab 4.7.2.1
Fecha: 30/10/2024
'''

from random import randrange

def DisplayBoard(board):
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|  " + "  |  ".join(row) + "  |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def EnterMove(board):
    move = int(input("Ingresa tu movimiento: "))
    free_fields = MakeListOfFreeFields(board)
    valid_move = False
    while not valid_move:
        if (move-1) in range(9) and (move//3, move%3) in free_fields:
            row, col = (move-1)//3, (move-1)%3
            board[row][col] = 'O'
            valid_move = True
        else:
            move = int(input("Movimiento inválido. Ingresa tu movimiento nuevamente: "))

def MakeListOfFreeFields(board):
    free_fields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['O', 'X']:
                free_fields.append((r, c))
    return free_fields

def VictoryFor(board, sign):
    win_combinations = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
    for combo in win_combinations:
        if all([board[r][c] == sign for r, c in combo]):
            return True
    return False

def DrawMove(board):
    free_fields = MakeListOfFreeFields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

board = [
    ['1', '2', '3'],
    ['4', 'X', '6'],
    ['7', '8', '9']
]

while True:
    DisplayBoard(board)
    EnterMove(board)
    if VictoryFor(board, 'O'):
        DisplayBoard(board)
        print("¡Has Ganado!")
        break
    DrawMove(board)
    if VictoryFor(board, 'X'):
        DisplayBoard(board)
        print("La Máquina Ha Ganado.")
        break
    if not MakeListOfFreeFields(board):
        DisplayBoard(board)
        print("¡Es un Empate!")
        break