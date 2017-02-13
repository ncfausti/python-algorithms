"""
Some functions that work with linked lists.

1. Given a singly linked list, write a funcction to find
the nth-to-last element of the list.
"""


class Node:
    """Node object to be used in linked lists.

    Some summary text here.
    """

    def __init__(self, val):
        """
        Node object to be used in linked lists.

        Some summary text here.
        """
        self.value = val
        self.next = None


def nth_to_last(node, n):
    """Return the nth to last node in a linked list."""
    curr = node
    follower = node
    i = 0
    while curr.next is not None:
        if i >= n:
            follower = follower.next
        i += 1
        curr = curr.next

    return follower.value

# Setup linked list here
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

print(nth_to_last(a, 0))
