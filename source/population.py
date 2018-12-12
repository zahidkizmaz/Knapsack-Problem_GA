from bag import Bag
from dna import Dna
from math import ceil

class Population:

    def __init__(self, params):
        self.params = params
        self.random_counter = 0
        self.pop = [] #[Dna()] * size

    def increase_counter(self):
        self.random_counter += 1
        if self.random_counter == len(self.params.get('random_number_array')):
            self.random_counter = 0

    def initialize_population(self):
        for i in range(self.params.get('pop_size')):
            tmp_dna = Dna(self.initialize_bits(), self.params.get('item_weights'), self.params.get('item_values'), Bag(self.params.get('bag_size')))
            tmp_dna.eval_vals()
            self.pop.append(tmp_dna)

    def initialize_bits(self):
        bits = len(self.params.get('item_weights')) * '0'
        for i, b in enumerate(bits):
            if self.get_next_random() >= 0.5:
                bits_list = list(bits)
                bits_list[i] = '1'
                bits = "".join(bits_list)
        return bits
    
    def mutate_pop(self, mutation_rate = None):
        mutation_rate = mutation_rate if mutation_rate is not None else self.params.get('mutation_rate')
        for p in self.pop:
            for i, b in enumerate(p.bits):
                if self.get_next_random() <= mutation_rate:
                    bits_list = list(p.bits)
                    if bits_list[i] =='0':
                        bits_list[i] = '1'
                    else:
                        bits_list[i] = '0'
                    self.pop[i].bits = "".join(bits_list)

    def get_next_random(self):
        randm = self.params.get('random_number_array')[self.random_counter]
        self.increase_counter()
        return randm

    def crossover(self, parent1, parent2, crossover_point):
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def get_index_by_random(self, array_len):
        return ceil(array_len * self.get_next_random()) - 1

    def create_pool(self, tournament_size):
        pool = []
        for _ in range(tournament_size):
            pool.append(self.pop[self.get_index_by_random(self.params.get('pop_size'))])
        return pool

    def select_parents(self, tournament_size):
        pool = self.create_pool(tournament_size)
        pool.sort(key = lambda x: x.fitness)
        return pool[0], pool[1]

    def __str__(self):
        res = ''
        for i, p in enumerate(self.pop):
            res += str(i+1) + '- ' + str(p) +  '\tFitness:' + str(p.fitness()) + '\n'
            #print(p)
        return res

    
