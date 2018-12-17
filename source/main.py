import matplotlib.pyplot as plt
from bag import Bag
from dna import Dna
from input_handler import get_params
from population import Population

if __name__ == "__main__":
    """Getting parameters from the given text file. 
    """
    params, file_name = get_params()
    iter_number = params.get('iter_number')
    print(params)

    """Genetic algorithm:
    """
    pop = Population(params)
    pop.initialize_population()
    summary = []
    for i in range(iter_number):
        print('Generation', i, '\n', pop)
        summary.append(pop.pop_summary())
        parents = []
        for _ in range(int(params.get('pop_size') / 2)):
            pars = pop.select_parents(params.get('tournament_size'))
            parents.append(pars)
        
        children = pop.recombine(parents)
        pop.mutate_children(children)
        mating_pool = pop.pop.copy()
        mating_pool += children

        pop.pop = pop.survivor_select(mating_pool)
    
    print('Final Population:', pop)

    """Creating the summaries for graph.
    """
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
    title = 'Fitness values for ' 
    title += str(file_name)
    plt.title(title)
    fig = plt.gcf()
    fig.canvas.set_window_title(file_name)
    plt.show()
