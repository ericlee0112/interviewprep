# combination sum 
class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.ans = []
        
        for i in range(len(candidates)):
            candidate = candidates[i]
            if target - candidate >= 0:
                self.dig([candidate], candidates[i:], target - candidate)

        return self.ans
    
    def dig(self, combiantion, subsetOfCandidates, remainder):
        if remainder == 0:
            self.ans.append(combiantion)
        else:
            for i in range(len(subsetOfCandidates)):
                candidate = subsetOfCandidates[i]
                if remainder - candidate >= 0:
                    self.dig(combiantion + [candidate], subsetOfCandidates[i:], remainder - candidate)


sln = Solution()

candidates = [2,3,6,7]
target = 7
print(sln.combinationSum(candidates, target))