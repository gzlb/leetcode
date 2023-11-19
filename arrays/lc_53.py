def max_subarray_sum(nums):
    current_sum = nums[0]
    max_sum = current_sum

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


nums = [5,4,-1,7,8]

print(max_subarray_sum(nums=nums))

