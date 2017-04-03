from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        if elements:
            for elem in elements:
                self.append(elem)       # Calling the append method defined below

    def __str__(self):
        listing = [elem2 for elem2 in self]
        return ("[" + ", ".join(["%d"] * len(listing)) + "]") % tuple(listing)

    def __len__(self):
        return self.count()             # Ensuring we can get the number of elements in a list through 
                                        # len() as well as count()

    def __iter__(self):                 # Building the LinkedList by calling up the Node references until 
        node = self.start               # the next attribute is None (end of list)
        while node:
            yield node.elem
            node = node.next
        raise StopIteration

    def __getitem__(self, index):       # Enabling index searches for the LinkedList
        if (index >= len(self)) or (len(self) == 0):
            raise IndexError
        
        for i,elem in enumerate(self):
            if i == index:
                return elem

    def __add__(self, other):           # Enabling list concatenation by creating a new LinkedList
        listing = LinkedList(elem2 for elem2 in self)
        
        for elem in other:
            listing.append(elem)
        
        return listing

    def __iadd__(self, other):          # Enabling list concatenation by modifying original LinkedList
        for elem in other:
            self.append(elem)
        
        return self

    def __eq__(self, other):            # Enabling comparision of equality
        if len(self) != len(other):     # Checking both lists are the same length
            return False
        
        elif (len(self) and len(other)) == 0:   # Checking if both lists are empty
            return True
        
        for e1,e2 in zip(self, other):          # Comparing each pair of elements at the same index
            if e1 != e2:
                return False
        
        return True

    def __ne__(self, other):            # Enabling comparision of inequality
        return not self.__eq__(other)

    def append(self, elem):
        if self.start is None:          # If the LinkedList is currently empty
            self.start = Node(elem)     # Creating the fist element
            self.end = self.start       # Keeping track of the last element
            return self.start
        
        # If the LinkedList isn't empty:
        new_node = Node(elem)           # Creating a new node
        
        # Updating the end node with the new node added to the LinkedList
        self.end.next = new_node        # Updating the Node reference
        self.end = new_node             # Updating the LinkedList

    def count(self):
        counter = 0
        for elem in self:
            counter += 1
        
        return counter

    def pop(self, index=None):
        if (len(self) == 0) or (index >= len(self)):    # Checking the LinkedList is not empty
            raise IndexError                            # and that the index given is valid
        
        if index is None:                               # If no index is given, assign it the position of
            index = self.count() - 1                    # the last element
        
        if index == 0:                                  # Removing the first element
            elem = self.start.elem                      # Capturing the value of the first element
            self.start = self.start.next                # Modifying the LinkedList to begin at the next element
            return elem
        
        # Removing an element elsewhere in the LinkedList:
        i = 0                                           # Setting up the variables at the beginning of the
        prev_node = None                                # LinkedList
        cur_node = self.start
        
        while True:
            if i == index:                              # Looping through the list until the given index is reached
                prev_node.next = cur_node.next          # Updating the node references so that the previous node refers to the next node, thus effectively removing the current node from the LinkedList
                return cur_node.elem                    # Breaking the loop and returning the removed element
            prev_node = cur_node                        # Updating variables to keep looping until the right element is reached
            cur_node = cur_node.next
            i += 1