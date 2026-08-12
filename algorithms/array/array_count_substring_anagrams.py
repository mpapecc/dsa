from collections import Counter


string = "gattactat"
anagram = "att"

def array_count_substring_anagrams(string : str, anagram: str):
    window_length = len(anagram)
    anagram_counter = Counter(anagram)
    window_counter = Counter(string[:window_length])
    count = 0
    for i in range(len(string) - window_length):
        if window_counter == anagram_counter:
            count += 1
            print(window_counter)

        window_counter[string[i]] = 0
        window_counter[string[i + window_length]] +=1

    return count

print(array_count_substring_anagrams(string, anagram))