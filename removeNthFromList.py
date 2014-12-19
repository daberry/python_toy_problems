# Write a function that removes the nth element from the
# end of a linked list using only one pass through

class Solution(object):
    def remove_nth_from_list(self, head, n):
        front = rear = head
        counter = 0
        while counter != n:
            front = front.next
            counter += 1
        if not front:
            return head.next
        while front:
            front = front.next
            temp = rear
            rear = rear.next
        temp.next = rear.next
        return head
