def merge_sort(list:list[int]):
    if list.__len__() <= 1:
        return list

    # Split 
    mid_point = list.__len__()//2
    left_part = list[mid_point:]
    right_part = list[:mid_point]

    left = merge_sort(left_part)
    right = merge_sort(right_part)
    # end Split

    #Sort Merge
    l = []
    left_position = 0
    right_position = 0

    while left_position < left.__len__() and right_position < right.__len__():
        if left[left_position] < right[right_position]:
            l.append(left[left_position])
            left_position += 1
        else:
            l.append(right[right_position])
            right_position += 1

    while left_position <  left.__len__():
        l.append(left[left_position])
        left_position += 1

    while right_position <  right.__len__():
        l.append(right[right_position])
        right_position += 1

    print(l)
    return l

merge_sort([5,8,9,1,2, 55,66,67,12,77,88])