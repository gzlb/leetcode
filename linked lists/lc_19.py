class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    def remove_nth_node(head: Node, n) -> Node:
        
        dummy = Node(0, head)
        left = dummy 
        right = head 

        while n > 0 and right is not None:
            right = right.next 
            n -= 1 

        while right: 
            right = right.next
            left = left.next 

        
        left.next = left.next.next 

        return dummy.next 


