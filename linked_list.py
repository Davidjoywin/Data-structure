"""
linked list implementtion from
insertion
deletion
traversing
count and so on
"""

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insertionAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.count += 1
            return

        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
        self.count += 1

    def printAll(self):
        while self.head is not None:
            print(self.head.data, "->", end=" ")
            self.head = self.head.next
        print()

    def getLength(self):
        return self.count


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
llist = LinkedList()

llist.insertionAtEnd(5)
llist.insertionAtEnd(7)
llist.insertionAtEnd(8)
llist.insertionAtEnd(9)

llist.printAll()

print(llist.getLength())


