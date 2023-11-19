def three_sum(nums, target):

    nums = sorted(nums)
    res = []

    for i,v in enumerate(nums):
        if i > 0 and v == nums[i - 1]: 
            continue

        l,r = 0, len(nums) - 1 

        while l < r: 
            three_sum = nums[l] + nums[r] + v

            if three_sum < target:
                l += 1 

            elif three_sum > target: 
                r -= 1 

            else: 
                res.append([nums[l],nums[r],v])
                l += 1 
                while nums[l] == nums[l - 1] and l < r: 
                    l+= 1 


        
    return res 

    

