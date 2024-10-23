import collections
def maxSlidingWindow(nums, k):
    queue = collections.deque([])
    output = []
    left = 0
    right = 0

    while right < len(nums):
        while len(queue) > 0 and nums[queue[-1]] < nums[right]:
            queue.pop()
        
        queue.append(right)

        if left > queue[0]:
            queue.popleft()
        
        if right >= k - 1:
            maxElementInWindow = nums[queue[0]]
            output.append(maxElementInWindow)
            left += 1
        
        right += 1
    return output

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums,k))
