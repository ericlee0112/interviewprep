# get kth largest element in array
# use quick select
# after quick select, well get the element at len(array) - k

class Solution:
    def findKthLargest(self, nums, k):
        self.k = len(nums) - k
        return self.quickSelect(nums, 0, len(nums) - 1)
        
       
    def quickSelect(self, nums, left, right):
        pivot = nums[right]
        p = left
        
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        
        nums[p], nums[right] = nums[right], nums[p]

        if p > self.k:
            # do quick select on left half 
            return self.quickSelect(nums, left, p - 1)
        elif p < self.k:
            return self.quickSelect(nums, p + 1, right)
        else:
            return nums[p]
