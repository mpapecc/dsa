arr_list = [1,2,3,4,5,6,7,8,9,10]

def binary_search_exists(arr_list : list[int], target : int) -> int | None:
    first = 0
    last = arr_list.__len__() - 1

    while first <= last:
        midpoint = (first + last)//2

        if target == arr_list[midpoint]:
            return True,arr_list[midpoint]
        elif target < arr_list[midpoint]:
            last = midpoint - 1
        else :
            first = midpoint + 1

    return False, None

def binary_search_for_index_recursive(
        arr_list : list[int], 
        target : int, 
        start_index: int = 0, 
        last_index: int = len(arr_list) -1
        ) -> int | None:
    midpoint = (start_index + last_index)//2

    print(arr_list, start_index, last_index)
        
    if target == arr_list[midpoint]:
        return midpoint
    elif target < arr_list[midpoint]:
        return binary_search_for_index_recursive(arr_list,target, start_index, midpoint-1)
    elif target > arr_list[midpoint]:
        return binary_search_for_index_recursive(arr_list,target, midpoint+1, last_index)
    else:
        return None

print(binary_search_exists(arr_list, 19))