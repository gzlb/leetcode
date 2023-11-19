def longest_repeating_character_replacement(string,k):

    count = dict()
    l = 0
    max_len = 0 

    for r in range(len(string)):
        count[string[r]] = 1 + count.get(string[r], 0)

        while (r - l + 1) - max(count.values()) > k:
            count[string[l]] -= 1 
            l += 1 

        max_len = max(max_len, r - l + 1)


    return max_len


string = "AABA"
k = 1 

print(longest_repeating_character_replacement(string=string, k=k))