# Define a class for the linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a class for the linked list itself
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a new node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="\n")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    # Create a linked list instance
    linkedlist = LinkedList()
    def clg(clgname):
         if(clgname=="MIT college"):
              linkedlist.append("MIT College")
              linkedlist.append("president Dr.YK Patil")
              linkedlist.append("vice_president Dr. JK Sharma")
              linkedlist.append("principal MR. Vinod Bairagi")
              linkedlist.append("branches 5")
              linkedlist.append("Teachers 10")
         if(clgname=="polytechnic"):
              linkedlist.append("polytechnic mds")
              linkedlist.append("president Dr.patidar sir")
              linkedlist.append("vice_president Dr. pathak sir")
              linkedlist.append("principal MR. sharma sir")
              linkedlist.append("branches 4")
              linkedlist.append("Teachers 8")
    cname=input("Enter College name ")
    clg(cname)
    linkedlist.print_list()
        
