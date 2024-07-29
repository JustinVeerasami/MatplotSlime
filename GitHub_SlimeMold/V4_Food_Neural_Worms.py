import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class PhysarumSim:
    def __init__(self, gridSize=100, numIterations=1000, batch_size=10, decay_rate=0.95):
        self.grid_size = gridSize
        self.num_iterations = numIterations
        self.batch_size = batch_size
        self.decay_rate = decay_rate
        self.grid = np.zeros((gridSize, gridSize))
        self.particles = np.zeros((gridSize, gridSize))
        self.foodParticles = []  # Store positions of food particles
        self.positions = []
        self.fig, self.ax = plt.subplots()
        self.im = None  # To store the image plot for updating

    def graphVisual(self):
        self.im = self.ax.imshow(self.grid, cmap='inferno', interpolation='nearest')
        for (fx, fy) in self.foodParticles:
            self.ax.plot(fy, fx, 'yo', markersize=8)  # Plot food particles as yellow circles
        
        self.ax.set_title('Slime Mold (Physarum) Simulation')
        self.fig.colorbar(self.im, ax=self.ax, label='Normalized Chemical Conc.')
        
        ani = FuncAnimation(self.fig, self.update_visualization, frames=self.num_iterations // self.batch_size,
                            interval=200, repeat=False)
        
        plt.show()

    def update_visualization(self, frame):
        for _ in range(self.batch_size):
            self.updateParticles()
            self.decayParticles()
        
        # Update the grid and particles
        self.im.set_data(self.grid)  # Update the data for the image plot
        
        return self.im,

    def initParticles(self, num_particles=5):
        for _ in range(num_particles):
            x, y = np.random.randint(self.grid_size), np.random.randint(self.grid_size)
            self.particles[x, y] = 1
            self.positions.append((x, y))
            self.grid[x, y] += 1  # Increment grid value for gradient effect

    def initFoodParticles(self, num_foodParticles=10):
        for _ in range(num_foodParticles):
            x, y = np.random.randint(self.grid_size), np.random.randint(self.grid_size)
            self.foodParticles.append((x, y))

    def movementPattern(self, x, y):
        # Example movement pattern, can be customized
        return np.random.choice([-1, 0, 1]), np.random.choice([-1, 0, 1])

    def updateParticles(self):
        new_positions = []
        for pos in self.positions:
            x, y = pos
            dx, dy = self.movementPattern(x, y)
            new_x, new_y = (x + dx) % self.grid_size, (y + dy) % self.grid_size
            self.grid[new_x, new_y] += 1
            self.particles[new_x, new_y] = 1
            new_positions.append((new_x, new_y))
        self.positions = new_positions

    def decayParticles(self):
        self.particles *= self.decay_rate
        self.grid *= self.decay_rate

    def runSimulation(self):
        self.initParticles()
        self.initFoodParticles()

sim = PhysarumSim(gridSize=100, numIterations=1000, batch_size=10, decay_rate=0.99)
sim.runSimulation()
sim.graphVisual()
