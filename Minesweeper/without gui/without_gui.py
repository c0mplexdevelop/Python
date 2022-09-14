# Steps
# 1. create the board: Done
#   1a. place bombs on the board: Done
#   1b. Put values on the board depending on the amount of bombs: Done
# 2. Show the board: Done
#   2a. Show the updated board after every move
# 3. User input a row, col to dig at
#   3a. Dig continuously until at the end, or the edge sides are the bomb
#   3b. If bomb, gg. If all squares w/o bombs dug, gg win.


import random


class Minesweeper:
    def __init__(self, num_bomb: int = 2, size: int = 5):
        self.num_bomb = num_bomb
        self.size = size
        self.board = self.make_board()
        self.dug = set()
        
        self.get_values_on_board()
        

    def __str__(self):
        board = ""  #visual representation of the board
        for row, columns in enumerate(self.board):
            for col, value in enumerate(columns):
                if (row, col) not in self.dug:
                    if col == self.size - 1:
                        board += f" \n"
                    else:
                        board += f" |"
                    continue
                
                if col == self.size - 1:
                    board += f"{value}\n"
                else:
                    board += f"{value}|"

        return board

    def make_board(self) -> list[str]:
        board = [[" " for i in range(self.size)] for j in range(self.size)]  # create a 2d board
        return self.place_bombs(board)  # runs the place_bomb function
    
    def place_bombs(self, board) -> list[str]:
        placed_bomb = 0
        while placed_bomb < self.num_bomb:
            row, col = random.randrange(0, self.size), random.randrange(0, self.size)   # assigns a row and col, upper limit is size-1
            if board[row][col] == "*": # if its a bomb, redo the loop
                continue
            
            board[row][col] = "*"   # if its empty, place a bomb
            placed_bomb += 1    # increments placed_bomb counter
        
        return board

    def get_values_on_board(self) -> None:
        for row, columns in enumerate(self.board):
            for col, value in enumerate(columns):
                if self.board[row][col] == "*":
                    continue
                score = self.assign_values_on_board(row, col)
                self.board[row][col] = score

    def assign_values_on_board(self, row_index: int, col_index: int) -> int:
        amount_of_bombs = 0
        for row in range(max(0, row_index-1), min(self.size , row_index+2)): # checks all the rows, if its over or under the index, prevents it by taking the min/max valid value
            for col in range(max(0, col_index-1), min(self.size, col_index+2)): # same as the row part
                # NOTE: the self.size is not subtracted by one as range only checks until max-1, and col-index is added by two
                # since col_index + 1 is one value under the upper limit of the list since max-1 also applies
                # hence adding another 1 prevent the problem
                if row == row_index and col == col_index:   # if its the same index, just iterate over
                    continue
                
                if self.board[row][col] == "*":
                    amount_of_bombs += 1
        
        return amount_of_bombs
    
    def dig(self, row_index, col_index) -> bool:
        # We're doing the digging recursively, so we need to check at the front to stop an endless loop
        if self.board[row_index][col_index] == "*": # if the recursive dig is a bomb, dont dig
            return False
        
        elif self.board[row_index][col_index] > 0: # if the recursive dig is a number, means there is a bomb nearby, dont dig further
            self.dug.add((row_index, col_index))
            return True

        self.dug.add((row_index, col_index))
        for row in range(max(0, row_index-1), min(self.size, row_index+2)): # borrow code from assign_values_on_board
            for col in range(max(0, col_index-1), min(self.size, col_index+2)):
                if row == row_index and col == col_index:
                    continue
                elif (row, col) in self.dug:
                    continue

                self.dig(row, col) # dig again at the new spot
                
        return True # means its neither a square with bombs, or a bomb
        
        

    def player_input(self):
        while True:
            row = int(input("Input a row: ")) - 1
            col = int(input("Input a column: ")) - 1
            # means the player indicated an invalid position (above or below valid index values)
            if row >= self.size or col >= self.size or row < 0 or col < 0:
                continue

            return self.dig(row, col) # dig at the spot indicated by the player


def main():
    game = Minesweeper()
    available_area = game.size**2 - game.num_bomb
    while len(game.dug) < available_area:
        print(game)
        game_status = game.player_input()
        if not game_status: # dug a bomb, HA idiot!
            print("You lose")
            return
    
    print(game) # you won, show the board one last time
    print("You won!")
    

if __name__ == "__main__":
    main()