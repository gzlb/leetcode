class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    def reorder_list(head:Node) -> None:
        
        slow, fast = head, head.next 


        #1. FIND MIDDLE 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

        #2. REVERSE SECOND HALF 
        second = slow.next 
        prev = slow.next = None 

        while second is not None:
            tmp = second.next
            second.next = prev 
            prev = second 
            second = tmp 

        
        #3 MERGE THE LIST 
        first, second = head, prev
        while second is not None: 
            tmp1, tmp2 = first.next, second.next 
            first.next = second 
            second.next = first 
            first = tmp1
            second = tmp2 





