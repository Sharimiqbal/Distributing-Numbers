import random
def create_list_summing_up_to(n):
    values = []
    for i in range(1, 12):
        value = random.randint(0, n)
        values.append(value)
        n -= value
    
    values.append(n)  # Calculate the last value to ensure the sum is correct
    return values

print(create_list_summing_up_to(100000))
