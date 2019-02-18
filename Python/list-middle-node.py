# LeetCode 876: Middle of the Linked List
# Given a non-empty, singly linked list with head node head, 
#   return a middle node of linked list.

# Example: Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  
#   (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
#   ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 
#   and ans.next.next.next = NULL.

If there are two middle nodes, return the second middle node.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(head):
    pointer1 = head
    pointer2 = head
    
    while pointer1 and pointer1.next != None:
        pointer1 = pointer1.next
        
        if pointer1:
            pointer1 = pointer1.next
        
        pointer2 = pointer2.next
        
    return pointer2

def main():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print(middleNode(node1).val)  # => 3

    node5.next = node6
    print(middleNode(node1).val)  # => 4

    node6.next = node7
    print(middleNode(node1).val)  # => 4


if __name__ == "__main__":
    main()
    