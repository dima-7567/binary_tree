class Node:
    def __init__(self, parent, left_child=None, right_child=None):
        self.parent = parent
        if left_child is not None:
            self.left_child = Node(left_child)
        else:
            self.left_child = None
        if right_child is not None:
            self.right_child = Node(right_child)
        else:
            self.right_child = None


class TreeHandler:
    """
    |creation                    |
    |balancing                   |
    |creation with balancing     |
    |find element                |
    |append node                 |
    |delete node                 |
    """

    # method creates tree from list
    def create_btree(self, in_data: tuple) -> Node:
        tree = Node(in_data[0])
        for el in range(len(in_data)):
            self.__insert_el(in_data[el], tree)
        return tree

    # auxiliary method for previous, insert element in tree as sheet
    # private method
    def __insert_el(self, el: int, tree: Node) -> None:
        if el > tree.parent:
            if tree.right_child is None:
                tree.right_child = Node(el)
                return
            else:
                self.__insert_el(el, tree.right_child)
        elif el < tree.parent:
            if tree.left_child is None:
                tree.left_child = Node(el)
                return
            else:
                self.__insert_el(el, tree.left_child)
        else:
            return


class TreePrint:
    """
    for debug
    print the tree
    traversals
    """
    def __init__(self, tree: Node):
        self.tree = tree

    # print tree as tree
    def __call__(self, high: int) -> None:
        for i in range(high):
            print(end=" " * ((2 ** (high - 1)) - i ** 2))
            self.print_level(self.tree, level=i)
            print()

    # auxiliary method for previous, get all heirs in {level} generation
    def print_level(self, *trees: Node, level: int) -> None:
        if level != 0:
            for tree in trees:
                if tree is None:
                    self.print_level(Node("."), Node("."), level=level - 1)
                else:
                    if tree.left_child is None:
                        tree.left_child = Node(".")
                    if tree.right_child is None:
                        tree.right_child = Node(".")
                    self.print_level(tree.left_child, tree.right_child, level=level - 1)

        else:
            for tree in trees:
                if tree is not None:
                    if tree.parent is not None:
                        print(tree.parent, end=" ")
                    else:
                        print(" ", end=" ")
                else:
                    print(" ", end=" ")

    # binary tree traversals {
    def infix_tree(self, tree: Node) -> list:
        sp = []
        if self.tree.left_child is not None:
            self.infix_tree(self.tree.left_child)
        sp.append(self.tree.parent)
        if self.tree.right_child is not None:
            self.infix_tree(self.tree.right_child)
        return sp

    def prefix_tree(self, tree: Node) -> list:
        sp = [self.tree.parent]
        if self.tree.left_child is not None:
            self.infix_tree(self.tree.left_child)
        if self.tree.right_child is not None:
            self.infix_tree(self.tree.right_child)
        return sp

    def postfix_tree(self, tree: Node) -> list:
        sp = []
        if self.tree.left_child is not None:
            self.infix_tree(self.tree.left_child)
        if self.tree.right_child is not None:
            self.infix_tree(self.tree.right_child)
        sp.append(self.tree.parent)
        return sp
    #                        }


test_ = [6, 7, 8, 2, 1, 3, 4, 5, 9]

tree_ = TreeHandler()




