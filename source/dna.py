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
            if bit == '1':
                total_val += self.values[i]
                total_weights += self.weights[i]
        self.total_weight = total_weights
        self.total_value = total_val
        return total_val, total_weights

    def fitness(self):
        if self.bag.capacity < self.total_weight:
            #print(self.bag.capacity, self.total_weight)
            return 0
        else:
            return self.total_value

    def __str__(self):
        return self.bits
        
    