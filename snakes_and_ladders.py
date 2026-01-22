import random

class SnakesAndLadders:
    def __init__(self, num_players=2):
        self.board_size = 100
        self.num_players = num_players
        self.player_positions = [0] * num_players

        # Define snakes (head -> tail)
        self.snakes = {
            16: 6,
            47: 26,
            49: 11,
            56: 53,
            62: 19,
            64: 60,
            87: 24,
            93: 73,
            95: 75,
            98: 78
        }

        # Define ladders (bottom -> top)
        self.ladders = {
            1: 38,
            4: 14,
            9: 31,
            21: 42,
            28: 84,
            36: 44,
            51: 67,
            71: 91,
            80: 100
        }

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player_num, dice_roll):
        current_pos = self.player_positions[player_num]
        new_pos = current_pos + dice_roll

        # Check if move exceeds board size
        if new_pos > self.board_size:
            return current_pos, "Position exceeds 100, staying at current position"

        # Check for ladder
        if new_pos in self.ladders:
            final_pos = self.ladders[new_pos]
            self.player_positions[player_num] = final_pos
            return final_pos, f"Ladder! Climbed from {new_pos} to {final_pos}"

        # Check for snake
        if new_pos in self.snakes:
            final_pos = self.snakes[new_pos]
            self.player_positions[player_num] = final_pos
            return final_pos, f"Snake! Slid from {new_pos} to {final_pos}"

        # Normal move
        self.player_positions[player_num] = new_pos
        return new_pos, f"Moved to {new_pos}"

    def check_winner(self, player_num):
        return self.player_positions[player_num] == self.board_size

    def display_board(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n" + "="*80)
        print(" " * 25 + "SNAKES AND LADDERS")
        print("="*80)

        # Create a 10x10 board
        board = []
        for row in range(10):
            if row % 2 == 0:
                # Even rows: left to right
                board.append(list(range(100 - row * 10, 90 - row * 10, -1)))
            else:
                # Odd rows: right to left
                board.append(list(range(91 - row * 10, 101 - row * 10)))

        # Display the board
        for row in board:
            # Print top border
            print("+" + "-------+" * 10)

            # Print cell content with player positions
            line = "|"
            for cell in row:
                cell_content = f"{cell:3}"

                # Check if any player is on this cell
                players_here = [i+1 for i in range(self.num_players)
                               if self.player_positions[i] == cell]

                if players_here:
                    player_str = "".join([f"P{p}" for p in players_here])
                    cell_content = f"{player_str:^7}"
                elif cell in self.snakes:
                    cell_content = f"{cell:3}->S"
                elif cell in self.ladders:
                    cell_content = f"{cell:3}->L"
                else:
                    cell_content = f"  {cell:3} "

                line += cell_content + "|"
            print(line)

        # Print bottom border
        print("+" + "-------+" * 10)

        # Print legend and player positions
        print("\n" + "="*80)
        print("LEGEND: S=Snake Head, L=Ladder Bottom, P1/P2/P3/P4=Players")
        print("="*80)
        print("CURRENT POSITIONS:")
        for i in range(self.num_players):
            marker = "<<< YOU" if i == getattr(self, 'current_player', 0) else ""
            print(f"  Player {i+1}: Position {self.player_positions[i]} {marker}")
        print("="*80 + "\n")

    def play(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Welcome to Snakes and Ladders!")
        print(f"Number of players: {self.num_players}")
        print(f"Goal: Reach position {self.board_size}")
        print("\nSnakes at positions:", ", ".join([f"{k}->{v}" for k, v in list(self.snakes.items())[:5]]), "...")
        print("Ladders at positions:", ", ".join([f"{k}->{v}" for k, v in list(self.ladders.items())[:5]]), "...")

        input("\nPress Enter to start the game...")

        self.current_player = 0

        while True:
            self.display_board()
            input(f"\nPlayer {self.current_player + 1}'s turn. Press Enter to roll the dice...")

            dice_roll = self.roll_dice()
            print(f"\nPlayer {self.current_player + 1} rolled a {dice_roll}")

            new_pos, message = self.move_player(self.current_player, dice_roll)
            print(message)

            # Check for winner
            if self.check_winner(self.current_player):
                self.display_board()
                print(f"\n{'*'*50}")
                print(f"PLAYER {self.current_player + 1} WINS!")
                print(f"{'*'*50}\n")
                break

            input("\nPress Enter to continue...")

            # Move to next player
            self.current_player = (self.current_player + 1) % self.num_players

if __name__ == "__main__":
    print("How many players? (2-4): ", end="")
    try:
        num_players = int(input())
        if num_players < 2 or num_players > 4:
            print("Invalid number of players. Using 2 players.")
            num_players = 2
    except:
        print("Invalid input. Using 2 players.")
        num_players = 2

    game = SnakesAndLadders(num_players)
    game.play()
