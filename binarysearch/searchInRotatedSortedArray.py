class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (right + left) // 2
            
            if nums[mid] == target:
                return mid
            
            # if left portion is sorted, 
            if nums[left] <= nums[mid]:
                # if target is out of range
                if target < nums[left] or nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            else:
                if nums[right] < target or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
    
'''


'''