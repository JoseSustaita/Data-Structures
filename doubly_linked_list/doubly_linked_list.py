"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        s = ""
        node = self.head
        while node != None:
            s += f"{str(node.value)}, "
            node = node.next
        return s[:-2]
    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # Create a new node
        new_node = ListNode(value)
        # If empty list:
        if self.head is None:
            # Set self.head = new_node
            self.head = new_node
        # Set self.tail = new_node
            self.tail = new_node
        # Else:
        else:
            # Set self.head.prev = new_node
            self.head.prev = new_node
        # Set new_node.next to self.head
            new_node.next = self.head
            # Set self.head = new_node
            self.head = new_node
            # New_node.previous = none
            # just to be explicit
            new_node.prev = None
        # increment
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # old head is head
        old_head = self.head
        # new head is the old head's next
        new_head = old_head.next
        if new_head:
            # new head perv is set to none
            new_head.prev = None
        # new head becomes head
            self.head = new_head
        else:
            # Head and tail are set to none and length is decremented
            self.head, self.tail = None, None
        self.length -= 1
        return old_head.value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # Create a new node
        new_node = ListNode(value)
        # If empty list:
        if self.tail is None:
            # Set self.head = new_node
            self.head = new_node
        # Set self.tail = new_node
            self.tail = new_node
        # Else:
        else:
            # Set self.head.prev = new_node
            self.tail.next = new_node
        # Set new_node.next to self.head
            new_node.prev = self.tail
            # Set self.head = new_node
            self.tail = new_node
            # New_node.previous = none
            # just to be explicit
            new_node.next = None
        # increment
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # old tail is tail
        old_tail = self.tail
        # if old tail is none
        if old_tail == None:
            return None
        # New tails becomes old tail's prev
        new_tail = old_tail.prev
        if new_tail:
            # New tail next is none
            new_tail.next = None
            # new tail become tail
            self.tail = new_tail
        else:
            # head and tail are set to none and length is decremented
            self.head, self.tail = None, None
        self.length -= 1
        return old_tail.value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # Delete method
        self.delete(node)
        # node we are moving becomes head
        new_node = self.head
        self.head = node
        # head's next becomes
        self.head.next = new_node
        # head's prev is set to none
        self.head.prev = None
        # new node's prev becomes new head
        new_node.prev = self.head
        self.length += 1

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # Delete method
        self.delete(node)
        # node we want to move becomes tail's next
        self.tail.next = node
        # nodes prev is tail
        node.prev = self.tail
        # node's next is set to none
        node.next = None
        # node we moved becomes tail
        self.tail = node
        self.length += 1

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node: ListNode):
        # Check for empty pointers
        # Get previous node = node.prev
        previous_node = node.prev
        # Set prev_node.next to node.next
        if previous_node is None:
            # could just call self.remove_from_head()
            self.head = node.next
        else:
            previous_node.next = node.next
        # Next_node = node.next
        next_node = node.next
        # Set next_node.previous = previous_node
        if next_node is None:
            self.tail = node.prev
        else:
            next_node.prev = previous_node
        # Decrement length
        self.length -= 1
        # Set node.prev = None
        node.prev = None
        # Set node.next = None
        node.next = None
        # Return node.value
        return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # If length == 0 return None
        if self.length == 0:
            return None
        # If length == 1 return self.head.value
        if self.length == 1:
            return self.head.value
        # Current_max starts out as self.head.value
        current_max = self.head.value
        # Iterate through the list
        current_node = self.head
        # Stop when current_node is None
        while current_node is not None:
            # Compare current_max to each value and update current_max if value > current_max
            if current_max < current_node.value:
                current_max = current_node.value
        # Move current_node forward
            current_node = current_node.next
        # Return current_max
        return current_max
