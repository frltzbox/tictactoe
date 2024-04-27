# Tic-Tac-Toe Spiel

Dieses Python-Programm implementiert das klassische Tic-Tac-Toe Spiel, auch bekannt als "Drei gewinnt". Das Spiel bietet verschiedene Modi, darunter Spieler gegen Spieler und Bot gegen Spieler.

## Spielanleitung

1. Das Spielfeld ist ein Raster mit 3x3 (kann angepasst werden).
2. Zwei Spieler nehmen abwechselnd Züge.
3. Ziel ist es, eine Linie aus drei eigenen Symbolen horizontal, vertikal oder diagonal zu bilden.
4. Der erste Spieler, der eine solche Linie bildet, gewinnt das Spiel.
5. Wenn alle Felder gefüllt sind und kein Spieler eine Linie gebildet hat, endet das Spiel unentschieden.

## Anforderungen

- Python 3.x

## Funktionen

- `initialize_board(size)`: Initialisiert das Spielfeld mit der angegebenen Größe.
- `draw_board(board)`: Zeichnet das aktuelle Spielfeld.
- `check_win(board, player)`: Überprüft, ob der angegebene Spieler gewonnen hat.
- `get_user_move(board)`: Fordert den Benutzer auf, einen Zug einzugeben und validiert ihn.
- `bot_move(board, player)`: Ermittelt den nächsten Zug des Bots.
- `main()`: Hauptfunktion, die das Spiel steuert.

## Hinweise

- Spieler werden durch die Symbole "❌" und "⭕️" dargestellt.
- Das Spielfeld wird durch Zahlen dargestellt, die den Spielzug repräsentieren.
- Der Bot verwendet eine einfache Strategie, um Züge zu machen.

## Spielmodi

1. **Bot gegen Spieler**: Der Bot spielt gegen den Benutzer.
2. **Spieler gegen Spieler**: Zwei Benutzer spielen gegeneinander.
3. **Beenden**: Beendet das Spiel.

## Autoren

Dieses Programm wurde von Fritz erstellt.

Genießen Sie das Spiel! 🎮
