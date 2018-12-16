from bag import Bag
from dna import Dna
from input_handler import get_params
from population import Population

if __name__ == "__main__":
    params = get_params()
    iter_number = params.get('iter_number')
    print(params)

    pop = Population(params)
    pop.initialize_population()
    #print(pop)

    for i in range(iter_number):
        print('Generation', i, '\n', pop)
        parent1, parent2 = pop.select_parents(params.get('tournament_size'))
        crossover_point = pop.get_index_by_random(len(parent1.bits))
        child1, child2 = pop.crossover(parent1,parent2,crossover_point)
        pop.mutate_individual(child1)
        pop.mutate_individual(child2)
        child1.eval_vals()
        child2.eval_vals()
        
        mating_pool = pop.pop.copy()
        mating_pool.append(child1)
        mating_pool.append(child2)

        pop.pop = pop.survivor_select(mating_pool)
