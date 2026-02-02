import tkinter as tk

# --- Constants ---
WIDTH, HEIGHT = 800, 300
GROUND_Y = 260
PLAYER_SIZE = 20
GRAVITY = 1
JUMP_VEL = -12
SPEED = 5
WAVE_SPEED = 6


class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.mode = "cube"  # cube | wave
        self.running = True

        # Player
        self.x = 100
        self.y = GROUND_Y - PLAYER_SIZE
        self.vel_y = 0
        self.wave_dir = -1
        self.holding = False

        self.player = self.canvas.create_rectangle(
            self.x, self.y, self.x + PLAYER_SIZE, self.y + PLAYER_SIZE, fill="cyan"
        )

        self.spikes = []
        self.spawn_spike()

        root.bind("<space>", self.press)
        root.bind("<KeyRelease-space>", self.release)
        root.bind("w", self.toggle_mode)

        self.update()

    def toggle_mode(self, event=None):
        self.mode = "wave" if self.mode == "cube" else "cube"
        self.vel_y = 0

    def press(self, event=None):
        self.holding = True
        if self.mode == "cube" and self.y >= GROUND_Y - PLAYER_SIZE:
            self.vel_y = JUMP_VEL

    def release(self, event=None):
        self.holding = False

    def spawn_spike(self):
        x = WIDTH
        spike = self.canvas.create_polygon(
            x, GROUND_Y, x + 20, GROUND_Y, x + 10, GROUND_Y - 20, fill="red"
        )
        self.spikes.append(spike)

    def update_cube(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y

        if self.y >= GROUND_Y - PLAYER_SIZE:
            self.y = GROUND_Y - PLAYER_SIZE
            self.vel_y = 0

    def update_wave(self):
        self.wave_dir = -1 if self.holding else 1
        self.y += self.wave_dir * WAVE_SPEED

        if self.y <= 0 or self.y + PLAYER_SIZE >= GROUND_Y:
            self.game_over()

    def update(self):
        if not self.running:
            return

        if self.mode == "cube":
            self.update_cube()
        else:
            self.update_wave()

        self.canvas.coords(
            self.player, self.x, self.y, self.x + PLAYER_SIZE, self.y + PLAYER_SIZE
        )

        for spike in self.spikes:
            self.canvas.move(spike, -SPEED, 0)
            if self.check_collision(spike):
                self.game_over()
                return

        if self.canvas.coords(self.spikes[-1])[0] < WIDTH - 200:
            self.spawn_spike()

        self.root.after(16, self.update)

    def check_collision(self, spike):
        px1, py1, px2, py2 = self.canvas.coords(self.player)
        sx1, sy1, sx2, sy2 = self.canvas.bbox(spike)
        return not (px2 < sx1 or px1 > sx2 or py2 < sy1 or py1 > sy2)

    def game_over(self):
        self.running = False
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2, text="GAME OVER", fill="white", font=("Arial", 32)
        )


root = tk.Tk()
root.title("Geometry Dash – Cube & Wave")
Game(root)
root.mainloop()
