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
    
    def check_for_winner(self) -> bool:
        for x, y, z in self.winning_positions:
            if self.positions[x] == self.positions[y] == self.positions[z] != "":
                return True
        return False
    
def main():
    game = Game()
    while True:
        game.player_input("X")
        print(game)
        if game.check_for_winner():
            print("X won!")
            return
        game.player_input("O")
        print(game)
        if game.check_for_winner():
            print("O won!")
            return
        
if __name__ == "__main__":
    main()