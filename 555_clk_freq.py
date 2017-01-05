import math

# Desired frequency in Hz here.
frequency = float( input("Enter desired frequency (Hz): ") )

# Get set of resistors from inventory
resistor_inventory_fd = open('resistor_inventory.txt', 'r')
resistors = resistor_inventory_fd.readlines()
# The elements in the resistors list are all strings.
# Convert them to floats
resistors = [float(i) for i in resistors]

# Get set of capacitors from inventory
capacitor_inventory_fd = open('capacitor_inventory.txt', 'r')
capacitors = capacitor_inventory_fd.readlines()
# The elements in the capacitors list are all strings.
# Convert them to floats
capacitors = [float(i) for i in capacitors]


# Find the best answer set.
closest_frequency = frequency*999 # Pick an abitraritly large initial value

# Iterate through every possible combination of components to find set
# which give the result closest to the desired frequency
for ra in resistors:
    for rb in resistors:
        for c in capacitors:
            candidate_frequency = 1 / ( math.log(2)*(ra + 2*rb) * c )
            current_error = math.fabs( closest_frequency - frequency )
            candidate_error = math.fabs( candidate_frequency - frequency )
            if ( candidate_error < current_error ):
                closest_frequency = candidate_frequency
                best_c = c
                best_ra = ra
                best_rb = rb

print('A frequency of {} can be achieved with Ra={}, Rb={} , and C={}.'.format(closest_frequency, best_ra, best_rb, best_c))
