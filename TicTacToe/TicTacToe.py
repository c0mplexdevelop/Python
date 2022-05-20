import time
import pygame as pg

pg.init()


class Game:
    def __init__(self, window_length: int =800, window_height: int = 600):
        self.window_length = window_length
        self.window_height = window_height
        self.winner: str = ""
        self.positions = {1: "", 2: "", 3: "",
                          4: "", 5: "", 6: "",
                          7: "", 8: "", 9: ""}
        self.winning_positions = [[7, 8, 9], [4, 5, 6], [1, 2, 3],
                                  [7, 4, 1], [8, 5, 2], [9, 6, 3],
                                  [7, 5, 3], [9, 5, 1]]
        self.font = pg.font.SysFont("Arial", 200)
        self.X = self.font.render("X", 1, "#FFFFFF")
        self.O = self.font.render("O", 1, "#FFFFFF")
        self.rects = self.make_board_pygame()
        self.window = pg.display.set_mode((self.window_length,self.window_height))

    # def player_input(self, player_letter: str) -> None:
    #     while True:
    #         position = int(input(f"{player_letter}, Input the desired position: "))
    #         if self.positions[position]:
    #             print(f"Position already taken by {self.positions[position]}")
    #             continue
    #         self.positions[position] = player_letter
    #         break

    def check_for_winner(self) -> bool:
        for x, y, z in self.winning_positions:
            if self.positions[x] == self.positions[y] == self.positions[z] != "":# checks if the triples are alike
                pg.draw.line(self.window, "#00FFFF", (self.rects[x-1].center[0], self.rects[x-1].center[1]),       #draws a line from center of x rect to z rect in either hori, verti, diagonal direction
                             (self.rects[z-1].center[0], self.rects[z-1].center[1]), 19)
                self.winner = self.positions[x]
                return True
        return False

    def click_rect(self, mouse_x, mouse_y, letter:str):
        for position, rect in enumerate(self.rects):
            if rect.collidepoint(mouse_x, mouse_y):
                if self.positions[position+1] == "":
                    self.positions[position+1] = letter
                else:
                    break

    def make_board_pygame(self) -> None:
        rects = []
        for position in self.positions:
            if position <= 3:
                # places rects at the third row
                rects.append(pg.Rect((position - 1)*self.window_length/3, self.window_height /3 * 2 + 2, 
                                     self.window_length//3+1, self.window_height//3))
            elif position <= 6:
                # places rects at the second row
                rects.append(pg.Rect((position - 4)*self.window_length/3, self.window_height/3 + 2, 
                                     self.window_length//3+1, self.window_height//3))
            else:
                # places rects at the first row
                rects.append(pg.Rect((position - 7)*self.window_length/3, 0,
                                     self.window_length//3+1, self.window_height//3))
        return rects
                

    def show_board_pygame(self) -> None:    
        for idx, rect in enumerate(self.rects):
            if idx <= 2:
                if self.positions[idx+1] == "X":
                    self.window.blit(self.X, (rect.midtop[0]-50, rect.midtop[1]))
                elif self.positions[idx+1] == "O":
                    self.window.blit(self.O, (rect.midtop[0]-60, rect.midtop[1]))
                else:
                    pg.draw.rect(self.window, "#000000", rect)
            elif idx <= 5:
                if self.positions[idx+1] == "X":
                    self.window.blit(
                        self.X, (rect.midtop[0]-50, rect.midtop[1]))
                elif self.positions[idx+1] == "O":
                    self.window.blit(
                        self.O, (rect.midtop[0]-60, rect.midtop[1]))
                else:
                    pg.draw.rect(self.window, "#000000", rect)
            elif idx <= 8:
                if self.positions[idx+1] == "X":
                    self.window.blit(
                        self.X, (rect.midtop[0]-50, rect.midtop[1]))
                elif self.positions[idx+1] == "O":
                    self.window.blit(
                        self.O, (rect.midtop[0]-60, rect.midtop[1]))
                else:
                    pg.draw.rect(self.window, "#000000", rect)
            
            
        pg.draw.line(self.window, "#FFFFFF", (self.window_length/ \
                     3, 0), (self.window_length/3, self.window_height), 7)
        pg.draw.line(self.window, "#FFFFFF",
                     (self.window_length/3 * 2, 0), (self.window_length/3 * 2, self.window_height), 7)
        pg.draw.line(self.window, "#FFFFFF", (0, self.window_height/3),
                     (self.window_length, self.window_height/3), 7)
        pg.draw.line(self.window, "#FFFFFF", (0, self.window_height /
                     3 * 2), (self.window_length, self.window_height/3 * 2), 7)

    def game_over(self):
        self.window.fill("#000000")
        pg.display.update()
        game_over_font = pg.font.SysFont("Times New Roman", 70)
        game_over_text = game_over_font.render(f"{self.winner} WON!", 1, "#FFFFFF")
        game_over_text_rect = game_over_text.get_rect(center=(self.window_length/2, self.window_height/2))
        self.window.blit(game_over_text, game_over_text_rect)
        pg.display.update()
        
    def play(self):
        player_turn = "X"
        turns = 0
        while turns < 9:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    self.click_rect(mouse_x, mouse_y, player_turn)
                    if player_turn == "X":
                        player_turn = "O"
                    else:
                        player_turn = "X"
                    print(self.positions)
                    
                    turns += 1
            if self.check_for_winner():
                self.show_board_pygame()
                pg.display.update()
                time.sleep(1.2)
                self.game_over()
                time.sleep(2)
                break

            self.show_board_pygame()
            pg.display.update()
                    

def main():
    g = Game()
    g.play()
            


if __name__ == "__main__":
    main()
