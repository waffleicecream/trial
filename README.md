# Snakes and Ladders Game

A simple, interactive command-line implementation of the classic Snakes and Ladders board game with a visual ASCII board display.

## Features

- **Visual Board Display**: 10x10 grid showing all 100 positions
- **Multi-player Support**: 2-4 players can play together
- **Real-time Updates**: Board updates after each move showing player positions
- **Snake & Ladder Indicators**: Visual markers showing where snakes and ladders are located
- **Turn-based Gameplay**: Players take turns rolling dice and moving around the board
- **Clear Win Condition**: First player to reach position 100 wins

## Game Elements

### Snakes (10 total)
Snakes send you down when you land on their head:
- 16 → 6, 47 → 26, 49 → 11, 56 → 53, 62 → 19
- 64 → 60, 87 → 24, 93 → 73, 95 → 75, 98 → 78

### Ladders (9 total)
Ladders let you climb up when you land on their bottom:
- 1 → 38, 4 → 14, 9 → 31, 21 → 42, 28 → 84
- 36 → 44, 51 → 67, 71 → 91, 80 → 100

## How to Play

### Requirements
- Python 3.x

### Running the Game

```bash
python snakes_and_ladders.py
```

### Game Instructions

1. When prompted, enter the number of players (2-4)
2. Press Enter to start the game
3. On your turn, press Enter to roll the dice
4. Your piece will automatically move based on the dice roll
5. If you land on a ladder, you'll climb up
6. If you land on a snake, you'll slide down
7. The first player to reach position 100 wins

### Board Layout

The board is displayed in a snake pattern (boustrophedon):
```
100 99  98  97 ... 91
81  82  83  84 ... 90
80  79  78  77 ... 71
...
10  9   8   7  ... 1
```

### Legend
- **P1, P2, P3, P4**: Player positions
- **->S**: Snake head (will slide down)
- **->L**: Ladder bottom (will climb up)
- **<<< YOU**: Current player's turn indicator

## Example Gameplay

```
Player 1's turn. Press Enter to roll the dice...

Player 1 rolled a 4
Ladder! Climbed from 4 to 14

CURRENT POSITIONS:
  Player 1: Position 14 <<< YOU
  Player 2: Position 0
```

## Files

- `snakes_and_ladders.py`: Main game file containing all game logic
- `README.md`: This file
- `.gitignore`: Git ignore file for Python projects

## Future Enhancements

Possible improvements for future versions:
- Customizable board sizes
- Custom snake and ladder positions
- Game statistics and history
- Save and load game state
- Different game modes (speed mode, challenge mode, etc.)

## License

This is a simple educational project for learning Python and game development.