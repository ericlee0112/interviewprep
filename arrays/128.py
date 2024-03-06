'''
https://leetcode.com/problems/longest-consecutive-sequence/description/

'''

class okaySolution:
    def longestConsecutive(self, nums):
        # get the smallest and largest numbers in nums
        smallest = min(nums)
        largest = max(nums)
        hashset = set()
        # for every number in nums, add it to hashset
        for num in nums:
            hashset.add(num)

        # keep track of streak 
        current_streak = 1
        record_streak = 1


        # for i in range(smallest + 1, largest + 1)
        for i in range(smallest + 1, largest + 1):
            # if i in hashset, longest_so_far += 1
            if i in hashset:
                current_streak += 1
            # else, update record_streak and reset current_streak to 1
            else:
                record_streak = max(record_streak, current_streak)
                current_streak = 0
        
        record_streak = max(record_streak, current_streak)

        return record_streak
    
'''

[100,4,200,1,3,2]
turn this into set

loop through nums array
    if number has a left neighbour (nums[i] - 1), this is the start of a sequence


sequencebuilder method (num)
    streak = 1
    num += 1
    while there is no next neighbour
        if num not in hashset
            return streak
        else
            streak += 1
            num += 1
    
     x

'''

class betterSolution:
    def longestConsecutive(self, nums):
        self.hashset = set()
        for num in nums:
            self.hashset.add(num)

        max_streak = 0
        
        for i in range(len(nums)):
            if (nums[i] - 1) not in self.hashset:
                # start of a sequence
                streak = self.sequenceBuilder(nums[i])
                max_streak = max(max_streak, streak)
        return max_streak
    
    def sequenceBuilder(self, num):
        streak = 0
        while num in self.hashset:
            streak += 1
            num += 1
        return streak



testcase1 = [9,1,4,7,3,-1,0,5,8,-1,6]
testcase2 = [0,3,7,2,5,8,4,6,0,1]

sln = betterSolution()
print(sln.longestConsecutive(testcase1))
print(sln.longestConsecutive(testcase2))