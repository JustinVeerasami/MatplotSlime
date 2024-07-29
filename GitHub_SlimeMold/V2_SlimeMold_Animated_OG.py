import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class PhysarumSim:
    def __init__(self, grid_size=100, num_iterations=1000):
        self.grid_size = grid_size
        self.num_iterations = num_iterations
        self.grid = np.zeros((grid_size, grid_size))
        self.particles = np.zeros((grid_size, grid_size))
        self.particles[:] = np.nan
        self.positions = []
        self.grid_frames = []  # List to store grid snapshots for animation

    def initParticles(self, num_particles=10):
        for _ in range(num_particles):
            x, y = np.random.randint(self.grid_size), np.random.randint(self.grid_size)
            self.particles[x, y] = 1
            self.positions.append((x, y))

    def updateParticles(self, batch_size=100):
        new_positions = []
        for pos in self.positions:
            x, y = pos
            dx, dy = self.movementPattern(x, y)
            new_x, new_y = (x + dx) % self.grid_size, (y + dy) % self.grid_size
            self.grid[new_x, new_y] += 1
            self.particles[new_x, new_y] = 1
            new_positions.append((new_x, new_y))
        self.positions = new_positions[:]  # Update positions after batch processing
        self.grid_frames.append(np.copy(self.grid))  # Store current grid state for animation

    def movementPattern(self, x, y):
        return np.random.choice([-1, 0, 1]), np.random.choice([-1, 0, 1])

    def runSimulation(self):
        self.initParticles()
        for _ in range(self.num_iterations):
            self.updateParticles()

    def graphVisual(self):
        plt.figure(figsize=(8, 6))
        normalized_grid = self.grid / np.max(self.grid)  # Normalize grid values
        plt.imshow(normalized_grid, cmap='inferno', interpolation='nearest')
        plt.title('Physarum polycephalum Simulation')
        plt.colorbar(label='Normalized Chemical Conc.')
        plt.show()

    def animate(self, batch_size=100, repeat=False):
        fig, ax = plt.subplots(figsize=(8, 6))
        img = ax.imshow(self.grid_frames[0], cmap='inferno', interpolation='nearest')
        plt.title('Physarum polycephalum Simulation')
        plt.colorbar(img, ax=ax, label='Normalized Chemical Conc.')

        def update(frame):
            for _ in range(batch_size):
                if frame * batch_size + _ < len(self.grid_frames):
                    img.set_array(self.grid_frames[frame * batch_size + _] / np.max(self.grid_frames[frame * batch_size + _]))
            return img,

        num_frames = (len(self.grid_frames) + batch_size - 1) // batch_size
        ani = FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True, repeat=repeat)
        
        # To ensure the animation stops at the end and does not repeat
        if not repeat:
            plt.show()
        
        return ani

sim = PhysarumSim(grid_size=100, num_iterations=4000)
sim.runSimulation()
# sim.graphVisual()  # Uncomment to show static gradient plot
ani = sim.animate(batch_size=50, repeat=False)  # Show animated gradient plot with batch processing and stop at end
plt.show()  # To display the animation in Jupyter or other environments
