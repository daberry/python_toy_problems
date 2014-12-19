class Solution:
    def insertionSortList(self, head):
        if not head:
            return head
        ref = ListNode(0)
        ref.next = head
        current = head
        while current.next:
            if current.next.val < current.val:
                current.val, current.next.val = current.next.val, current.next
                
