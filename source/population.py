from bag import Bag
from dna import Dna
from math import ceil

class Population:

    def __init__(self, params):
        """Creates a Population object.

        Keyword arguments:
        params -- Parameter object got by user. Includes hyper paramateres for genetic algorithm.
        """
        self.params = params
        self.random_counter = 0
        self.pop = [] #[Dna()] * size

    def increase_counter(self):
        """Increases the counter for random list. 
        Sets counter the zero to not get index out of bounds.
        """
        self.random_counter += 1
        if self.random_counter == len(self.params.get('random_number_array')):
            self.random_counter = 0

    def initialize_population(self):
        """Initializes the population.
        """
        for _ in range(self.params.get('pop_size')):
            tmp_dna = Dna(self.initialize_bits(), self.params.get('item_weights'), self.params.get('item_values'), Bag(self.params.get('bag_size')))
            tmp_dna.eval_vals()
            self.pop.append(tmp_dna)

    def initialize_bits(self):
        """Initializes and returns the bits.
        """
        bits = len(self.params.get('item_weights')) * '0'
        for i, b in enumerate(bits):
            if self.get_next_random() >= 0.5:
                bits_list = list(bits)
                bits_list[i] = '1'
                bits = "".join(bits_list)
        return bits
    
    def mutate_children(self, children, mutation_rate = None):
        """Applies mutation operation the giving list of Dna objects.

        Keyword arguemnts:
        children -- List of Dna objects reprents children to get mutated.
        """
        mutation_rate = mutation_rate if mutation_rate is not None else self.params.get('mutation_rate')
        print('Applying mutation to:', children)
        for child in children:
            self.mutate_individual(child)
            child.eval_vals()
        print('Mutated offspring:', children)
    
    
    def mutate_individual(self, individual):
        """Applies mutation operation the giving individual Dna object.

        Keyword arguments:
        individual -- Single Dna object that will get mutated.
        """
        mutation_rate = self.params.get('mutation_rate')
        for i, b in enumerate(individual.bits):
            if self.get_next_random() <= mutation_rate:
                #print('Applying Mutation:')
                bits_list = list(individual.bits)
                if bits_list[i] =='0':
                    bits_list[i] = '1'
                else:
                    bits_list[i] = '0'
                new_bits = "".join(bits_list)
                #print(new_bits)
        individual.bits = new_bits

    def get_next_random(self):
        """Returns next random number from the random list.
        """
        randm = self.params.get('random_number_array')[self.random_counter]
        self.increase_counter()
        return randm

    def crossover(self, parent1, parent2, crossover_point):
        """Applies one point crossover operation to between two Dna objects. 
        Returns the results of the crossover by two Dna object.
        
        Keyword Arguments:
        parent1 -- Dna object that represents firs parent of crossover. 
        parent2 -- Dna object that represents second parent of crossover. 
        crossover_point -- Integer index of the crossover point.  
        """
        print('Applying Crossover:\t at', crossover_point)
        print('Parents: ',(parent1, parent2))
        child1_bits = parent1.bits[:crossover_point] + parent2.bits[crossover_point:]
        child2_bits = parent2.bits[:crossover_point] + parent1.bits[crossover_point:]
        child1 = Dna(child1_bits, self.params.get('item_weights'), self.params.get('item_values'), Bag(self.params.get('bag_size')))
        child2 = Dna(child2_bits, self.params.get('item_weights'), self.params.get('item_values'), Bag(self.params.get('bag_size')))
        print('Children: ',(child1_bits, child2_bits))
        return (child1, child2)

    def recombine(self, parents):
        """Applies crossover to each parent duo from the list. 
        Returns the childen list.
        
        Keyword arguments:
        parents -- List of Dna objects that represents parents.
        """
        dna_len = len(parents[0][0].bits)
        children = []
        for p1, p2 in parents:
            crossover_point = self.get_index_by_random(dna_len)
            child1, child2 = self.crossover(p1, p2, crossover_point)
            child1.eval_vals()
            child2.eval_vals()
            children.append(child1)
            children.append(child2)
        return children
        

    def get_index_by_random(self, array_len):
        """Calculates and returns the index of random element using random list.

        Keyword arguments:
        array_len -- Element number of the list.
        """
        return (ceil(array_len * self.get_next_random()) - 1)

    def create_pool(self, tournament_size):
        """Creates and returns a pool from random Dna objects for tournament selection algorithm.

        Keyword arguments:
        tournament_size -- Integer size of the pool.
        """
        pool = []
        for _ in range(tournament_size):
            pool.append(self.pop[self.get_index_by_random(self.params.get('pop_size'))])
        return pool

    def select_parents(self, tournament_size):
        """Selects and returns two parents from pool.

        Keyword arguments:
        tournament_size -- Integer size of the pool.
        """
        pool = self.create_pool(tournament_size)
        pool.sort(key = lambda x: x.fitness(), reverse=True)
        return (pool[0], pool[1])

    def survivor_select(self, mating_pool):
        """Eliminates the worse Dna objects by their fitness value.

        Keyword arguemnts:
        mating_pool -- Pool of all Dna objets.
        """
        sorted_pool = sorted(mating_pool,key = lambda x: x.fitness(), reverse=True)
        return sorted_pool[:self.params.get('pop_size')]

    def pop_summary(self):
        """Keeps track of populations numbers.
        Returns best Dna's fitness, average fitness and worst Dna's fitness value of the population. 
        """
        best_individual = max(self.pop, key=lambda x: x.fitness())
        worst_individual = min(self.pop, key=lambda x: x.fitness())
        avg_fitness = sum(i.fitness() for i in self.pop) / float(len(self.pop))

        return (best_individual.fitness(), avg_fitness, worst_individual.fitness())


    def __str__(self):
        return str(self.pop)
        
    def __repr__(self):
        return str(self)

    
