#Nodes and Pointers

#Initializes a node with the given value (data), and sets its next and prev pointers to None.
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

#Doubly Linked List
class DoublyLinkedList():
  #Initializes an empty doubly linked list, setting head, tail to None and length to 0.
  def __init__(self):

    self.head = None
    self.tail = None
    self.length = 0

#Returns a string representation of the list by traversing from head to tail and collecting 
#all data values.  
  def __str__(self):
    temp = self.head
    s = '['
    while temp is not None:
      s = s + str(temp.data) + ', '
      temp = temp.next
    s = s + ']'
    return s

#Get the length of a doubly linked list
  def get_length(self):
    return self.length()

#Prints the list elements from head to tail in a bracketed format.
  def print(self):

    temp = self.head

    print('[', end='')
    while temp is not None:
      print(temp.data, end=', ')
      temp = temp.next
    print(']')

#Add an element at the end of the doubly linked list
  def append(self, data):

    new_node = Node(data)

    if self.length == 0: #if the list is empty
      self.head = new_node
      self.tail = new_node

    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node

    self.length += 1

#Remove an element from the end of the doubly linked list
  def pop(self):

    if self.length == 0: #if the list is empty
      return None

    temp = self.tail

    if self.length == 1: #if the list has only one element
      self.head = None
      self.tail = None

    else:
      self.tail = temp.prev
      self.tail.next = None
      temp.prev = None

    self.length -= 1

    return temp

#Pop an element and raise an exception if the DLL is empty.
  def pop_we(self):
    if self.length == 0:
      raise Exception('Error: Attempted to pop from an empty DLL.')
    temp = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      temp.prev = None
    self.length -= 1
    return temp

#Add an element at the beginning of a doubply linked list
  def prepend(self,data):
    new_node = Node(data)

    if self.length == 0: #if the list is empty
      self.head = new_node
      self.tail = new_node

    else:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node

    self.length += 1

#Removes and returns the first element of the list.
  def pop_first(self):
    if self.length == 0: #if the list is empty
      return None

    temp = self.head
    if self.length == 1: #if the list has only one element
      self.head = None
      self.tail = None

    else:
      self.head = temp.next
      self.head.prev = None
      temp.next = None

    self.length -= 1

    return temp

#Returns the node at position index. If the index is invalid, returns None.
  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    for i in range(index):
      temp = temp.next
    return temp

  def set_value(self, index, data):
    temp = self.get(index)
    if temp is not None:
      temp.data = data

#insert the value data at the left of the element with a given index index
  def insert(self, index, data):
    if index < 0 or index > self.length:
      raise IndexError('Index out of Bounds') #does not make sense to return None
    if index == 0:
      self.prepend(data)
    elif index == self.length: #the last element has index n-1, so I want to insert the new element on the right of the last one
      self.append(data)
    else:
      u = Node(data)
      before = self.get(index-1) # previously defined
      after = before.next
      u.next=after
      u.prev=before
      after.prev=u
      before.next=u
      self.length+=1

#Removes the node at position index and returns it. Handles cases for removing the first or last element separately.
  def remove(self, index):
    if index < 0 or index >= self.length:
      return None  # alternatively raise an exception
    if index == 0:
      return self.pop_first() # previously defined
    elif index == self.length-1:
      return self.pop() # previously defined
    else:
      temp = self.get(index) # previously defined

      before = temp.prev
      after = temp.next
      before.next = after
      after.prev = before
      temp.prev = None
      temp.next = None

      self.length-=1
      return temp

#Traverses the list to find the first occurrence of data. Returns its index if found, otherwise None
  def search(self, data):
    if self.length == 0:
        return None  # alternatively raise an exception
    temp = self.head
    for i in range(self.length):
        if temp.data == data:
            return i
        temp = temp.next
    return None

# Some examples
dll = DoublyLinkedList()
dll.print()

#Adding the numbers from 0 to 4 as elements in the list:
n = 5
for i in range(n):
  dll.append(i)
print(dll)

#Removing an element from the end of the list:
popped_element = dll.pop()
print(f'We removed the element {popped_element.data}. The list is now composed by:')
print(dll)

#Adding elements at the beginning of a list:
dll.prepend(54)
print(dll)

#Removing elements at the beginning of a list:
popped_element = dll.pop_first()
print(f'We removed the element {popped_element.data} from the beginning of the list.\nThe list is now composed by:')
print(dll)

#Get an element by its index:
i = 2
node = dll.get(i)
print(f'The element in position {i} is : {node.data}')

#Modify the value of an element by its index:
i = 2
data = 46
node = dll.set_value(i, data)
print(dll)

#Search an element by its value:
data = 46
index = dll.search(data)
print(f'The element {data} is in position {index}')

#Insert an element such that after the insertion it will get a desired index:
dll.insert(2, 78)
print(dll)

#Remove the element with a specific index:
popped_element = dll.remove(2)
print(f'We removed the element {popped_element.data} from the beginning of the list.\nThe list is now composed by:')
print(dll)


# Private and Protected Attributes
class Example:
  def __init__(self, value):
      self.__private_attribute = value  # Private attribute

  def get_private_attribute(self):
      return self.__private_attribute  # Access method

  def set_private_attribute(self, value):
      self.__private_attribute = value  # Modifying method

obj = Example(10)
print(obj.get_private_attribute())  # Outputs: 10
obj.set_private_attribute(20)
print(obj.get_private_attribute())  # Outputs: 20

class Example:
  def __init__(self, value):
      self._protected_attribute = value  # Protected attribute

  def get_protected_attribute(self):
      return self._protected_attribute   # Access method

  def set_protected_attribute(self, value):
      self._protected_attribute = value  # Modifying method

obj = Example(10)
print(obj.get_protected_attribute())  # Outputs: 10
obj.set_protected_attribute(20)
print(obj.get_protected_attribute())  # Outputs: 20



# Queues
class  node():
  def __init__(self, data):
    self.data = data
    self.next = None

#Initializes an empty queue. 
#first: points to the front (head) of the queue.
#last: points to the end (tail) of the queue.
class Queue():
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

#Displays the queue contents in this way:
#prints underscores (__) as placeholders for elements.
#shows the elements from first to last.
#indicates direction with <- .
 
  def print(self):
    print('\t', end='')
    for _ in range(self.length):
      print('__', end=' ')
    print('\n')
    print('<-\t', end ='')
    temp = self.first
    while temp is not None:
      print(temp.data, end=', ')
      temp = temp.next
    print('\t<-\n')
    print('\t', end='')
    for _ in range(self.length):
      print('__', end=' ')

#Adds (enqueue) an element at the end of the queue.
  def enque(self, data):
    new_node = node(data)
    if self.length==0:
      self.first = new_node
      self.last = new_node
    else:
      self.last.next = new_node
      self.last = new_node
    self.length += 1

#Removes (dequeue) and returns the element at the front of the queue.
  def deque(self):

    if self.length==0:
      return None

    temp = self.first
    if self.length == 1:
      self.first = None
      self.last = None
    else:
      self.first = temp.next
      temp.next = None
    self.length -= 1

    return temp



# Stacks
#Defines a node that contains the value stored (data) and a pointer/reference to the 
#next node in the stack (default is None)
class Node2():
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack():
  def __init__(self):
    self.top = None
    self.height = 0

#Prints a visual representation of the stack
  def print(self):
    temp = self.top
    for _ in range(self.height):
      print('__', end=' ')
    print('\n')
    while temp is not None:
      print(temp.data, end=', ')
      temp = temp.next
    print('|')
    for _ in range(self.height):
      print('__', end=' ')

#Adds a new element on top of the stack.
  def push(self, data):
    new_node = Node2(data)
    if self.height == 0:
      self.top = new_node
    else:
      new_node.next = self.top
      self.top = new_node
    self.height += 1

#Removes and returns the top element of the stack.
  def pop(self):
    if self.height==0:
      return None

    else:
      temp = self.top
      self.top = temp.next
      temp.next = None

    self.height -= 1
    return temp

#Create the stack and fill it with elements to test the push method:
s = Stack()
for i in range(4):
  s.push(i**2)
s.print()
#Test the pop method:
popped_element = s.pop()

print(f'We popped an element with value {popped_element.data}')
s.print()



# Binary Search Trees
class Node3 ():
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

#Represents the whole tree. root: reference to the root node (the top of the tree).
#size: number of nodes inserted.

class BinarySearchTree():
  def __init__(self):
    self.root = None
    self.size = 0

#It prints the right subtree first, then the current node, then the left subtree
  def print(self):

    def print_tree(node, level = 0):
      if node != None:
          print_tree(node.right, level + 1) 
          print(" " * 7 * level + "-> " + str(node.data))
          print_tree(node.left, level + 1)

    print_tree(self.root)


#Inserts a new node.
#If tree is empty the new node becomes the root.
#Otherwise:
#If data < temp.data, go left.
#If data > temp.data, go right.
#If data == temp.data, do nothing (no duplicates allowed).
#Increases size each time a node is added.
#Returns True if insertion succeeds, False if duplicate.
 
  def insert(self, data):

    new_node = Node3(data)

    if self.root is None:
      self.root = new_node
      self.size +=1
      return True
    
    temp = self.root
    while True:
      if data < temp.data:
        if temp.left is None:
          temp.left = new_node
          self.size +=1
          return True
        temp = temp.left

      elif data > temp.data:
        if temp.right is None:
          temp.right = new_node
          self.size +=1
          return True
        temp = temp.right

      else:
        return False


#Searches for a value in the tree
  def contains(self, data):

    if self.root is None:
      return False

    temp = self.root
    while temp is not None:
      if data < temp.data:
        temp = temp.left
      elif data > temp.data:
        temp = temp.right
      else: 
        return True
    
    return False

#Finds the minimum value in the tree
  def find_min(self):
    if self.root is None:
      return None

    temp = self.root

    while temp.left is not None:
      temp = temp.left

    return temp.data


#Fill the tree with random integers
import random
random.seed(100)
bst = BinarySearchTree()

for i in range(20):
  bst.insert(random.randint(0, 100))

bst.print()
#Check if the tree contains the value 22
bst.contains(22)
#Check if the tree contains the value 83
bst.contains(83)
#Find the min
bst.find_min()





