#Sitong Guo

'''
9b assignment:
Create your own github repo
Add a .py file
Create a simple version of an agent based simulation, based on the code in the last lecture, and the github repo linked at the end
1. Create an Agent class
2. Create a World class
3. Initialize the world
4. Create a loop
Ask each agent in sequence to find an empty patch
Move the agent to the empty patch
End

Keep it simple (small grid, small number of agents, small number of loops), and utilize the code from the more complex example given in lecture. 
'''
import random

class Agent:
    def __init__(self, world, id):
        self.world = world
        self.id = id
        self.location = None

    def find_empty_patch(self):   #find a random empty patch in the world
        
        empty_patches = [loc for loc, occupant in self.world.grid.items() if occupant is None]
        
        if empty_patches:
            return random.choice(empty_patches)
        else:
            return None

    def move(self):  #move agent to random empty 
        new_location = self.find_empty_patch()
        if new_location:
            if self.location:
                self.world.grid[self.location] = None
            self.location = new_location
            self.world.grid[new_location] = self
            return True
        return False

class World:
    
    def __init__(self, size, num_agents):
        
        self.size = size
        self.num_agents = num_agents
        self.grid = self.build_grid(size)
        self.agents = self.build_agents(num_agents)

    def build_grid(self, size):
        
        locations = [(i, j) for i in range(size[0]) for j in range(size[1])]
        return {loc: None for loc in locations}

    def build_agents(self, num_agents):
      
        agents = [Agent(self, i) for i in range(num_agents)]
        for agent in agents:
            agent.move()
        return agents

    def step(self):
        for agent in self.agents:
            agent.move()

    def run(self, num_steps):
        for step in range(num_steps):
            self.step()
            self.print_grid()
            print("\n")

    def print_grid(self):  
        
        for i in range(self.size[0]):
            row = ""
            for j in range(self.size[1]):
                if self.grid[(i, j)] is None:
                    row += "[ ]"
                else:
                    row += "[*]"
            print(row)

#simulation parameters 
world_size = (5, 5)  
num_agents = 5       
num_steps = 10       

world = World(world_size, num_agents)
world.run(num_steps)
