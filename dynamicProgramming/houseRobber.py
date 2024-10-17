'''

[1,2,3,1]

[1,2,4,]

rob = max(arr[0] + rob[2:n], rob[1:n])
'''

class Solution:
    def rob(self, nums):
        rob1 = 0
        rob2 = 0
        for i in range(len(nums)):
            
            maxPossibleValueWeCanRobAtI = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = maxPossibleValueWeCanRobAtI
        
        return rob2

'''
[2,9,8,3,6]

i rob1.  rob2
0  0      0
1. 0      2
2. 2      9
3. 9      10
4  10     12

10 + 6 = 16

'''