def longest_increasing_subsequence(nums) -> int:
    """
    LIS: goal, check for each subsequence in nums if subsequent element is larger
                if true cnt += 1 
                
                compare all counters for each previous subsequence, largest is the return 


    ALGORITHM: 
        - start at idx 0, 
                        if element idx 1 is larger then continue, 
                            increase length by one then check for idx 2
                            repeat if true then increase cnt 
                            else set start idx to 2  
        
                        else set start idx to 1

        - we can see a pattern, either sliding window where we have one pointer which goes through the nums and another which trails this 
                0 1 2 3 4 5     it 1 
                l r 

                0 1 2 3 4 5     it 2  if true 
                l   r  

                0 1 2 3 4 5     it 2  if false 
                  l r  

        OR easier is dp since there is a recursive call 

        general DP algo: define an array dp with 0s, loop over dp array, then loop over num in nums check if it is increasing if so, 
        adjust dp element by max of previous dp and dp + 1 


        apply dp to length 
    
    """

    dp = [1 for _ in range(len(nums))] # use 1 since minimal length of a subsequence is one 

    
    for i in range(len(dp)): 
        for j in range(i): 
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)


    return max(dp)



nums = [10,9,2,5,3,7,101,18]

print(longest_increasing_subsequence(nums=nums))