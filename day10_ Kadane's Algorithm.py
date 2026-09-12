def max_subarray(nums):
    max_current = max_global = nums[0]
    
    for num in nums[1:]:
        # Decide whether to add to the existing subarray or start a new one
        max_current = max(num, max_current + num)
        
        # Update the overall maximum if current is larger
        if max_current > max_global:
            max_global = max_current
            
    return max_global
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray(numbers)
print("Maximum contiguous sum:", result)  # Output: 6 (from [4, -1, 2, 1])
