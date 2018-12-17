# Knapsack Problem Solved With Genetic Algorithms
[![Python 3.6](https://img.shields.io/badge/python-3.7-green.svg)](https://www.python.org/downloads/release/python-360/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-green.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![matplotlib](https://img.shields.io/badge/matplotlib-2.2.3-green.svg)](https://matplotlib.org/2.2.3/index.html)
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
