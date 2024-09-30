# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''
import heapq
class Solution:
    def mergeKLists(self, lists):
        heap = []
        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i))
        
        parentNode = ListNode(0)
        curr = parentNode

        while len(heap) > 0:
            headVal, listNodeIndex = heapq.heappop(heap)
            print([headVal, listNodeIndex])

            node = lists[listNodeIndex]

            newNode = ListNode(headVal)

            curr.next = newNode

            curr = curr.next
            node = node.next
            lists[listNodeIndex] = lists[listNodeIndex].next

            if node is not None:
                heapq.heappush(heap, (node.val, listNodeIndex))
            print(parentNode)
        
        return parentNode.next

node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(3)

node2 = ListNode(4)
node2.next = ListNode(5)
node2.next.next = ListNode(8)

nodeList = [node1, node2]

sln = Solution()
print(sln.mergeKLists(nodeList))