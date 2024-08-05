# insert interval
# https://leetcode.com/problems/insert-interval/
'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

def insert(intervals, interval):
    # asort intervals
    intervals.append(interval)
    sortedintervals = sorted(intervals, key=lambda x: x[0])
    print(sortedintervals)

    ans = [intervals[0]]

    for i in range(1, len(sortedintervals)):
        lastend = ans[-1][1]

        start = sortedintervals[i][0]
        end = sortedintervals[i][1]
        
        if start <= lastend:
            # merge
            ans[-1][1] = max(lastend, end)
        else:
            ans.append([start,end])
    return ans



intervals = [[1,2],[8,10],[3,5],[6,7],[12,16]]
interval = [4,8]
print(insert(intervals, interval))