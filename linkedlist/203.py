# remove linked list elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
# https://leetcode.com/problems/remove-linked-list-elements/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int):
    curr = head
    prev = None
    while curr is not None:
        if curr.val == val:
            # get prev node
            # get nextNode
            nextNode = curr.next
            # connect them together
            if prev is not None:
                prev.next = nextNode
                curr = nextNode
            else:
                curr = curr.next
                head = curr
                
        else:
            prev = curr
            curr = curr.next
        
        
    return head
        
