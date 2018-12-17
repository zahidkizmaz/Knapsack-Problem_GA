# Knapsack Problem Solved With Genetic Algorithms
[![Python 3.6](https://img.shields.io/badge/python-3.7-green.svg)](https://www.python.org/downloads/release/python-360/)
[![matplotlib](https://img.shields.io/badge/matplotlib-2.2.3-green.svg)](https://matplotlib.org/2.2.3/index.html)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-green.svg)](https://www.gnu.org/licenses/gpl-3.0)

# Knapsack Problem

The knapsack problem or rucksack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. For more information: [knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem)
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Knapsack.svg/640px-Knapsack.svg.png?1545059810405" width="40%">
</p>

# Genetic Algorithms

A genetic algorithm (GA) is a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on bio-inspired operators such as mutation, crossover and selection. John Holland introduced Genetic Algorithm (GA) in 1960 based on the concept of Darwin’s theory of evolution; afterwards, his student Goldberg extended GA in 1989. For more information: [genetic algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm)
<p align="center">
<img src="https://cdn-images-1.medium.com/max/1600/1*vIrsxg12DSltpdWoO561yA.png" width="40%"/>
</p>

### Pseudo code for the genetic algorithms:

* BEGIN
  - Initialise
  - Evaluate
  - Repeat: 
    * Parent Select 
    * Recombine 
    * Mutate 
    * Evaluate 
    * Survivor Select
* END

# Installation and Usage

I recommend using a virtualenv:

```
  $ git clone https://github.com/zahidkizmaz/Knapsack-Problem_GA
  $ cd Knapsack-Problem_GA/
  $ python3 -m venv venv
  $ source venv/bin/activate
  (venv) $ pip install -r requirements.txt
  (venv) $ cd source/
  (venv) $ python main.py ../tests/test1.txt > out1.txt

```
After this you should be able to see a graph and a out1.txt contains informaton about the genetic algortihm results.

### Example Graph

This graph indicates a summary of the population at the given iteration. Best is the highest fitness value in the population and worst is the lowest fitness value in the population. Also average indicates for average fitness value for all population at the corresponding iteration.

<p align="center">
  <img src="https://github.com/zahidkizmaz/Knapsack-Problem_GA/blob/master/graphs/test1.txt.png">
</p>
