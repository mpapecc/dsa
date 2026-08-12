from collections import defaultdict


string = "abtzefcaaaaa"
# abcdaer
#[2, 7, 10, 13]

def array_longest_substring_without_repeating_chars(string : str):
    start = 0
    end = 0
    max_count = 0
    array_range = (0,0)

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

def array_longest_substring_without_repeating_chars_imporoved(string : str):
    longest = 0
    l = 0
    visited_count = defaultdict(int)

    for r in range(len(string)):
        visited_count[string[r]] += 1

        while visited_count[string[r]] > 1:
            l +=1
            visited_count[string[r]] -= 1

        longest = max(longest, r-l+1)

    return longest



print(array_longest_substring_without_repeating_chars_imporoved(string))
