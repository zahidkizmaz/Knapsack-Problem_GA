class Dna:

    def __init__(self, bits, weights, values, bag):
        self.bits = bits #len(weights) * '0'
        self.weights = weights
        self.values = values
        self.bag = bag
    
    def eval_vals(self):
        total_val = 0
        total_weights = 0
        for i, bit in enumerate(self.bits):
            if bit:
                total_val += self.values.get(i)
                total_weights += self.weights.get(i)

        return total_val, total_weights

    def fitness(self):
        if self.bag.capacity < self.weights:
            return 0
        else:
            return self.values
        
    