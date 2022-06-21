"""
Steps:
    1. Create the board: Done
        1.1. Create the board with variable length and width: Done
        1.2. Place ships within the board: Done
    2. Show the board: Done
        2.1. Show the board in pygame:  Done
        2.2. Show the board in variable length and width: Done
    3. User click the rectangle:    Done
    4. Check if its a ship or its nothing:  Done
        4.1. If its a ship, place a green rectangle:    Done
        4.2. if its not a ship, place a red rectangle and decrease lives by 1:  Done
    5. Win condition:   Done
        5.1. If lives are 0, lose:  Done
        5.2. If all ships are gone, show a winning screen: Doing
"""


import random
import pygame as pg
import time


class Board:
    def __init__(self, length, width, num_ships):
        self.length: int = length
        self.width: int = width
        self.num_ships: int = num_ships
        self.board = self.make_board()

    def __str__(self):
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
    
    def make_board(self):
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
    


class Game(Board):
    def __init__(self, length: int = 5, width: int = 5, num_ships: int = 2, window_length : int = 800, window_width : int = 800):
        super().__init__(length, width, num_ships)
        pg.init()
        # self.lives = self.player_lives()
        self.window_length = window_length
        self.window_width = window_width
        self.taken_coordinates = set()
        self.menu_rects = []
        self.board_rects = []
        self.window = pg.display.set_mode((window_length, window_width))
        self.text = pg.font.Font(None, 62)
        self.make_pg_board()
        
    # def player_lives(self) -> int:
    #     while True:
    #         try:
    #             lives = int(input("Input your lives:"))
    #         except ValueError:
    #             print("Inputted an invalid number, your lives are by default: 5")
    #             return 5
            
    #         if lives < 0:
    #             print("Inputted an invalid number, your lives are by default: 5")
    #             return 5
            
    #         elif lives > (self.length*self.width)/3:
    #             print("Your lives are greater than the third of all squares.")
    #             continue
            
    #         elif lives < 5:
    #             print("Oh? Daring are we? You have less than 5 lives, Continue?")
    #             yes_or_no = input("Yes or No: ")
    #             if yes_or_no.lower() == "yes":
    #                 return lives
    #             else:
    #                 continue
            
    #         return lives

    def player_lives_in_pg(self, number : str) -> int:
        try:
            life = int(number)
        except ValueError:
            # raise ValueError("Invalid number")
            return False
        
        if life > self.length*self.width//3:
            return -1
        
        return life

    def make_pg_board(self) -> None:    # Just creates the pg board and assigns the coordinates for showing it
        for row in range(self.length):
            rects_to_append = []
            for col in range(self.width):
                rects_to_append.append(pg.Rect((self.window_length//self.length * col, self.window_width//self.width * row), (self.window_length//self.length, self.window_width//self.width)))
            self.board_rects.append(rects_to_append)
    
    def make_menu(self) -> None:
        input_box = pg.Rect(self.window_length/3, self.window_width/2, self.window_length//3, 50)   #create a rectangle for input box
        self.menu_rects.append(input_box)
        return input_box    #return the rectangle for drawing and assigning the activity
            
    def show_board(self) -> None:
        for row, rects_of_rects in enumerate(self.board_rects):   # Shows the rectangles in pygame
            for col, rect in enumerate(rects_of_rects):
                if (row, col) in self.taken_coordinates:    # If the rectangle is clicked/already clicked
                    if self.board[row][col] != "S":         # If the rectangle is not a ship
                        pg.draw.rect(self.window, "#FF0000", rect)  # Draw a red rectangle
                    elif self.board[row][col] == "S":       # If the rectangle is a ship
                        pg.draw.rect(self.window, "#00FF00", rect)  # Draw a green rectangle
                else:
                    pg.draw.rect(self.window, "#000000", rect)  # IF not yet clicked, draw a black rectangle
        
        
        for column in range(1, self.length):   # Only need 4 lines, and we dont want 0 for column
            pg.draw.line(self.window, "#FFFFFF", (self.window_length//self.length * column, 0), (self.window_length//self.length * column, self.window_width), 3)
        
        for row in range(1, self.length): # same as above, but we're using window_width and width now
            pg.draw.line(self.window, "#FFFFFF", (0, self.window_width//self.width * row), (self.window_length, self.window_width//self.width * row), 3)
   
    def check_board(self, row : int, col : int) -> None:
        if self.board[row][col] == "S":
            return True
        
        elif self.board[row][col] != "S":
            self.lives -= 1
            return False
   
    def check_rect_input(self, mouse_x, mouse_y) -> None:
        for row, listed_rects in enumerate(self.board_rects):
            for col, rect in enumerate(listed_rects):
                if rect.collidepoint(mouse_x, mouse_y):
                    if (row, col) not in self.taken_coordinates:
                        self.taken_coordinates.add((row, col))
                        self.check_board(row, col)
    
    def show_menu(self) -> None:
        text_box = self.make_menu()
        is_text_box_active = False  #necessary to check if the rect is clicked and rdy for typing
        user_text = ""  #text that will be displayed
        menu_text = "Input your lives:"
        running = True
        while running:
            self.window.fill("#000000")
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if text_box.collidepoint(event.pos):
                        is_text_box_active = True   #if the rect is clicked, the text box is active
                    else:
                        is_text_box_active = False  #if any other thing is clicked, the text box is disabled
                
                elif event.type == pg.KEYDOWN:
                    if is_text_box_active:
                        if event.key == pg.K_BACKSPACE:
                            user_text = user_text[:-1]
                        elif event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                            self.lives = self.player_lives_in_pg(user_text)
                            if not self.lives:
                                user_text = ""
                                continue
                            if self.lives < 0:
                                menu_text = f"""Lives greater than 1/3 of all squares."""
                                user_text = ""
                                continue
                            
                            running = False
                        else:
                            user_text += event.unicode
            
            for rect in self.menu_rects:
                if is_text_box_active:
                    pg.draw.rect(self.window, "#FFFFFF", rect)
                else:
                    pg.draw.rect(self.window, "#FFFFFF", rect, 1)
                    
            user_text_surface = self.text.render(user_text, True, (0,0,0))
            user_text_rect = user_text_surface.get_rect(center=text_box.center)
            menu_text_surface = self.text.render(menu_text, True, "#FFFFFF")
            menu_text_rect = menu_text_surface.get_rect(center=(text_box.center[0], text_box.center[1] - 300))
            self.window.blit(user_text_surface, user_text_rect)
            self.window.blit(menu_text_surface, menu_text_rect)
            
            pg.display.update()
                    
    def show_end_screen(self):
        self.window.fill("#000000")
        if self.lives:  # if the player has lives at the end of the game
            end_text = f"You won with {self.lives} lives left!" 
            end_text_surface = self.text.render(end_text, True, "#FFFFFF")
            end_text_rect = end_text_surface.get_rect(center=(self.window_length/2, self.window_width/2))   #centers the text
            self.window.blit(end_text_surface, end_text_rect)
            pg.display.update()
            time.sleep(3)   # sleep to stick the text longer
        else:
            end_text = "You lost!"
            end_text_surface = self.text.render(end_text, True, "#FFFFFF")
            end_text_rect = end_text_surface.get_rect(center=(self.window_length/2, self.window_width/2))   #centers the text
            self.window.blit(end_text_surface, end_text_rect)
            pg.display.update()
            time.sleep(3)   # sleep to stick the text longer
            
    
    def play(self):
        self.show_menu()
        while self.lives > 0:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    self.check_rect_input(mouse_x, mouse_y)
            
            self.show_board()
            pg.display.update()
        
        self.show_end_screen()
    
def main():
    g = Game()
    g.play()
    

if __name__ == "__main__":
    main()


