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


def print_level(*trees, level: int):
    if level != 0:
        for tree in trees:
            if tree is None:
                print_level(Node("."), Node("."), level=level - 1)
            else:
                if tree.left_child is None:
                    tree.left_child = Node(".")
                if tree.right_child is None:
                    tree.right_child = Node(".")
                print_level(tree.left_child, tree.right_child, level=level - 1)

    else:
        for tree in trees:
            if tree is not None:
                if tree.parent is not None:
                    print(tree.parent, end=" ")
                else:
                    print(" ", end=" ")
            else:
                print(" ", end=" ")


def print_b_tree(tree, high):
    for i in range(high):
        print(end=" " * ((2 ** (high - 1)) - i ** 2))
        print_level(tree, level=i)
        print()


def create_btree(in_data: tuple):
    tree = Node(in_data[0])
    for el in range(len(in_data)):
        insert_el(in_data[el], tree)
    return tree


def insert_el(el: int, tree: Node):
    if el > tree.parent:
        if tree.right_child is None:
            tree.right_child = Node(el)
            return
        else:
            insert_el(el, tree.right_child)
    elif el < tree.parent:
        if tree.left_child is None:
            tree.left_child = Node(el)
            return
        else:
            insert_el(el, tree.left_child)
    else:
        return


def print_tree(tree: Node):
    if tree.left_child is not None:
        print_tree(tree.left_child)
    print(tree.parent, end=" ")
    if tree.right_child is not None:
        print_tree(tree.right_child)


btree = create_btree((5, 6, 9, 8, 7, 1, 2, 3, 4))

