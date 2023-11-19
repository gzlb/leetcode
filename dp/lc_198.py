def house_robber(nums):
    # temp = 0
    # profit = nums[0]

    # for i in range(len(nums)):
    #     temp, profit = profit, max(profit, temp + nums[i])


    # much easier 

    if len(nums) == 1: 
        return nums[1]
    
    else:

        profit = nums 
        profit[1] = max(profit[0], profit[1])

        for i in range(2, len(profit)):
            
            profit[i] = max(profit[i-1], nums[i] + profit[i - 2])



        return profit

