def product_of_array_except_self(nums):
    n = len(nums)
    prod, right, left = [1]*n, [1]*n, [1]*n


    for i in range(1,n):
        left[i] = left[i-1]*nums[i-1]

    for i in range(n-2,-1,-1):
        right[i] = right[i+1]*nums[i+1]
        
    for i in range(n):
        prod[i] = left[i]*right[i]

    return prod 




nums = [1,2,3,4,5]

print(product_of_array_except_self(nums=nums))



