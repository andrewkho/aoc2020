"""
Playground for optimal parking problem
"""

# Cost of reaching parking spot without parking
C0 = 10
# Number of iterations/spots to consider
T = 10

p = 0.2  # Probability parking spot is free
q = 1.-p

values = [C0] + [0]*(T-1)
policy = [0]*T  # 0 if continue, 1 if try to park

# Dynamic program, walk backwards from final spot
for k in range(1, T):
    #values[k] = p * min(k, values[k-1]) + q * values[k-1]
    values[k] = min((p*k + q*values[k-1]), values[k-1])

print(list(enumerate(values)))

for k, j in enumerate(values):
    if k < j:
        policy[k] = 1
    else:
        policy[k] = 0

print(list(zip(values, policy)))


# How can I solve this using transition probabilities?
# Transition probs
# For every parking spot, we have 2 possible states and 2 possible destination states
# i.e. for parking spot 0, 
import numpy as np
#         Num spots, i, j, a
p_ija = np.zeros((T, 2, 2, 2))

for k in range(T):
    i = 0
    # If we continue driving, we'll definitely not be parked
    p_ija[k, i, 0, 0] = 1.
    p_ija[k, i, 1, 0] = 0.

    # If we try to park, we'll be parked with prob p
    p_ija[k, i, 0, 1] = 1.-p
    p_ija[k, i, 1, 1] = p

    i = 1
    # If we're parked, then we can't unpark, no matter the action
    p_ija[k, i, 0, 0] = 0.
    p_ija[k, i, 1, 0] = 1.

    p_ija[k, i, 0, 1] = 0.
    p_ija[k, i, 1, 1] = 1.

