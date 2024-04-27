import os
import random
import time

def initialize_board(size):
    max_number = size * size
    num_digits = len(str(max_number))
    return [[f"{(size * j + i + 1):>{num_digits}}" for i in range(size)] for j in range(size)]

def draw_board(board):
    size = len(board)
    for i in range(size):
        print("")
        print(" " + "―――" * size*2)
        print("| " + " | ".join(board[i]) + " |")
    print(" " + "―――" * size*2)
    print("")



def get_user_move(board):
    size = len(board)
    while True:
        try:
            move = int(input("Gib deinen Zug ein (1-" + str(size * size) + "): "))
            if move < 1 or move > size * size:
                print("Ungültiger Zug. Bitte gib eine Zahl zwischen 1 und", size * size, "ein.")
                continue
            row = (move - 1) // size
            col = (move - 1) % size
            if board[row][col] != f"{move:>{len(str(size * size))}}":
                print("Dieses Feld ist bereits belegt. Bitte wähle ein anderes.")
                continue
            return row, col
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")

def bot_move(board, player):
    size = len(board)
    # Zuerst prüfen, ob der Bot im nächsten Zug gewinnen kann
    for i in range(size * size):
        row = i // size
        col = i % size
        if board[row][col] == f"{i + 1:>{len(str(size * size))}}":
            board[row][col] = player
            if check_win(board, player):
                return True
            else:
                board[row][col] = f"{i + 1:>{len(str(size * size))}}"

    # Wenn der Bot nicht gewinnen kann, prüfen, ob der Gegner im nächsten Zug gewinnen kann und blockieren
    opponent = '⭕️' if player == '❌' else '❌'
    for i in range(size * size):
        row = i // size
        col = i % size
        if board[row][col] == f"{i + 1:>{len(str(size * size))}}":
            board[row][col] = opponent
            if check_win(board, opponent):
                board[row][col] = player  # Blockieren des Gegners
                return False
            else:
                board[row][col] = f"{i + 1:>{len(str(size * size))}}"


    # Wenn weder ein Gewinn noch ein Blockieren möglich ist, mache einen zufälligen Zug
    empty_positions = [(row, col) for row in range(size) for col in range(size) if board[row][col] != '❌' and board[row][col] != '⭕️']
    if empty_positions:
        row, col = random.choice(empty_positions)
        board[row][col] = player
    return False

def check_win(board, player):
    size = len(board)
    # Überprüfe Zeilen, Spalten und Diagonalen
    for i in range(size):
        if all(board[i][j] == player for j in range(size)) or \
           all(board[j][i] == player for j in range(size)):
            return True
    # Überprüfe Diagonalen
    if all(board[i][i] == player for i in range(size)) or \
       all(board[i][size - 1 - i] == player for i in range(size)):
        return True
    return False

def main():
    while True:
        os.system('clear')
        print("Willkommen bei Tic-Tac-Toe!")
        print("Wähle deinen Modus:")
        print("1. Bot gegen Spieler")
        print("2. Spieler gegen Spieler")
        print("3. Beenden")

        choice = input("Gib deine Auswahl ein: ")

        if choice == '1' or choice == '2':
            size = int(input("Gib die Größe des Spielfelds ein (z.B. 3 für 3x3): "))
            if size < 3:
                print("Das Spielfeld muss mindestens 3x3 groß sein.")
                continue
            board = initialize_board(size)
            players = ['❌', '⭕️']
            current_player = random.choice(players)

            while True:
                if choice == '1' and current_player == '⭕️':
                    print("Der Bot denkt nach...")
                    time.sleep(1)
                    if bot_move(board, current_player):
                        draw_board(board)
                        print("Der Bot gewinnt!")
                        break
                else:
                    draw_board(board)

                    print("Spieler", current_player + " ist dran")
                    row, col = get_user_move(board)
                    board[row][col] = current_player
                    draw_board(board)
                    if check_win(board, current_player):
                        print("Spieler", current_player, "gewinnt!")
                        break

                if all(board[i][j] != f"{size * j + i + 1:>{len(str(size * size))}}" for i in range(size) for j in range(size)):
                    print("Unentschieden!")
                    break

                if check_win(board, current_player):
                    print("Spieler", current_player, "gewinnt!")
                    break

                if all(board[i][j] != f"{size * j + i + 1:>{len(str(size * size))}}" for i in range(size) for j in range(size)):
                    print("Unentschieden!")
                    break

                current_player = players[(players.index(current_player) + 1) % len(players)]

        elif choice == '3':
            print("Auf Wiedersehen!")
            break

        else:
            print("Ungültige Auswahl. Bitte gib 1, 2 oder 3 ein.")

if __name__ == '__main__':
    main()
