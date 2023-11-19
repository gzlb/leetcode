def max_container(height):
    left = 0
    right = len(height) - 1
    max_area = 0 

    while left < right: 
        curr_area = (right - left)*min(height[left], height[right])
        max_area = max(max_area, curr_area)

        if height[left] < height[right]: 
            left += 1 

        else:
            right -= 1 


    return max_area 

height = [1,8,6,2,5,4,8,3,7]

print(max_container(height=height))