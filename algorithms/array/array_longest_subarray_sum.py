array = [4, 3, 3, 2, 1, 5, 2, 3, 5, 10, 1]
target_sum = 10

def array_longest_subarray_sum(array : list[int], target_sum: int):
    window_sum = 0 
    max_length = 0 
    pointer = 0 

    for i in range(len(array)):
        window_sum += array[i]

        while window_sum > target_sum:
            window_sum -= array[pointer]
            pointer += 1

        if window_sum == target_sum:
            max_length = max(max_length, i - pointer + 1)


    return max_length


print(array_longest_subarray_sum(array, target_sum))