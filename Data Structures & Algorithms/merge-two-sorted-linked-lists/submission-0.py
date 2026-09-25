# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # One goal of the Linked lists is to sort the separate lists 
        # and get the lists to be merged in one new list and be in the correct numerical order
        # I would want to use two pointers, one and the first list, one at the second
        # Once I step through the first list, if the number on the second list is greater than the first one, you can input the number from the first list into the new list and move one step forward
        # Keep doing that processs until you find a number on the first one that is bigger than the second one
        # Once you find it you input that second number you can keep repeating the process until you get to the final nodes in each list then you return the output
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
                 
            
        return dummy.next

