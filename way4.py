import numpy as np
def create_list_summing_up_to(n):
    values = np.random.multinomial(n, [1/12]*12)
    return values.tolist()

print(create_list_summing_up_to(2000))
