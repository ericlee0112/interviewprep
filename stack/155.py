'''
https://leetcode.com/problems/min-stack/description/
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

'''

class MinStack:
    def __init__(self):
        self.min_so_far = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        self.min_so_far = min(self.min_so_far, val)
        self.stack.append([self.min_so_far, val])
        

    def pop(self) -> None:
        minimum, val = self.stack[-1]
        del(self.stack[-1])
        if len(self.stack) > 0 and self.stack[-1][0] > minimum:
            self.min_so_far = self.stack[-1][0]   
        elif len(self.stack) == 0:
            self.min_so_far = float('inf')    

    def top(self) -> int:
        return self.stack[-1][1]
        

    def getMin(self) -> int:
        return self.stack[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()