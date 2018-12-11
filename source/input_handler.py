import sys

def handle_inputs(input_array):
    # example input txt file -> 
    # ['0.06,0.32,0.87,0.02,0.15,0.47,0.36,0.53,0.32,0.39,0.39,0.26,0.27,0.21,0.73,0.42,0.69,0.32,0.3', 
    # '30', '5', '0.07', '82', '47', 
    # '14,13,11,13,10,11,13,14,11,13,15,11,11,11,5,15,15,6,12,12,7,8,6', 
    # '18,22,21,23,18,22,19,22,25,17,23,21,11,13,20,11,13,14,15,17,25,14,17']
    random_number_array = list(map(float, input_array[0].split(',')))
    pop_size = int(input_array[1])
    tournament_size = int(input_array[2])
    mutation_rate = float(input_array[3])
    iter_number = int(input_array[4])
    bag_size = int(input_array[5])
    item_weights = list(map(int,input_array[6].split(',')))
    item_values = list(map(int,input_array[7].split(',')))
    return {'random_number_array':random_number_array,
            'pop_size':pop_size,
            'tournament_size': tournament_size,
            'mutation_rate': mutation_rate,
            'iter_number': iter_number,
            'bag_size': bag_size,
            'item_values': item_values,
            'item_weights': item_weights,
        }

def get_inputs(inpts):
    file_name = ""
    for i in inpts:
        if '.txt' in i:
            file_name = i
            break
    if file_name :
        f = open(file_name)
    lines = []

    for line in f:
        lines.append(line.rstrip('\n'))
    
    return lines

def get_params():
    inpt_array = get_inputs(sys.argv)
    paramaters = handle_inputs(inpt_array)
    return paramaters

if __name__ == "__main__": 
    inpt_array = get_inputs(sys.argv)
    paramaters = handle_inputs(inpt_array)
    #print(paramaters)


