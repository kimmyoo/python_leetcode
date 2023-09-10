# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class LinkedListSetup(object):
    # form a singly linked list from a list
    def formSinglyLinkedList(self, nums):
        dummyHead = ListNode()
        walk = dummyHead
        for num in nums:
            curNode = ListNode(num)
            walk.next = curNode
            walk = walk.next
        # the true head
        return dummyHead.next

    # visualize the linked list
    def printLinkedList(self, head):
        walk = head
        while walk:
            print(walk.val, end="->")
            walk = walk.next
            if not walk:
                print("None", end="")
