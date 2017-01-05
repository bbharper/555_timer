import math

# Desired frequency in Hz here.
duty_cycle = float( input("Enter desired duty cycle (%): ") )

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
closest_duty_cycle = duty_cycle*999 # Pick an abitraritly large initial value

# Iterate through every possible combination of components to find set
# which give the result closest to the desired duty cycle
for ra in resistors:
    for rb in resistors:
        for c in capacitors:
            candidate_high_time = math.log(2)*c*(ra+rb)
            candidate_low_time = math.log(2)*c*rb
            candidate_duty_cyle = ( candidate_high_time / ( candidate_high_time + candidate_low_time) )*100
            current_error = math.fabs( closest_duty_cycle - duty_cycle )
            candidate_error = math.fabs( candidate_duty_cyle - duty_cycle )
            if ( candidate_error < current_error ):
                closest_duty_cycle = candidate_duty_cyle
                best_c = c
                best_ra = ra
                best_rb = rb

print('A duty cycle of {} % can be achieved with Ra={}, Rb={} , and C={}.'.format(closest_duty_cycle, best_ra, best_rb, best_c))
