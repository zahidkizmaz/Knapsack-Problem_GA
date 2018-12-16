import matplotlib.pyplot as plt
from bag import Bag
from dna import Dna
from input_handler import get_params
from population import Population

if __name__ == "__main__":
    params, file_name = get_params()
    iter_number = params.get('iter_number')
    print(params)

    pop = Population(params)
    pop.initialize_population()
    summary = []
    for i in range(iter_number):
        print('Generation', i, '\n', pop)
        summary.append(pop.pop_summary())
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
    
    print('Final Population:', pop)

    best_vals = [s[0] for s in summary]
    avg_vals = [s[1] for s in summary]
    worst_vals = [s[2] for s in summary]

    range_ = range(0, iter_number)
    plt.plot(range_, best_vals, 'go--', label='Best')
    plt.plot(range_, avg_vals, 'rs--', label='Average')
    plt.plot(range_, worst_vals, 'bo--', label='Worst')
    plt.grid()
    plt.legend(loc='lower right')
    plt.xlabel('Iteration')
    plt.ylabel('Fitness')
    fig = plt.gcf()
    fig.canvas.set_window_title(file_name)
    plt.show()
