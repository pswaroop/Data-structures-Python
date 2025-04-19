from Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head=None
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        if self.head is not None:
            print("None")
        else:
            print("Nothing to Display")
    
    def deleteNode(self, elm):
        temp = self.head
        if temp and temp.data==elm:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data!=elm:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def insertAtStart(self,data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode
    
    def insertAtEnd(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = NewNode

    def rev_display(self):
        li = []
        temp = self.head
        while temp:
            li.append(temp.data)
            temp=temp.next
        li = li[::-1]
        for elm in li:
            print(elm,end="->")
        print("None")

    def _rev_display_recursive(self, node):
        if node is None:
            return
        self._rev_display_recursive(node.next)
        print(node.data, end="->")

    def rev_display_recursive(self):
        self._rev_display_recursive(self.head)
        print("None")

    
if __name__ == '__main__':
    ob = SinglyLinkedList()
    ob.insertAtEnd(10)
    # ob.insertAtStart(5)
    # ob.insertAtEnd(20)
    # ob.insertAtEnd(30)
    ob.insertAtEnd(15)
    # ob.insertAtEnd(40)
    ob.display()
    ob.deleteNode(15)
    ob.deleteNode(10)
    ob.display()
    #ob.rev_display_recursive()