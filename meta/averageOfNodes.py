
class part2:
    def solution(self, root):
        isTreeCompliant, numberOfDescendants, totalSumOfDesecendants = self.traverse(root)
        return isTreeCompliant

    def traverse(self, root):
        if root is None:
            return [True, 0,0]
        
        isLeftCompliant, numberOfChildNodesFromLeft, sumOfChildNodesFromLeft = self.traverse(root.left)
        isRightCompliant, numberOfChildNodesFromRight, sumOfChildNodesFromRight = self.traverse(root.right)

        if (isLeftCompliant == False or isRightCompliant == False):
            return [False, 0, 0]

        totalNumberOfChildNodes = numberOfChildNodesFromLeft + numberOfChildNodesFromRight + 1
        totalSumOfChildNodes = sumOfChildNodesFromLeft + sumOfChildNodesFromRight + root.val

        average = totalSumOfChildNodes // totalNumberOfChildNodes
        
        if average != root:
            isCompliant = False
        else:
            isCompliant = True

        return [isCompliant, totalNumberOfChildNodes, totalSumOfChildNodes]
