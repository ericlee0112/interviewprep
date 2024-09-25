'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1,n + 1)]
        self.arr = arr
        self.ans = []
        self.k = k
        self.traverse(0, [])
        return self.ans

    
    def traverse(self, index, combination):
        if len(combination) == self.k:
            self.ans.append(combination)
            
        else:
            for i in range(index, len(self.arr)):
                self.traverse(i + 1, combination + [self.arr[i]])