class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        elif sum(candidates) == target:
            return [candidates]

        candidates.sort()
        self.candidates = candidates
        self.target = target 
        self.memo = set()
        self.ans = []
        self.traverse(0, [])
        
        return self.ans
    
    def traverse(self, index, combination):
        if sum(combination) == self.target and str(combination) not in self.memo:
            self.memo.add(str(combination))
            self.ans.append(combination)
        elif index < len(self.candidates) and sum(combination) < self.target:
            for i in range(index, len(self.candidates)):
                if i > index and self.candidates[i] == self.candidates[i - 1]:
                    continue
                self.traverse(i + 1, combination + [self.candidates[i]])
