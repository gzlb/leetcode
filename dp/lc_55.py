def jump_game(nums):
    """
    solve this reverse, assume we are at the last index and then check if we can reach the first 
    suppose last index is labeld as l_idx

    eg [2,3,1,1,4] l_idx = 5 

    we start at idx 4 we can reach l_idx since 4 + 1 = 5 
    idx 3, we can reach idx 4 since 3 + 1 = 4 
    idx 2, we can reach idx 3 since 2 + 3 = 5 > 3 
    idx 1, we can reach idx 2 since 1 + 2 = 3 > 2 
    
    eg nums = [3,2,1,0,4] l_ixd = 5 

    we start at idx 4, we cannot reach l_idx since at idx 4 + 0 = 

    """

    goal = len(nums) - 1 

    for i in range(goal - 1, -1, -1): 
        if i + nums[i] >= goal:
            goal = i 


    return True if goal == 0 else False

