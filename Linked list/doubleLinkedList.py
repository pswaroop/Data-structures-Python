class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node.prev = temp
        temp.next = new_node

    def display(self, reverse):
        if not self.head:
            print("Nothing to Display")
            return

        if reverse:
            temp = self.head
            while temp.next:
                temp = temp.next
            while temp:
                print(temp.data, end="->")
                temp = temp.prev
        else:
            temp = self.head
            while temp:
                print(temp.data, end="->")
                temp = temp.next
        print("None")

    def deleteNode(self, elm):
        temp = self.head

        if not temp:
            return

        if temp.data == elm:
            if temp.next:
                temp.next.prev = None
            self.head = temp.next
            return

        while temp and temp.data != elm:
            temp = temp.next

        if not temp:
            return "Element not found in the list"

        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

if __name__ == '__main__':
    ob = DoubleLinkedList()
    ob.insertAtEnd(10)
    ob.insertAtStart(5)
    ob.insertAtEnd(20)
    ob.insertAtEnd(30)
    ob.insertAtEnd(15)
    ob.insertAtEnd(40)
    ob.display(0)  # Forward
    ob.deleteNode(15)
    ob.deleteNode(10)
    ob.display(0)  # Forward after deletion
    ob.display(1)  # Reverse
