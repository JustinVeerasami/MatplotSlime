import numpy as np
import matplotlib.pyplot as plt


class PhysarumSim:
    def __init__(self, grid_size=100, num_iterations=1000):
        self.grid_size = grid_size
        self.num_iterations = num_iterations
        self.grid = np.zeros((grid_size, grid_size))
        self.particles = np.zeros((grid_size, grid_size))
        self.particles[:] = np.nan
        self.positions = []

    def initParticles(self, num_particles=10):
        for _ in range(num_particles):
            x, y = np.random.randint(self.grid_size), np.random.randint(self.grid_size)
            self.particles[x, y] = 1
            self.positions.append((x, y))

    def updateParticles(self):
        for pos in self.positions:
            x, y = pos
            dx, dy = self.movementPattern(x, y)
            new_x, new_y = (x + dx) % self.grid_size, (y + dy) % self.grid_size
            self.grid[new_x, new_y] += 1
            self.particles[new_x, new_y] = 1
            self.positions[self.positions.index(pos)] = (new_x, new_y)

    def movementPattern(self, x, y):
        # Add your Physarum-like movement rules here
        # For example, you can implement a gradient-following behavior
        return np.random.choice([-1, 0, 1]), np.random.choice([-1, 0, 1])

    def runSimulation(self):
        self.initParticles()
        for _ in range(self.num_iterations):
            self.updateParticles()

    def graphVisual(self):
        plt.figure(figsize=(8, 6))
        plt.imshow(self.grid, cmap='inferno', interpolation='nearest')
        plt.title('Physarum polycephalum Simulation')
        plt.colorbar(label='Chemical Conc.')
        plt.show()

# Example usage
sim = PhysarumSim(grid_size=100, num_iterations=1000)
sim.runSimulation()
sim.graphVisual()