# reverse a linked list through recursion

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode, node_list = []) -> ListNode:
        if head == None:
            if not node_list:
                return None
            answer = node_list[len(node_list) - 1]
            node_list.clear()
            return answer

        node_list.append(head)
        node_ahead = head.next
        if head == node_list[0]:

            head.next = None
        else:
            head.next = node_list[-2]
        return Solution.reverseList(self, head = node_ahead, node_list = node_list)
