from collections import defaultdict

def group_anagrams(strs): 
    anagram_dict = defaultdict(list)


    for word in strs: 
        sorted_word = "".join(sorted(word))
        anagram_dict[sorted_word].append(word) 

    return list(anagram_dict.values())