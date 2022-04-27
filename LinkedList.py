class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            return
        
        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node



llist = LinkedList()

llist.add(1)
llist.add(2)
llist.add(3)
llist.add(4)
ls = ""
while llist.head != None:
    ls += f"{llist.head.data} --> " 
    llist.head = llist.head.next;

print(ls)
