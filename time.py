import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)  # Randomly choose a pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return randomized_quicksort(left) + middle + randomized_quicksort(right)
________________________________________
