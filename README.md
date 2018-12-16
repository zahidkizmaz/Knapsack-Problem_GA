# Knapsack Problem Solved With Genetic Algorithms

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
  $ python3 -m venv venv
  $ source venv/bin/activate
  (venv) $ pip install -r requirements.txt
  (venv) $ cd source/
  (venv) $ python main.py ../tests/test1.txt > out1.txt

```
After this you should be able to see graph and a out1.txt contains informaton about the genetic algortihm results.
