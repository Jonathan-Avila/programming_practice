from collections import deque as stack
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

      
    # reverse a linked list through iteraction using a stack 
    
        if head == None:
            return None
        
        node = head
        node_stack = stack()
        node_list = []
        
        while node is not None:
            node_stack.append(node)
            node = node.next


        while len(node_stack) > 1:
            node = node_stack.pop()
            node.next = node_stack[-1]
            node_list.append(node)
        else:
            node = node_stack.pop()
            node.next = None
            node_list.append(node)
            
        return node_list[0]
        
        
        

