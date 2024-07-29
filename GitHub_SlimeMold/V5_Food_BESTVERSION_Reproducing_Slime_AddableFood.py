import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import time

class PhysarumSim:
    def __init__(self, gridSize=100, numIterations=1000, batch_size=10, decay_rate=0.95, food_attraction_radius=10, food_lifetime=1.0):
        self.grid_size = gridSize
        self.num_iterations = numIterations
        self.batch_size = batch_size
        self.decay_rate = decay_rate
        self.food_attraction_radius = food_attraction_radius
        self.food_lifetime = food_lifetime  # Lifetime of food particle in seconds
        self.grid = np.zeros((gridSize, gridSize))
        self.particles = np.zeros((gridSize, gridSize))
        self.foodParticles = []  # Store positions of food particles and their consumption times
        self.positions = []
        self.food_consumed_times = {}  # Dictionary to store consumption times of food particles
        self.food_to_remove = []  # List to store food particles to be removed
        self.fig, self.ax = plt.subplots()
        self.im = None  # To store the image plot for updating
        self.food_dots = None  # To store the plot of food particles

        # Connect mouse click event to handler
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)

    def graphVisual(self):
        self.im = self.ax.imshow(self.grid, cmap='inferno', interpolation='nearest')
        self.food_dots, = self.ax.plot([], [], 'yo', markersize=10)  # Initialize food particles plot
        
        self.ax.set_title('Slime Mold (Physarum) Simulation')
        self.fig.colorbar(self.im, ax=self.ax, label='Slime Mold Conc.')
        
        ani = FuncAnimation(self.fig, self.update_visualization, frames=self.num_iterations // self.batch_size,
                            interval=100, repeat=False)
        
        plt.show()

    def update_visualization(self, frame):
        for _ in range(self.batch_size):
            self.updateParticles()
            self.decayParticles()
            self.checkFoodDecay()
        
        # Update food particles plot
        fx = [p[1] for p in self.foodParticles]
        fy = [p[0] for p in self.foodParticles]
        self.food_dots.set_data(fx, fy)
        
        # Update the grid and particles
        self.im.set_data(self.grid)  # Update the data for the image plot
        
        return self.im, self.food_dots

    def initParticles(self, num_particles=5, spread_radius=5, center=None):
        if center is None:
            center_x = self.grid_size // 2
            center_y = self.grid_size // 2
        else:
            center_x, center_y = center
        
        for _ in range(num_particles):
            # Introduce slight random spread around the center
            spread_x = np.random.randint(-spread_radius, spread_radius + 1)
            spread_y = np.random.randint(-spread_radius, spread_radius + 1)
            
            x = center_x + spread_x
            y = center_y + spread_y
            
            # Ensure positions are within grid bounds
            x = np.clip(x, 0, self.grid_size - 1)
            y = np.clip(y, 0, self.grid_size - 1)
            
            self.particles[x, y] = 1
            self.positions.append((x, y))
            self.grid[x, y] += 1  # Increment grid value for gradient effect

    def initFoodParticles(self, num_foodParticles=4):
        for _ in range(num_foodParticles):
            x, y = np.random.randint(self.grid_size), np.random.randint(self.grid_size)
            self.foodParticles.append((x, y))
            self.food_consumed_times[(x, y)] = None  # Initialize consumed time as None

    def movementPattern(self, x, y):
        # Check nearby food particles within the attraction radius
        min_dist = float('inf')
        best_dx, best_dy = 0, 0
        
        for fx, fy in self.foodParticles:
            dist = np.sqrt((fx - x) ** 2 + (fy - y) ** 2)
            if dist < min_dist:
                min_dist = dist
                best_dx = fx - x
                best_dy = fy - y
        
        # If a food particle is within attraction radius, move towards it
        if min_dist <= self.food_attraction_radius:
            return np.sign(best_dx), np.sign(best_dy)
        else:
            # Otherwise, move randomly
            return np.random.choice([-1, 0, 1]), np.random.choice([-1, 0, 1])

    def updateParticles(self):
        new_positions = []
        consumed_food = []  # Track consumed food particles
        current_time = time()
        
        for pos in self.positions:
            x, y = pos
            dx, dy = self.movementPattern(x, y)
            new_x = np.clip(x + dx, 0, self.grid_size - 1)  # Clamp x to grid boundaries
            new_y = np.clip(y + dy, 0, self.grid_size - 1)  # Clamp y to grid boundaries
            
            # Check if particle reaches a food particle
            if (new_x, new_y) in self.foodParticles:
                self.consumeFood(new_x, new_y, current_time)
                self.grid[new_x, new_y] += 1  # Increment grid at food location
                consumed_food.append((new_x, new_y))
            else:
                self.grid[new_x, new_y] += 1
                self.particles[new_x, new_y] = 1
            
            new_positions.append((new_x, new_y))
        
        self.positions = new_positions
        
        # Remove consumed food particles after updating positions
        for food in consumed_food:
            self.food_to_remove.append(food)

        # Clean up food particles marked for removal
        for food in self.food_to_remove:
            if food in self.foodParticles:
                self.foodParticles.remove(food)
                self.food_consumed_times.pop(food)
                self.grid[food[0], food[1]] = 0
                # Summon new particles around the consumed food location
                self.initParticles(num_particles=2, spread_radius=3, center=food)
        self.food_to_remove = []

    def consumeFood(self, x, y, current_time):
        # Record the consumption time of the food particle
        self.food_consumed_times[(x, y)] = current_time

    def decayParticles(self):
        self.particles *= self.decay_rate
        self.grid *= self.decay_rate

    def checkFoodDecay(self):
        current_time = time()
        for (fx, fy), consumed_time in list(self.food_consumed_times.items()):  # Use list() to avoid modifying while iterating
            if consumed_time is not None and current_time - consumed_time >= self.food_lifetime:
                self.food_to_remove.append((fx, fy))

        # Clean up food particles marked for removal
        for food in self.food_to_remove:
            if food in self.foodParticles:
                self.foodParticles.remove(food)
                self.food_consumed_times.pop(food)
                self.grid[food[0], food[1]] = 0
        self.food_to_remove = []

    def runSimulation(self):
        self.initParticles()
        self.initFoodParticles()

    def onclick(self, event):
        # Check if click happened within the plot area
        if event.xdata is not None and event.ydata is not None:
            # Convert clicked coordinates to grid indices
            x = int(event.xdata + 0.5)
            y = int(event.ydata + 0.5)
            
            # Ensure coordinates are within grid bounds
            if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                # Add food particle to the clicked location
                self.foodParticles.append((y, x))  # Note: Reversed due to imshow() displaying matrix transpose
                self.food_consumed_times[(y, x)] = None  # Initialize consumption time as None
                self.grid[y, x] += 1  # Increment grid at food location

                # Update the plot with the new food particle
                self.food_dots.set_data([p[1] for p in self.foodParticles], [p[0] for p in self.foodParticles])
                self.im.set_data(self.grid)
                self.fig.canvas.draw()

sim = PhysarumSim(gridSize=100, numIterations=2000, batch_size=10, decay_rate=0.99, food_attraction_radius=5, food_lifetime=1.0)
sim.runSimulation()
sim.graphVisual()
