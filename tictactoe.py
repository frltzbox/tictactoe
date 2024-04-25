import os
import random
import time

feld = [[3*j+i+1 for i in range(3)] for j in range(3)]

def feld_malen():
    print('\n')
    print(' ', feld[0][0],' | ', feld[0][1],' | ', feld[0][2])
    print('-'*15)
    print(' ', feld[1][0],' | ', feld[1][1],' | ', feld[1][2])
    print('-'*15)
    print(' ', feld[2][0],' | ', feld[2][1],' | ', feld[2][2])
    print('\n')

def main():
    while True:  # Keep the game running until the user chooses to exit
        os.system('clear')
        game_over = False
        zug = 0
        spieler = ['❌', '⭕️']
        
        abfrage = input('Spielmodi:\n1. Bot gegen Spieler\n2. Spieler gegen Spieler\n')
        feld_malen()
        
        if abfrage == '1':
            while not game_over:
                print('Du bist am Zug. Es ist Zug #' + str(zug)+'\n')
                eingabe = input('Dein Zug bitte: ')
                
                if eingabe not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    print('Ungültige Eingabe\n')
                    continue
                
                row = (int(eingabe) - 1) // 3
                col = (int(eingabe) - 1) % 3
                
                if feld[row][col] in [spieler[0], spieler[1]]:
                    print('Dieses Feld ist bereits belegt.\n')
                    continue
                
                feld[row][col] = spieler[zug % 2]
                zug += 1
                feld_malen()
                
                if check_win():
                    print('\nDu hast gewonnen!')
                    game_over = True
                elif zug == 9:
                    print('\nUnentschieden!')
                    game_over = True
                    
                if not game_over:
                    print("\nBot denkt nach...")
                    time.sleep(1)
                    bot_zug = bot()
                    row = bot_zug // 3
                    col = bot_zug % 3
                    feld[row][col] = spieler[zug % 2]
                    zug += 1
                    feld_malen()
                    
                    if check_win():
                        print('\nDer Bot hat gewonnen!')
                        game_over = True
                    elif zug == 9:
                        print('\nUnentschieden!')
                        game_over = True
        
        elif abfrage == '2':
            while not game_over:
                feld_malen()

                print('Spieler ' + spieler[zug % 2] + ' ist am Zug. Es ist Zug #' + str(zug))
                eingabe = input('Dein Zug bitte: ')
                
                if eingabe not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    print('Ungültige Eingabe')
                    continue
                
                row = (int(eingabe) - 1) // 3
                col = (int(eingabe) - 1) % 3
                
                if feld[row][col] in [spieler[0], spieler[1]]:
                    print('Dieses Feld ist bereits belegt.')
                    continue
                
                feld[row][col] = spieler[zug % 2]
                zug += 1
                
                feld_malen()
                
                if check_win():
                    print('Spieler ' + spieler[(zug - 1) % 2] + ' hat gewonnen!')
                    game_over = True
                elif zug == 9:
                    print('Unentschieden!')
                    game_over = True
                    
        else:
            print('Ungültige Eingabe')
            continue  # Restart the loop if the input is invalid
        
        # After the game ends, prompt the user to play again or exit
        play_again = input("Möchten Sie noch einmal spielen? (Ja/Nein): ").lower()
        if play_again != 'ja':
            break  # Exit the loop and end the game if the user chooses not to play again

def check_win():
    for i in range(3):
        if feld[i][0] == feld[i][1] == feld[i][2] or feld[0][i] == feld[1][i] == feld[2][i]:
            return True
    if feld[0][0] == feld[1][1] == feld[2][2] or feld[0][2] == feld[1][1] == feld[2][0]:
        return True
    return False

def check_patterns():
    patterns = [
        # Rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    
    for pattern in patterns:
        symbols = [feld[row][col] for row, col in pattern]
        if symbols.count('❌') == 3:  # Player X wins
            return '❌'
        elif symbols.count('⭕️') == 3:  # Player O wins
            return '⭕️'
    
    return None

def bot():
    # First, check if bot can win in the next move
    for i in range(9):
        row = i // 3
        col = i % 3
        if feld[row][col] not in ['❌', '⭕️']:
            feld[row][col] = '⭕️'
            if check_patterns() == '⭕️':
                return i
            else:
                feld[row][col] = str(i + 1)
    
    # If bot cannot win, check if opponent can win in the next move and block
    for i in range(9):
        row = i // 3
        col = i % 3
        if feld[row][col] not in ['❌', '⭕️']:
            feld[row][col] = '❌'
            if check_patterns() == '❌':
                feld[row][col] = '⭕️'  # Block the opponent
                return i
            else:
                feld[row][col] = str(i + 1)
    
    # If neither winning nor blocking, make a random move
    return random.choice([i for i in range(9) if feld[i // 3][i % 3] not in ['❌', '⭕️']])


if __name__ == '__main__':
    main()
