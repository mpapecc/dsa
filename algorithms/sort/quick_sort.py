array = [5,8,9,1,2,55,66,67,12,77,88]

def quicksort(array : list[int]):
    if array.__len__() <= 1:
        return array

    midpoint = array.__len__() // 2
    pivot_value = array[midpoint]

    smaller = []
    bigger = []

    for i in range(array.__len__()-1):
        if pivot_value <= array[i]:
            smaller.append(array[i])
        else:
            bigger.append(array[i])

    print(smaller)
    print(pivot_value)
    print(bigger)
    return quicksort(smaller) + [pivot_value] + quicksort(bigger)


print(quicksort(array))