"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: BSTNode = None  # Either a BSTNode or None
        self.right: BSTNode = None
    # Insert the given value into the tree

    def insert(self, value):
        # Compare target value to node.value
        # If value > node.value:
        if value >= self.value:
            # Go right
            # If node.right is None:
            if self.right is None:
                # Create the new node there
                self.right = BSTNode(value)
            else:  # self.right is a BSTNode
                # Do the same thing (aka recurse)
                # Insert value into node.right
                # right_child is a BSTNode, so we can call insert on it
                right_child = self.right
                right_child.insert(value)
        # Else if value < node.value
        if value < self.value:
            # Go Left
            # If node.left is None:
            if self.left is None:
                # Create node
                self.left = BSTNode(value)
            else:
                # Do the same thing
                # (compare, go left or right)
                # Insert value into node.left
                left_child = self.left
                left_child.insert(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        node = self

        def search(node, target):
            # If root is none there are no values
            if node == None:
                return False
            # Checks if vlaue matches target
            if node.value == target:
                return True
            # If root is larger then return the result of the the left sub-tree
            elif target < node.value:
                return search(node.left, target)
            # Else if root is smaller then return the result of the the right sub-tree

            else:
                return search(node.right, target)

        return search(node, target)

    def get_max(self):
        # the node with the maximum value will also be the right-most node
        if self.right is None:
            # Base Case
            # We're already at the right most node
            return self.value
        else:
            # Recursive case: make the problem smaller to get to the base case
            # Go right
            return self.right.get_max()
        # iterate get_max():
        # start at the root (self)
        cur_node = self
        # keep going right until you can't anymore
        # --> stop when cur_node.right is None
        while cur_node.right is not None:
            # move closer to the "base case"
            cur_node = cur_node.right
        # return
        # "base case"
        return cur_node.value
    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # Will have to look at both branches
        # Start at the root
        fn(self.value)
        if self.left is not None:
            # Go left
            self.left.for_each(fn)
        if self.right is not None:
            # Go right
            self.right.for_each(fn)

    # Part 2 -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        pass
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        pass
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):
        pass
    # Stretch Goals -------------------------
    # Note: Research may be required
    # Print Pre-order recursive DFT

    def pre_order_dft(self):
        pass
    # Print Post-order recursive DFT

    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# # print("in order")
# # bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
