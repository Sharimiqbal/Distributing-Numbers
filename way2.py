import random
def create_list_summing_up_to(n):
    average_value = n // 12
    remaining = n % 12

    values = [average_value] * 12
    # Distribute the remaining value randomly across the elements
    for _ in range(remaining):
        index = random.randint(0, 11)
        values[index] += 1

    return values
print(create_list_summing_up_to(200))
