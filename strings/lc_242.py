def valid_anagram(s: str, t:str) -> bool:
    """
    Solutions: 
    1. sort and then compare 
    2. collect all letters in hashmap and compare 
    """

    if len(s) == len(t):

        s_dict, t_dict = dict(), dict()

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

            return s_dict == t_dict

    else:
        return False
    
