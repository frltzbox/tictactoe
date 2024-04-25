# Tic Tac Toe Spiel

## Übersicht

Dieses Projekt implementiert eine einfache Befehlszeilenversion des klassischen Spiels Tic Tac Toe in Python. Das Spiel kann in zwei Modi gespielt werden:

1. Spieler gegen Bot: Ein menschlicher Spieler spielt gegen einen KI-Bot.
2. Spieler gegen Spieler: Zwei menschliche Spieler spielen abwechselnd gegeneinander.

## Funktionen

- Unterstützt zwei Spielmodi: Spieler gegen Bot und Spieler gegen Spieler.
- Der Bot implementiert eine grundlegende Strategie, um Züge zu machen, und kann den Gegner am Gewinnen hindern.
- Das Spiel zeigt das Tic Tac Toe-Spielfeld in der Befehlszeilenschnittstelle an.
- Am Ende jedes Spiels wird der Spieler aufgefordert, erneut zu spielen oder das Spiel zu beenden.

## Verwendete Technologien

- Python: Die Kernprogrammiersprache, die für die Implementierung verwendet wird.
- Random-Modul: Wird verwendet, um zufällige Züge für den Bot zu machen.
- Zeitmodul: Wird verwendet, um Verzögerungen während des Zuges des Bots hinzuzufügen.
- OS-Modul: Wird verwendet, um den Konsolenbildschirm zu löschen.

## Spielanleitung

1. Klonen Sie das Repository oder kopieren Sie den bereitgestellten Python-Code in eine Python-Umgebung.
2. Führen Sie das Python-Skript (`tictactoe.py`) aus.
3. Wählen Sie den Spielmodus: Spieler gegen Bot oder Spieler gegen Spieler.
4. Befolgen Sie die Anweisungen, um Züge zu machen.
5. Viel Spaß beim Spielen!

## Implementierungsdetails

- Das Spielbrett wird als 3x3-Raster mit einer verschachtelten Liste dargestellt.
- Die Hauptspiellogik ist in der Funktion `main()` implementiert, die das Spiel einrichtet, Spielerinput entgegennimmt und Bot-Züge macht.
- Die Strategie des Bots besteht darin, nach Gewinnzügen zu suchen und die Gewinnzüge des Gegners zu blockieren.
- Die Funktion `check_win()` überprüft nach jedem Zug das Spielbrett auf Gewinnkombinationen.
- Die Funktion `feld_malen()` druckt das Tic Tac Toe-Spielbrett in einem benutzerfreundlichen Format.

## Weitere Verbesserungen

- Implementieren Sie anspruchsvollere KI-Algorithmen wie Minimax mit Alpha-Beta-Pruning oder Monte Carlo Tree Search (MCTS), um den Bot intelligenter zu machen.
- Fügen Sie eine grafische Benutzeroberfläche (GUI) hinzu, um das Benutzererlebnis zu verbessern.
- Implementieren Sie Mehrspielerfunktionalität über ein Netzwerk, um Online-Spiel zu ermöglichen.

## Fazit

Das Tic Tac Toe-Spielprojekt bietet die Möglichkeit, grundlegende Python-Programmierkenntnisse zu üben, während ein unterhaltsames und interaktives Spiel erstellt wird. Durch die Erweiterung dieses Projekts können Entwickler fortgeschrittenere KI-Techniken und Benutzeroberflächendesigns erkunden.
