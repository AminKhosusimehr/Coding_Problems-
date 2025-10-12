class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        fake_node = ListNode()
        current = fake_node
        while list1 and list2 : 
            if list1.val <= list2.val :  
                current.next = list1     
                list1 = list1.next
            else : 
                current.next = list2     
                list2 = list2.next
            current = current.next  

        if list1 != None : 
            current.next = list1
        elif list2 != None : 
            current.next = list2 
        else : 
            current.next = None
            
        return fake_node.next