def max_subarray_prod(nums):
    res = nums[0]
    min_prod = res
    max_prod = res

    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod*num)
        min_prod = min(num, min_prod*num)

        res = max(res,max_prod)
    
    return res

nums = [2,3,-2,4] 

print(max_subarray_prod(nums=nums)) 