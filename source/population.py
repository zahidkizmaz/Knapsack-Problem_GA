from bag import Bag
from dna import Dna

class Population:

    def __init__(self, params):
        self.params = params
        self.random_counter = 0
        self.pop = [] #[Dna()] * size

    def increase_counter(self):
        self.random_counter += 1
        if self.random_counter == len(self.params.get('item_weights')):
            self.random_counter = 0

    def initialize_population(self):
        for i in range(self.params.get('pop_size')):
            self.pop.append(Dna(self.initialize_bits(), self.params.get('item_weights'), self.params.get('item_values'), Bag(self.params.get('bag_size'))))

    def initialize_bits(self):
        bits = len(self.params.get('item_weights')) * '0'
        for i, b in enumerate(bits):
            if self.params.get('random_number_array')[self.random_counter] >= 0.5:
                bits[i] = '1'
            self.increase_counter()
        return bits
    


