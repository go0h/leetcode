# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        fakehead = ListNode(val=0, next=head)
        cur_node = fakehead

        while cur_node.next and cur_node.next.next:
            one = cur_node.next
            two = cur_node.next.next

            cur_node.next = two
            one.next = two.next
            two.next = one
            cur_node = one

        return fakehead.next

