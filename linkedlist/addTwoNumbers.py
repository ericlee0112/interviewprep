# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        l3 = ListNode(0)
        curr = l3

        carry = False

        while l1 is not None and l2 is not None:
            # add values
            nodeSum = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next

            if carry:
                nodeSum += 1
                carry = False
            
            if nodeSum >= 10:
                nodeSum = nodeSum % 10
                carry = True
            
            newNode = ListNode(nodeSum)
            curr.next = newNode
            curr = curr.next

        
        while l1 is not None:
            nodeval = l1.val
            if carry:
                carry = False
                nodeval += 1
            
            if nodeval >= 10:
                carry = True
                nodeval = nodeval % 10
            
            newNode = ListNode(nodeval)
            l1 = l1.next
            curr.next = newNode
            curr = curr.next

        while l2 is not None:
            nodeval = l2.val

            if carry:
                carry = False
                nodeval += 1
            
            if nodeval >= 10:
                carry = True
                nodeval = nodeval % 10
            
            newNode = ListNode(nodeval)

            l2 = l2.next
            curr.next = newNode
            curr = curr.next
        
        if carry:
            newNode = ListNode(1)
            curr.next = newNode
        
        return l3.next