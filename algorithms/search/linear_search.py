arr_list = [1, 2, 3, 4, 5]

def linear_search(arr_list : list[int], target : int) -> int | None:
    for i in range(arr_list.__len__()):  
        if arr_list[i] == target:  
           return i
    return None

print(linear_search(arr_list, 10))