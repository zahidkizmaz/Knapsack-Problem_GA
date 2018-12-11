from bag import Bag
from dna import Dna

class Population:

    def __init__(self, size, mutation_rate):
        self.size = size
        self.mutation_rate = mutation_rate
        self.pop = []
    
    def initialize_population(self):
        for i in range(self.size):
            pass
