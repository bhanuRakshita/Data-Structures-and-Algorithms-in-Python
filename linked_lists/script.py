# We'll be using our Node class
class Node:
  def __init__(self, value = None, next_node = None):
    self.value = value
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
    def __init__(self):
        self.head_node = None

    def print_list(self):
       current_node = self.head_node
       while(current_node):
            print(current_node.value)
            current_node = current_node.next_node

    def insert_beginning(self, value):
       
       new_node = Node(value)
       if self.head_node: 
        new_node.next_node = self.head_node
       else:
        new_node.next_node = None
       self.head_node = new_node

    def insert_end(self, value):
        new_node = Node(value)
        current_node = self.head_node
        while(current_node):
            if(current_node.next_node is None):
               current_node.next_node = new_node
               break
            else: 
               current_node = current_node.next_node

    def remove(self, value):
       curr = self.head_node
       while curr:
          if curr.next_node and curr.next_node.value == value:
             del_node = curr.next_node
             curr.next_node = curr.next_node.next_node
             del del_node
          
          curr = curr.next_node
     

# Create a linked list with some initial values
linked_list = LinkedList()
linked_list.insert_beginning(10)
linked_list.insert_beginning(20)
linked_list.insert_beginning(30)
linked_list.insert_beginning(40)
linked_list.insert_beginning(30)
linked_list.insert_beginning(50)

# Print the initial linked list
print("Initial Linked List:")
linked_list.print_list()

# Remove a node with a specific value (e.g., 30)
value_to_remove = 30
linked_list.remove(value_to_remove)

# Print the linked list after removing the node
print(f"\nLinked List after removing node with value {value_to_remove}:")
linked_list.print_list()

# # Insert a new node at the beginning
# new_value = 5
# linked_list.insert_end(new_value)

# # Print the linked list after inserting a new node at the beginning
# print(f"\nLinked List after inserting a new node with value {new_value} at the beginning:")
# linked_list.print_list()
