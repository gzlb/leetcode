def palindromic_substrings(string: str) -> int:


    max_pldr = ""
    max_len = 0 
    count = 0 
    for i in range(len(string)):
        l,r = i, i 

        while l >= 0  and r < len(string) and string[r] == string[l]: 
            if (r - l + 1) > max_len:
                max_pldr = string[l:r + 1]
                max_len = r - l + 1 

            l -= 1 
            r += 1 

        l, r = i, i + 1

        while l >= 0  and r < len(string) and string[r] == string[l]: 
            if (r - l + 1) > max_len:
                max_pldr = string[l:r + 1]
                max_len = r - l + 1 
                count += 1 
            l -= 1 
            r += 1 

    return count 