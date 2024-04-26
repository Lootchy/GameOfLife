
import numpy as np
import pygame
from grid import Grid
from gamecontrol import GameControl

class MainApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.grid = Grid(self.screen, 800, 800, 20)
        self.controls = GameControl()
        self.run = True

    def run_game(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
                    elif event.key == pygame.K_SPACE:
                        self.controls.toggle_update()
                    elif event.key == pygame.K_LEFT:
                        self.controls.adjust_fps(-1)
                    elif event.key == pygame.K_RIGHT:
                        self.controls.adjust_fps(1)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                    mouse_pos = pygame.mouse.get_pos()
                    self.grid.check_collision(mouse_pos)


            if self.controls.is_updating:
                self.grid.update_state()

            self.screen.fill((10, 10, 10))
            self.grid.draw((255, 255, 255), (170, 170, 170), (40, 40, 40))
            pygame.display.flip()
            self.clock.tick(self.controls.fps)

        pygame.quit()

if __name__ == "__main__":
    app = MainApp()
    app.run_game()
