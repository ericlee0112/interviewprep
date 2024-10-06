

def maxSubarray(nums):
    max_global = nums[0]
    max_current_sum = nums[0]

    for i in range(1, len(nums)):
        max_current_sum = max(nums[i], nums[i] + max_current_sum)
        max_global = max(max_global, max_current_sum)
    
    return max_global