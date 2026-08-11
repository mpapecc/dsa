array = [1,4,1,10,25,3,5,0,26]
k = 4

def array_max_array_size_k(array : list[int], k:int):
    start = 0
    end = k-1
    current_sum = sum(array[:k])
    max_sum = current_sum
    while end < len(array)-1:
        start+=1
        end+=1
        current_sum = current_sum - array[start-1] + array[end]
        max_sum = max(current_sum, max_sum)
        
    return max_sum

def array_max_array_size_k_improved(array : list[int], k:int):
    current_sum = sum(array[:k])
    max_sum = sum(array[:k])
    for i in range(len(array) - k):
        current_sum = current_sum - array[i] + array[i +k]
        max_sum = max(current_sum, max_sum)
        
    return max_sum

print(array_max_array_size_k_improved(array, k))