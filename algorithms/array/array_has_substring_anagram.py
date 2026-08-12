string = "greyhounds"
anagram = "hoy"

def array_has_substring_anagram(string: str, anagram : str):
    window_length = len(anagram)

    for i in range(len(string) - window_length):
        count = 0
        for j in range(window_length):
            if anagram[j] in string[i:i + window_length]:                
                count += 1

        if count == window_length:
            return True

    return False

def array_has_substring_anagram_improved(string: str, anagram : str):
    window_length = len(anagram)
    anagram_set = set(anagram[:])
    window_set = set(string[:window_length]) 

    for i in range(len(string) - window_length):
        if window_set == anagram_set:
            return True
        
        window_set.remove(string[i]);
        window_set.add(string[i + window_length])

    return False

print(array_has_substring_anagram_improved(string, anagram))