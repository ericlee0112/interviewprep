# reorder list
# https://leetcode.com/problems/reorder-list/description/
'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def reorderList(head):
    # store the nodes in a list
    listofnodes = []
    curr = head
    while curr is not None:
        listofnodes.append(curr)
        curr = curr.next
    
    curr = head
    left = 0
    right = len(listofnodes) - 1
    while left < right:
        
        nextNode = ListNode(listofnodes[right].val)
        curr.next = nextNode
        curr = curr.next
        left += 1
        right -= 1
    
    return head

    
    

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)

reorderList(node)