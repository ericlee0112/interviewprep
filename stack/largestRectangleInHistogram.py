def largestRectangle(heights):
    heights.append(0)
    maxArea = 0
    stack = [] # (i, height)

    for i in range(len(heights)):
        currentHeight = heights[i]
        start = i
        while len(stack) > 0 and stack[-1][1] > currentHeight:
            index, prevHeight = stack.pop()
            maxArea = max(maxArea, prevHeight * (i - index))
            start = index
        stack.append((start, currentHeight))

    return maxArea
