array = [4,4, 1,2,3,7,8,5,10]
string_arr = ["c", "b", "e", "f", "a"] 

def selection_sort(array: list[int]):
    if len(array) <= 1:
        return array
    
    current_start = 0
    
    while(current_start < array.__len__()):
        current_min = current_start

        for i in range(current_start, array.__len__()):
            if(array[i] < array[current_min]):
                current_min = i

        array[current_start], array[current_min] = array[current_min], array[current_start]

        current_start += 1

    return array

print(selection_sort(string_arr))
