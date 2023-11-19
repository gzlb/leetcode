def longest_palindromic_substring(string: str) -> int:
    """
    ALGORITHM: 
        1. naive way: 
            - generate each substring O(n^2)
            - eliminate all non palindromes (or collect all palindromes)
            - obtain the one with highest length

            note: palindrome usually checked naively as by start right and end left and work towards middle 
            more clever: start from middle! 

        2. more optimal: 
            - store value max_len set to 0, store value max_pldr
            - loop with right and left pointers from the middle i.e. from the loop element i 
            - check while r - l + 1 > max_len and string[r] == string[l] 
                update max_pldr to string[l:r+1]
                update max_len to maximum of prev max_len and r - l + 1 
            - update pointers l -= 1 r += 1 

            edge case: even length then set l to i and r to i + 1 

    """

    max_pldr = ""
    max_len = 0 

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

            l -= 1 
            r += 1 

    return max_pldr 