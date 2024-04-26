class GameControl:
    def __init__(self):
        self.is_updating = False
        self.fps = 30

    def toggle_update(self):
        self.is_updating = not self.is_updating

    def adjust_fps(self, increment):
        self.fps += increment * 10
        self.fps = max(10, min(self.fps, 60))
