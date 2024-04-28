
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deleteMid(self,head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        slow = head
        faste = head
        # data = Node()
        while faste is not None and faste.next is not None and faste.next.next is not None:
            slow=slow.next
            faste = faste.next.next
        
        if slow == head and slow.next == None:
            return None
        elif slow == head:
            return None
    
        slow.next=slow.next.next
        return head
  
        #code here


list1 = Node(2)
list1.next = Node(3)
list1.next.next =Node(4)
list1.next.next.next =Node(6)
list1.next.next.next.next =Node(9)
obj= Solution()
linkedList= obj.deleteMid(list1)
while linkedList:
    print(linkedList.data , end=',')
    linkedList = linkedList.next