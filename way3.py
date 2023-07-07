import numpy as np
def create_list_summing_up_to(n):
    values = np.full(12, n // 12)  # Fill the array with equal values
    remaining = n % 12  # Calculate the remaining value
    indices = np.random.choice(12, remaining, replace=False)  # Choose random indices
    values[indices] += 1  # Add 1 to the randomly chosen indices
    return values.tolist()

print(create_list_summing_up_to(200))
