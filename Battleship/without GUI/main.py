"""
Steps:
    1. Create the board: Done
        1.1. Create the board with variable length and width: Done
        1.2. Place ships within the board: Done
    2. Show the board: Done
    3. User input row and column: Done
    4. Check if its a ship or its nothing: Done
        4.1. If its a ship, place S: Done
        4.2. if its not a ship, place X and decrease lives by 1: Done
    5. Win condition: Done
        5.1. If lives are 0, lose: Done
        5.2. If all ships are gone, 
"""
import random


class Game:
    def __init__(self, length: int = 5, width: int = 5, num_ships:int = 2, lives: int = 3) -> None:
        self.length = length
        self.width = width 
        self.num_ships = num_ships
        self.lives = lives
        self.board = self.make_board()
        self.taken_coordinates = set()
        self.ship_coordinates = set()
        
    def __str__(self) -> str:
        board = f""
        for row, row_board in enumerate(self.board):
            for col, col_board in enumerate(row_board):
                if (row, col) not in self.taken_coordinates:
                    if col == self.width - 1:
                        board += f"X\n"
                    else:
                        board += f"X "
                else:
                    if col == self.width - 1:
                        board += f"{col_board}\n"
                    else:
                        board += f"{col_board} "
                    
        return board
    
    def make_board(self) -> list[list[str]]:
        board = [["O" for col in range(self.width)] for row in range(self.length)]
        self.place_ships(board)
        return board
    
    def place_ships(self, board: list[list[str]]) -> None:
        placed_ships = 0
        while placed_ships < self.num_ships:
            row, col = random.randrange(0, self.length), random.randrange(0, self.width)
            if board[row][col] != "S":
                board[row][col] = "S"
                placed_ships += 1
    
    def player_input(self) -> None:
        while True:
            try:
                row = int(input("Enter your desired row: ")) - 1
                col = int(input("Enter your desired column: ")) - 1
                self.board[row][col]
            except ValueError:
                print("Invalid Number!")
                continue
            except IndexError:
                print("Position does not exist!")
                continue
            
            if (row, col) in self.taken_coordinates:
                print("You already guessed that!")
                continue
            
            self.position_checker(row, col)
            break
            
    def position_checker(self, row: int, col: int) -> None:
        if self.board[row][col] == "S":
            self.ship_coordinates.add((row,col))
            self.taken_coordinates.add((row,col))
        else:
            self.taken_coordinates.add((row,col))

def main():
    game = Game()
    while len(game.taken_coordinates) < game.lives:
        print(game)
        game.player_input()
        
        if len(game.ship_coordinates) == game.num_ships:
            print("You win!")
            break
        
    print("You lost!")
    
    
if __name__ == "__main__":
    main()