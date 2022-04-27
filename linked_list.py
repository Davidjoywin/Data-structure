"""
linked list implementtion from
insertion
deletion
count and so on
"""

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insertionAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            self.count += 2
            return

        while self.head.next != None:
            self.head = self.head.next
        self.head.next = new_node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
llist = LinkedList()

print(llist.insertionAtEnd(3))
