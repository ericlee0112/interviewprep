class Solution:
    def productExceptSelf(self, nums):
        leftProduct = [1 for _ in range(len(nums))]
        rightProduct = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            rightProduct[i] = rightProduct[i + 1] * nums[i + 1]
        
        productList = []
        for i in range(len(nums)):
            product = rightProduct[i] * leftProduct[i]
            productList.append(product)
        
        return productList

'''


[1,2,3,4]
'''
        