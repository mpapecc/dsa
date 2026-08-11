string = "abtzefcaaaaa"
# abcdaer
#[2, 7, 10, 13]

def array_longest_substring_without_repeating_chars(string : str):
    start = 0
    end = 0
    max_count = 0
    array_range = (0,0)
    seen = set()

    while end < len(string) and start < len(string):
        if is_unique(string[start:end+1]):
            if end - start +1 > max_count:
                array_range =(start, end)
                max_count = end - start +1
            end += 1
        else:
            start += 1

    return max_count,array_range


def is_unique(arr: list[str]):
    visited = set()

    for item in arr: 
        if item in visited:
            return False
        visited.add(item)
        
    return True




print(array_longest_substring_without_repeating_chars(string))
