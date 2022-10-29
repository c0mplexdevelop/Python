import pygame as pg
import random
from pygame.math import Vector2
from enum import Enum, auto


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


class Snake:
    def __init__(self, window_length=800, window_height=600, grid_size=100):
        self.window_length = window_length
        self.window_height = window_height
        self.grid_size = grid_size

        self.window = pg.display.set_mode(
            (self.window_length, self.window_height))

        # Vector 2 is just like tuples but mutable and easier to get x and y of (vector.x and vector.y).
        self.snake_body = [Vector2(3, 3), Vector2(2, 3), Vector2(1, 3)]

        self.apple = self.create_apple()

    def play(self):
        last_key = None

        # dir is a enum to disallow north -> south movement and east west and viceversa
        direction = None

        clock = pg.time.Clock()

        apple_eaten = False

        lost = False
        body_count = 3
        while True:
            clock.tick(3)   # runs at 3 fps maximum

            self.window.fill("#000000")
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w and last_key is not Direction.DOWN:
                        direction = Vector2(0, -1)
                        last_key = Direction.UP

                    elif event.key == pg.K_s and last_key is not Direction.UP:
                        direction = Vector2(0, 1)
                        last_key = Direction.DOWN

                    elif event.key == pg.K_a and last_key is not Direction.RIGHT:
                        direction = Vector2(-1, 0)
                        last_key = Direction.LEFT

                    elif event.key == pg.K_d and last_key is not Direction.LEFT:
                        direction = Vector2(1, 0)
                        last_key = Direction.RIGHT

            head_x = self.snake_body[0][0] * self.grid_size + 1
            head_y = self.snake_body[0][1] * self.grid_size + 1

            # check if the head is at the apple, if so, eats it.
            if (head_x, head_y) == self.apple.topleft:
                apple_eaten = True  # for snake extension

            if direction and not apple_eaten:
                self.move_snake(direction)
            elif direction and apple_eaten:
                self.move_snake_apple(direction)
                self.move_apple()
                apple_eaten = False  # reset the flag to avoid extending the snake infinitely

            self.show_board()

            self.show_apple()
            self.show_snake()

            # if any of this returns true, they lost
            if self.check_if_snake_eats_body() or self.check_if_head_past_border():
                lost = True
                break

            if body_count >= (self.window_length // self.grid_size) * (self.window_height // self.grid_size):   # they won
                break

            pg.display.flip()

        if lost:
            print("You lost!")
        else:
            print("You won!")

    def show_board(self):
        for row in range(self.window_length//self.grid_size):
            for col in range(self.window_height//self.grid_size):
                pg.draw.rect(self.window, "#FFFFFF", pg.Rect(
                    row*self.grid_size, col*self.grid_size, self.grid_size, self.grid_size), 1)

    def show_apple(self):
        pg.draw.rect(self.window, "#FF0000", self.apple)

    def show_snake(self):
        for idx, pos in enumerate(self.snake_body):
            x_pos = pos[0] * self.grid_size
            y_pos = pos[1] * self.grid_size

            # size is offset by 2 since the board borders take 1 px, so -2 to fit the rect to the hollowed board.
            # Coords are offset by 1 for the same reason
            rect = pg.Rect(x_pos + 1, y_pos + 1,
                           self.grid_size - 2, self.grid_size - 2)
            if idx == 0:
                pg.draw.rect(self.window, "#00FF00", rect)
            else:
                pg.draw.rect(self.window, "#0000FF", rect)

    def move_snake(self, direction: Vector2):
        """
        We copy the snake but not the tail, then we insert the new head at the start with its new position, then set the real body to the copy.
        Then we just draw it to another different function
        """
        body_copy = self.snake_body[:-1]
        body_copy.insert(0, body_copy[0] + direction)
        self.snake_body = body_copy

    def move_snake_apple(self, direction: Vector2):
        """
        This only runs if the apple_eaten flag is set to True
        This copy the entire snake_body, then inserts the new head with its new position.
        Since we included the tail, the snake extends by 1
        """
        body_copy = self.snake_body[:]
        body_copy.insert(0, body_copy[0] + direction)
        self.snake_body = body_copy

    def move_apple(self):
        while True:
            duplicate = False

            row = random.randrange(0, self.window_length // self.grid_size)
            col = random.randrange(0, self.window_height // self.grid_size)

            for vector in self.snake_body:
                # we are checking if the apple position is inside the snake, which shouldnt happen
                if row == vector.x and col == vector.y:
                    duplicate = True
                    break

            if duplicate:
                continue

            self.apple.topleft = row * self.grid_size + 1, col * self.grid_size + 1
            break

    def create_apple(self) -> pg.Rect:
        row = random.randrange(0, self.window_length // self.grid_size)
        col = random.randrange(0, self.window_height // self.grid_size)
        position = Vector2(row, col)
        return pg.Rect(position[0] * self.grid_size + 1, position[1] * self.grid_size + 1, self.grid_size - 2, self.grid_size - 2)

    def check_if_snake_eats_body(self):
        #We check if the head is inside the body, then if so, the player lost.
        head_vector = self.snake_body[0]
        for vector in self.snake_body[1:]:
            if head_vector == vector:
                return True

        return False

    def check_if_head_past_border(self):
        head_x = self.snake_body[0][0] * self.grid_size + 1
        head_y = self.snake_body[0][1] * self.grid_size + 1

        # check if the head is past the borders.
        if head_x < 0 or head_y < 0 or head_x > self.window_length or head_y > self.window_height:
            return True

        return False


def main():
    game = Snake()
    game.play()


if __name__ == "__main__":
    main()
