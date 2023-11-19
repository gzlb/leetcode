def word_break(s, wordDic) -> bool:

    """
    check if s can be sliced and matched with pairs in wordDic 

    we have to check the substring of s if they can be paired in wordDic 

    general idea is to have s[j:0] and s[j:i] checked and where i loops through the whole and j is adjusted by i 

    consider the case of empty string, this is true
    consider the case of a string with length 1 then just check if this character is present in wordDic 
    
    idea is to use an array and start of with saying that each case is false 

    array stores the cases for s[0:j]  and then each case check s[j:i] 

    """ 

    wordset = set(wordDic)

    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True 

    for i in range(len(s) + 1): 
        for j in range(i): 
            if dp[j] and s[j:i] in wordset:
                dp[i] = True
                


    return dp[-1]

s = "leetcode"

wordDict = ["leet", "code"]


print(word_break(s=s, wordDic=wordDict))