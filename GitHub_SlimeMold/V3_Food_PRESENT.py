import numpy as np
import matplotlib.pyplot as plt

class PhysarumSim:
    def __init__(self, gridSize=100, numIterations=1000):
        self.grid_size = gridSize
        self.num_iterations = numIterations
        self.grid = np.zeros((gridSize, gridSize))
        self.particles = np.zeros((gridSize, gridSize))
        self.foodParticles = []  # Store positions of food particles
        self.positions = []

    def graphVisual(self):
        plt.figure(figsize=(8, 6))
        
        # Assign colors for visualization
        cmap = plt.cm.get_cmap('inferno')
        
        # Plot regular particles with gradient effect
        plt.imshow(self.grid, cmap=cmap, interpolation='nearest')
        
        # Plot food particles with a different marker
        for (fx, fy) in self.foodParticles:
            plt.plot(fy, fx, 'o', color='yellow', markersize=8)
        
        plt.title('Slime Mold (Physarum) Simulation')
        plt.colorbar(label='Normalized Chemical Conc.')
        plt.show()

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
            self.positions[self.positions.index(pos)] = (new_x, new_y)

    def runSimulation(self):
        self.initParticles()
        self.initFoodParticles()
        for _ in range(self.num_iterations):
            self.updateParticles()

sim = PhysarumSim(gridSize=100, numIterations=1000)
sim.runSimulation()
sim.graphVisual()
