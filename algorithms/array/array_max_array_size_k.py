array = [1,4,1,10,25,3,5,0,26]
k = 4
def array_max_array_size_k(array : list[int], k:int):
    start = 0
    end = 3
    current_sum = sum(array[:k])
    max_sum = current_sum
    while end < len(array)-1:
        start+=1
        end+=1
        # print(start)
        # print(end)
        current_sum = max_sum - array[start] + array[end]
        print(current_sum)
        print(array[start:end+1])
        max_sum = max(current_sum, max_sum)
        

    return max_sum


print(array_max_array_size_k(array, k))