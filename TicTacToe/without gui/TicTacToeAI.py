import time


class Game:
    def __init__(self):
        self.positions = {1: "", 2: "", 3: "",
                          4: "", 5: "", 6: "",
                          7: "", 8: "", 9: ""}
        self.winning_positions = [[7, 8, 9], [4, 5, 6], [1, 2, 3], 
                                  [7, 4, 1], [8, 5, 2], [9, 6, 3], 
                                  [7, 5, 3], [9, 5, 1]]
        print("""
Welcome to Tic-Tac-Toe! Due to it being text-only, 
you will input your location like how it is in a numpad:
                7 8 9
                4 5 6
                1 2 3
          """)
        time.sleep(3)
        print(self)

    def __str__(self) -> str:
        return f"""
    {self.positions[7]:1}|{self.positions[8]:1}|{self.positions[9]:1}
    =====
    {self.positions[4]:1}|{self.positions[5]:1}|{self.positions[6]:1}
    =====
    {self.positions[1]:1}|{self.positions[2]:1}|{self.positions[3]:1}
    """
    
    def player_input(self, player_letter: str) -> None:
        while True:
            position = int(input(f"{player_letter}, Input the desired position: "))
            if self.positions[position]:
                print(f"Position already taken by {self.positions[position]}")
                continue
            self.positions[position] = player_letter
            break
                    
    def ai_input(self, ai_letter: str) -> None:
        best_score = -1000
        best_move = 0
        
        for position in self.positions:
            if not self.positions[position]:
                self.positions[position] = ai_letter
                score = self.minimax(ai_letter, False)
                self.positions[position] = ""
                if score > best_score:
                    best_score = score
                    best_move = position
                    
        self.positions[best_move] = ai_letter
    
    def minimax(self, letter: str, isMaximizing=False):
        player_letter = "X" if letter == "O" else "O"
        
        if self.check_for_winner(letter):
            return 1
        
        elif self.check_for_winner(player_letter):
            return -1
        
        elif not self.check_for_draw():
            return 0
        
        if isMaximizing:
            best_score = -10000

            for position in self.positions:
                if not self.positions[position]:
                    self.positions[position] = letter
                    score = self.minimax(letter, False)
                    self.positions[position] = ""
                    if score > best_score:
                        best_score = score
                        
            return best_score
        
        elif not isMaximizing:
            best_score = 10000
            
            for position in self.positions:
                if not self.positions[position]:
                    self.positions[position] = player_letter
                    score = self.minimax(letter, True)
                    self.positions[position] = ""
                    if score < best_score:
                        best_score = score
                        
            return best_score

            

        
    def check_for_draw(self):
        for position in self.positions:
            if not self.positions[position]:
                return True
        return False
        
        
    
    def check_for_winner(self, letter: str) -> bool:
        for x, y, z in self.winning_positions:
            if self.positions[x] == self.positions[y] == self.positions[z] == letter:
                return True
        return False
    
    
    
    
    
def main():
    while True:
        game = Game()
        while game.check_for_draw():
            game.player_input("X")
            print(game)
            if game.check_for_winner("X"):
                print("X won!")
                break

            game.ai_input("O")
            print(game)
            if game.check_for_winner("O"):
                print("O won!")
                break
        
        print("It's a draw!")
        restart = input("Would you like to restart (y/n)? ").lower()
        if restart in ("y", "yes"):
            continue
        return
        
if __name__ == "__main__":
    main()