# push dominoes
'''
838. Push Dominoes
Medium
Topics
Companies
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
'''
class Solution:
    def pushDominoes(self, dominoes):
        if len(dominoes) <= 1:
            return dominoes
        
        self.dominoes = list(dominoes)

        # break into segments
        segments = []
        left = 0
        right = 1
        while right < len(self.dominoes):
            if self.dominoes[right] == 'L' or self.dominoes[right] == 'R':
                # cut the segment
                # start a new segment
                segments.append((left,right))
                left = right
                right += 1
            else:
                right += 1
        segments.append((left,right-1))

        for (left, right) in segments:
            if (self.dominoes[left] == '.' and self.dominoes[right] == 'L') or (self.dominoes[left] == 'L' and self.dominoes[right] == 'L'):
                # everything is L
                self.turnEverythingLeft(left, right)

            elif (self.dominoes[left] == 'R' and self.dominoes[right] == '.') or (self.dominoes[left] == 'R' and self.dominoes[right] == 'R'):
                # everything is R
                self.turnEverythingRight(left, right)
            elif self.dominoes[left] == 'R' and self.dominoes[right] == 'L':
                self.topple(left, right)
        
        return self.dominoes
    
    def turnEverythingLeft(self, left, right):
        for i in range(left, right + 1):
            self.dominoes[i] = 'L'
    
    def turnEverythingRight(self, left, right):
        for i in range(left, right + 1):
            self.dominoes[i] = 'R'

    def topple(self, left, right):
        if len(self.dominoes[left:right + 1]) > 2:
            l = left + 1
            r = right - 1
            while l < r:
                self.dominoes[l] = 'R'
                self.dominoes[r] = 'L'
                l += 1
                r -= 1
        


dominoes = ".L.R...LR..L.."
print(Solution().alternateSolution(dominoes))