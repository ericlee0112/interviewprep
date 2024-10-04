
'''
there are a total of numCourses courses that you ahve to take, labelled from 0 to numCourses - 1

some courses may have prerequisites, 0 -> 1 is expressed as [0,1]

given the total number of courses and list of prerequisite pairs, is it possible for you to finish all courses ?

example 1:
numCourses = 2
prerequisites = [[1,0]]

1->0

output = true

example 2:
numCourses = 2
prerequisites = [[1,0],[0,1]]

0 -> 1 -> 0

use dfs or bfs 


e.g. 
n = 5
[[0,1], [0,2], [1,3], [1,4], [3,4]]

 0 -> 1 -> 3
 |      \  |      
 2        4

2 and 4 do not have any courses after

use adjacency list 

preRequsiteMap = {
    0 -> [1,2]
    1 -> [3,4]
    2 -> []
    3 -> [4]
    4 -> []
}

antiReqMap = {
    0 -> []
    1 -> [0]
    2 -> [0]
    3 -> [1]
    4 -> [3,1]

}

run dfs on every node from 0 to n -1 
 
'''

import collections
class Solution:
    def courseSchedule(self, numCourses, preReqs):
        self.nextCourseMap = collections.defaultdict(list)
        for (a,b) in preReqs:
            self.nextCourseMap[a].append(b)

        # visitSet is a set containing all the courses we have touched during a DFS traversal
        self.visitSet = set()

        for course in range(numCourses):
            res = self.dfs(course)
            if res == False:
                return False
            
        return True
    
    def dfs(self, course):
        if course in self.visitSet:
            return False
        # if we have reached the end of a dfs traversal, return true
        if len(self.nextCourseMap[course]) == 0:
            return True
        self.visitSet.add(course)

        for nextCourse in self.nextCourseMap[course]:
            res = self.dfs(nextCourse)
            if res == False:
                return False
        
        self.visitSet.remove(course)
        self.nextCourseMap[course] = []

        return True





        
                    
sln = Solution()
preReqs = [[0,1], [0,2], [1,3], [1,4], [3,4]]
print(sln.courseSchedule(5, preReqs))
