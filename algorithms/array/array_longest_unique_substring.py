from collections import defaultdict

string = "abcabcqbb"

def array_longest_unique_substring(string : str):
    max_length = 0
    pointer = 0
    char_count = defaultdict(int)

    for i in range(len(string)):
        char_count[string[i]] += 1
        while char_count[string[i]] > 1:
            char_count[string[i]] -= 1
            pointer +=1

        length = i - pointer + 1
        max_length = max(max_length, length)

    return max_length

print(array_longest_unique_substring(string))
