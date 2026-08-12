import math

array = [-9, 1, -8, 2, 3, 7]
k = 3

def array_max_array_product_k(array : list[int], k:int):
    current_product = math.prod(array[:k])
    max_product = current_product

    for i in range(len(array) - k):
        current_product = current_product * (array[i + k]/array[i])
        max_product = max(current_product, max_product)

    return max_product

print(array_max_array_product_k(array, k))