import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:    
    def mergeKLists(self, lists):
        heap = []
        heapq.heapify(heap)

        ans = ListNode(0)
        curr = ans

        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i))

        while len(heap) > 0:
            node_val, index = heapq.heappop(heap)

            ans.next = ListNode(node_val)
            ans = ans.next

            if lists[index].next is not None:
                lists[index] = lists[index].next
                heapq.heappush(heap, (lists[index].val, index))
        
        return curr.next




linkedlist1 = ListNode(1)
linkedlist1.next = ListNode(2)
linkedlist1.next.next = ListNode(4)


linkedlist2 = ListNode(1)
linkedlist2.next = ListNode(3)
linkedlist2.next.next = ListNode(5)


linkedlist3 = ListNode(3)
linkedlist3.next = ListNode(6)

lists = [linkedlist1, linkedlist2, linkedlist3]

sln = Solution()
print(sln.mergeKLists(lists))