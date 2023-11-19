def longest_substring_without_repeating_characters(string: str) -> int: 
    """
    ALGORITHM 
        goal: find the longest substring without repeating characters
            solution: 
                - minimal substring without repeating characters is 1 
                - define a hashmap, which stores the last idx of character and its length 
                - if the character is already present, we have to modify the starting point, 
                    starting point becomes the maximum of the previous and ending of the window + 1 
                - each case, the max length is the previous or the current,
                - each case, update the last_idx of each character by i 
                    last_idx = dict()
                    max_len = 0 
                    start_idx = 0 
                    for i in range(len(string)): 

                        if string[i] in last_idx: 
                            start_idx = max(start_idx, last_idx[string[i]] + 1)

                    
                        max_len = max(max_len, start_idx - i + 1)

                        last_idx[string[i]] = i 
        
        easier: use a set for the substring if it is in the set already, we update our window
     
    
    """

    sub_set = set()
    max_len = 0

    l = 0 

    for r in range(len(string)):
        while string[r] in sub_set: 
            sub_set.remove(string[l])
            l += 1 
    sub_set.add(string[r])
    max_len = max(max_len, r - l + 1)
    return max_len


