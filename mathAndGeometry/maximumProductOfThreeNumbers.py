class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        if nums[0] < 0 and nums[1] < 0 and nums[-1] > 0:
            withNegatives = nums[0] * nums[1] * nums[-1]
            withPositives = nums[-1] * nums[-2] * nums[-3]
            return max(withNegatives, withPositives)
        
        if nums[0] < 0 and nums[1] > 0:
            return nums[-1] * nums[-2] * nums[-3]
        
        return nums[-1] * nums[-2] * nums[-3]