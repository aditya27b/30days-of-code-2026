def addOne(self,head):
        last_not_nine = None
        curr = head
        
        while curr:
            if curr.data != 9:
                last_not_nine = curr
            curr = curr.next
    
        if last_not_nine:
            last_not_nine.data += 1
            curr = last_not_nine.next

            while curr:
                curr.data = 0
                curr = curr.next
            return head
            
        else:

            new_head = Node(1) # type: ignore
            new_head.next = head
            curr = head
            while curr:
                curr.data = 0
                curr = curr.next
            return new_head