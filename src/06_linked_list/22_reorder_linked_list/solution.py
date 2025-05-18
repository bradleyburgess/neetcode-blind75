from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"Node: {self.val} -> {self.next}" if self.next else f"Node: {self.val}"


class Solution:
    @staticmethod
    def reorder_list_pairs(head: Optional[ListNode]) -> None:
        if not head:
            return None
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        node = head
        distance = length - 1
        while distance >= 0:
            if distance > 1:
                pair = node
                for _ in range(distance):
                    pair = pair.next
                temp = node.next
                node.next = pair
                pair.next = temp
                node = temp
            if distance == 1:
                node.next.next = None
            if distance == 0:
                node.next = None
            distance -= 2

    @staticmethod
    def reorder_list_floyd(head: Optional[ListNode]) -> None:

        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        list1 = head
        list2 = prev
        while list1 and list2:
            l1_next = list1.next
            l2_next = list2.next
            list1.next = list2
            list2.next = l1_next
            list1 = l1_next
            list2 = l2_next

        # Guard against duplicate node
        if list1:
            list1.next = None

    @staticmethod
    def reorder_list_floyd_simpler(head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = None
        prev, curr = None, list2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        list1 = head
        list2 = prev
        while list1 and list2:
            l1_next = list1.next
            l2_next = list2.next
            list1.next = list2
            list2.next = l1_next
            list1 = l1_next
            list2 = l2_next
