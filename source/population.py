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
        for _ in range(self.params.get('pop_size')):
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
    '''
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
    '''
    
    def mutate_individual(self, individual):
        mutation_rate = self.params.get('mutation_rate')
        for i, b in enumerate(individual.bits):
            if self.get_next_random() <= mutation_rate:
                print('Applying Mutation:')
                bits_list = list(individual.bits)
                if bits_list[i] =='0':
                    bits_list[i] = '1'
                else:
                    bits_list[i] = '0'
                new_bits = "".join(bits_list)
                print(new_bits)
        individual.bits = new_bits

    def get_next_random(self):
        randm = self.params.get('random_number_array')[self.random_counter]
        self.increase_counter()
        return randm

    def crossover(self, parent1, parent2, crossover_point):
        print('Applying Crossover:\t at', crossover_point)
        print('Parents: ',parent1, parent2)
        child1_bits = parent1.bits[:crossover_point] + parent2.bits[crossover_point:]
        child2_bits = parent2.bits[:crossover_point] + parent1.bits[crossover_point:]
        child1 = Dna(child1_bits, self.params.get('item_weights'), self.params.get('item_values'), Bag(self.params.get('bag_size')))
        child2 = Dna(child2_bits, self.params.get('item_weights'), self.params.get('item_values'), Bag(self.params.get('bag_size')))
        print('Children: ',child1_bits, child2_bits)
        return child1, child2

    def get_index_by_random(self, array_len):
        return (ceil(array_len * self.get_next_random()) - 1)

    def create_pool(self, tournament_size):
        pool = []
        for _ in range(tournament_size):
            pool.append(self.pop[self.get_index_by_random(self.params.get('pop_size'))])
        return pool

    def select_parents(self, tournament_size):
        pool = self.create_pool(tournament_size)
        pool.sort(key = lambda x: x.fitness(), reverse=True)
        return pool[0], pool[1]

    def survivor_select(self, mating_pool):
        sorted_pool = sorted(mating_pool,key = lambda x: x.fitness(), reverse=True)
        return sorted_pool[:self.params.get('pop_size')]

    def pop_summary(self):
        best_individual = max(self.pop, key=lambda x: x.fitness())
        worst_individual = min(self.pop, key=lambda x: x.fitness())
        avg_fitness = sum(i.fitness() for i in self.pop) / float(len(self.pop))

        return (best_individual.fitness(), avg_fitness, worst_individual.fitness())


    def __str__(self):
        return str(self.pop)
        
    def __repr__(self):
        return str(self)

    
