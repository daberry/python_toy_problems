# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#  

class Solution(object):
    # @param: two ListNodes
    # @returns: a ListNode
    def mergeTwoLists(self, l1, l2):
        result = ListNode(-1)
        head = result
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        l3 = l1 and l1 or l2
        head.next = l3
        return result.next
