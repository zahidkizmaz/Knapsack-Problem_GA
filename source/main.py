from bag import Bag
from dna import Dna
from input_handler import get_params
from population import Population

if __name__ == "__main__":
    params = get_params()
    #print(params)
    pop = Population(params)
    pop.initialize_population()
    print(pop)