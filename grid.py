import pygame
import numpy as np

class Grid:
    def __init__(self, screen, width, height, block_size):
        self.screen = screen
        self.width = width
        self.height = height
        self.block_size = block_size
        self.cols = width // block_size
        self.rows = height // block_size
        self.states = np.zeros((self.rows, self.cols), dtype=int)
        self.grid_rects = [pygame.Rect(x * block_size, y * block_size, block_size, block_size)
                           for x in range(self.cols) for y in range(self.rows)]

    def draw(self, color_alive, color_die, color_grid):
        for index, rect in enumerate(self.grid_rects):
            x, y = index % self.cols, index // self.cols
            color = color_alive if self.states[y, x] == 1 else color_die
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, color_grid, rect, 1)

    def update_state(self):
        new_state = np.copy(self.states)
        for x in range(self.cols):
            for y in range(self.rows):
                InLife = sum(
                    self.states[y + dy, x + dx]
                    for dx in [-1, 0, 1] for dy in [-1, 0, 1]
                    if (dx != 0 or dy != 0) and (0 <= x + dx < self.cols) and (0 <= y + dy < self.rows)
                )
                if self.states[y, x] == 1 and (InLife < 2 or InLife > 3):
                    new_state[y, x] = 0
                elif self.states[y, x] == 0 and InLife == 3:
                    new_state[y, x] = 1
        self.states = new_state

    def check_collision(self, mouse_pos):
        for index, rect in enumerate(self.grid_rects):
            if rect.collidepoint(mouse_pos):
                x, y = index % self.cols, index // self.cols
                self.states[y, x] ^= 1  # Toggle between 0 and 1
