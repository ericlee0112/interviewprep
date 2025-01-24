class Solution:
    def maxSubArray(self, nums):

        # kadanes algorithm : max(nums[i], current_max_sum + nums[i])
        
        current_maxsum = nums[0]

        global_max = nums[0]

        for num in nums[1:]:
            current_maxsum = max(num, current_maxsum + num)
            
            global_max = max(global_max, current_maxsum)
        
        return global_max
'''

 -2,1, 1,5, 4,6,7,
[-2,1,-3,4,-1,2,1,-5,4]
'''