'''
https://leetcode.com/problems/merge-two-sorted-lists/


You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

eg.1
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        list3 = ListNode()
        curr = list3

        curr1 = list1
        curr2 = list2
        while curr1 is not None and curr2 is not None:
            # compare
            if curr1.val > curr2.val:
                newNode = ListNode(curr2.val)
                curr.next = newNode
                curr = curr.next
                curr2 = curr2.next
            else:
                newNode = ListNode(curr1.val)
                curr.next = newNode
                curr = curr.next
                curr1 = curr1.next
        
        if curr1 is not None:
            curr.next = curr1
        elif curr2 is not None:
            curr.next = curr2
        return list3.next
        
        