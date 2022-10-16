# STEPS TO CREATE SNAKE
# 1. divide grid to a grid of specific value: Done
# 2. create food: Done
#  2a. Place foodL Done
#  2b. Randomly place food
# 3. create snake: only Head
#  3a. when snake eat food, it extends snake
#  3b. if snake hits wall or itself, game over.
#  3c. Place both head and food in a fixed position at the start.
# 4. Move snake in a constant time, and per block only
# 5. If snake eats



import pygame as pg
import random


class SnakeGame:
    def __init__(self, window_length=800, window_height=800, grid_size=160):
        pg.init()
        
        if window_length % grid_size == 0:
            self.window_length = window_length
            self.window_height = window_height
        else:
            self.window_length = window_length + (grid_size - (window_length % grid_size)) # we take the remainder then subtract that to the grid size then add it to
            self.window_height = window_height + (grid_size - (window_height % grid_size)) # the dimension to make them fully divisible

        self.grid_size = grid_size
        self.window = pg.display.set_mode((self.window_length, self.window_height))
        
        if (self.window_length % grid_size) % 2 != 0: # the grid amount is odd
            self.snake_head = pg.Rect(self.window_length//grid_size+1, self.window_height//grid_size + 1, grid_size, grid_size)
        else:
            self.snake_head = pg.Rect(
                grid_size, grid_size * ((self.window_height//grid_size)//2), grid_size, grid_size   
                # we put the snake head at the middle of the grid, then second column from the left
                )
            
        self.xapple = self.window_length - grid_size * 2
        self.yapple = grid_size * ((self.window_height//grid_size)//2)
        
        self.apple = pg.Rect(
            self.window_length - grid_size*2, grid_size * ((self.window_height//grid_size)//2), 
            grid_size, grid_size
            # we put it on the right side then second column from the right
        )

        # self.snake_head = pg.Rect()
        self.snake_body: list[pg.Rect] = []
    
    def play(self):
        snake_x = 0
        snake_y = 0
        while True:
            print(snake_x, snake_y)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_w or event.key == pg.K_UP: # stops horizontal movement and start upward vertical movement
                        snake_y = -1 # NOTE: REMEMBER THAT POSITIVE Y IS DOWNWARD, AND UPWARD IS NEGATIVE Y
                        snake_x = 0
                        
                    elif event.key == pg.K_s or event.key == pg.K_DOWN:
                        snake_y = 1
                        snake_x = 0
                    
                    elif event.key == pg.K_a or event.key == pg.K_LEFT:
                        snake_y = 0 # Stops vertical movement and starts horizontal movement
                        snake_x = -1
                    
                    elif event.key == pg.K_d or event.key == pg.K_RIGHT:
                        snake_y = 0
                        snake_x = 1
                        
            self.show_board()
            
            pg.draw.rect(self.window, "#0000FF", self.snake_head) # draw the snake head
            pg.draw.rect(self.window, "#FF0000", self.apple) # draw the apple
            pg.display.update()
    
    def show_board(self):
        for row in range(self.window_length//self.grid_size):
            for col in range(self.window_length//self.grid_size):
                pg.draw.rect(self.window, "#FFFFFF", pg.Rect(
                    row*self.grid_size, col*self.grid_size, self.grid_size, self.grid_size), 1)
    
def main():
    game = SnakeGame()
    game.play()


if __name__ == '__main__':
    main()
    