import collections


class SparseVector:
    def __init__(self, nums):
        self.nums = []

        for i in range(len(nums)):
            if nums[i] != 0:
                self.nums.append((i, nums[i]))
    
    def dotProduct(self, vector2):
        dotProduct = 0

        i = 0
        j = 0

        while i < len(self.nums) and j < len(vector2.nums):
            firstVectorIndex, firstVectorVal = self.nums[i]
            secondVectorIndex, secondVectorVal = vector2.nums[j]

            if firstVectorIndex == secondVectorIndex:
                dotProduct += (firstVectorVal * secondVectorVal)
                i += 1
                j += 1
            elif firstVectorIndex > secondVectorIndex:
                j += 1
            else:
                i += 1
        
        return dotProduct

vec1 = SparseVector([1,0,0,2,3])
vec2 = SparseVector([1,0,4,4,1])
print(vec1.dotProduct(vec2))
