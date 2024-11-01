# node.py
class Node:
    def __init__(self, value=0, children=None):
        self.value = value  # Value of the node (for leaf nodes, this is the score)
        self.children = children if children is not None else []  # List of child nodes

    def is_terminal(self):
        return len(self.children) == 0
