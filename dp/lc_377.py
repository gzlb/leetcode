def combination_sum(nums, target): 

    dp = [0 for _ in range(target + 1)]

    dp[0] = 1 

    for k in range(target + 1):
        for num in nums:
            if k - num >= 0:
                dp[k] += dp[k - num]

    return dp[-1]


nums = [1,2,3]
target = 4

print(combination_sum(nums=nums, target=target))


